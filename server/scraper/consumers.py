import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ScraperConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Add the WebSocket connection to the "product_group"
        await self.channel_layer.group_add(
            "product_group",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the WebSocket connection from the "product_group"
        await self.channel_layer.group_discard(
            "product_group",
            self.channel_name
        )

    async def send_product_data(self, event):
        """
        Send the product data to the WebSocket client
        """
        scraped_data = event['product']
        await self.send(text_data=json.dumps({
            'message': scraped_data
        }))
