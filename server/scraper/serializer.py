from rest_framework.serializers import Serializer, CharField


class ProductSerializer(Serializer):
    title = CharField()
    description = CharField()
    selling_status = CharField()
    product_condition = CharField()
