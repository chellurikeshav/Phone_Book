from rest_framework import viewsets
from . import models
from . import serializers

class ContactViewset(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer