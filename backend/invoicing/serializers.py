from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields=['id', 'sale', 'invoice_number', 'pdf_file', 'email_sent', 'email_sent_at', 'created_at']