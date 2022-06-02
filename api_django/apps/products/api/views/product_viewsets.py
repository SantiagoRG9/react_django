from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.base.api import GeneralListApiView


class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer
