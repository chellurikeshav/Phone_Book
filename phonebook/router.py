from app.viewsets import ContactViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('contact',ContactViewset)