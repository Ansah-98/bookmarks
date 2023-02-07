from django.urls import path
from .views import image_creation


urlpatterns = [path('create',image_creation, name  = image_creation)]
