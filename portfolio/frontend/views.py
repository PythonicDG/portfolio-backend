from rest_framework import generics
from .models import Menu, ContactMessage
from .serializers import MenuSerializer, ContactMessageSerializer
from django.core.mail import send_mail
from django.conf import settings
import threading

class PortfolioContentView(generics.ListAPIView):
    queryset = Menu.objects.filter(is_active=True).order_by('order')
    serializer_class = MenuSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        subject = f"New Contact Message: {contact.subject}"
        message = (
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Location: {contact.location}\n"
            f"Budget: {contact.budget}\n"
            f"Message:\n{contact.message}"
        )

        def send_contact_email():
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['dipakgaikwadmg@gmail.com'],
                fail_silently=False,
            )

        threading.Thread(target=send_contact_email).start()