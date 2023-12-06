from django.urls import path, include
from rest_framework import routers
from .views import NoteViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
