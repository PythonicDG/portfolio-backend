from django.urls import path
from .views import PortfolioContentView

urlpatterns = [
    path('portfolio/', PortfolioContentView.as_view(), name='portfolio-content'),
]
