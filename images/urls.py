from django.urls import path
from .views import image_creation,image_detail


urlpatterns = [path('create',image_creation, name  = image_creation),
                path('detail',image_detail, name = 'image_detail')]
