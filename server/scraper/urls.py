from django.urls import path
from .views import root, start_product_scraping, handle_product_data

urlpatterns = [
    path('', root, name="root"),
    path('products/', start_product_scraping, name="crawler_products"),
    path('internal/handle_products/', handle_product_data, name="internal_handle_products")
]
