from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .celery import task_scrap_products
from .serializer import ProductSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def root(request):
    """
    Home page for the scraper app.
    """
    return render(request=request, template_name="scraper/root.html")


@api_view(['POST'])
def start_product_scraping(request):
    """
    Schedule the product scraping task.
    """
    task_scrap_products()
    return Response(data={"detail": "scrapping started."}, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def handle_product_data(request):
    """
    Handles product data sent by the worker and forwards it to the WebSocket group.
    This is used internally by the worker to send product details.
    """
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Sent product details to frondend via websocket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "product_group", 
        {
            "type": "send_product_data",
            "product": serializer.validated_data,
        }
    )

    return Response(
        data={'detail': 'Data sent to WebSocket'},
        status=status.HTTP_202_ACCEPTED
        )
