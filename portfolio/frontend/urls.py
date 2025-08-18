from django.urls import path
from .views import PortfolioContentView, ContactMessageCreateView

urlpatterns = [
    path('portfolio/', PortfolioContentView.as_view(), name='portfolio-content'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact-message-create'),
]
