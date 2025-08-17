from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer


class PortfolioContentView(generics.ListAPIView):
    queryset = Menu.objects.all().order_by('order')
    serializer_class = MenuSerializer
