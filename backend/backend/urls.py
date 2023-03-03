from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers                 
from chatapp import views                             

router = routers.DefaultRouter()                   
router.register(r'messages', views.MessageView, 'message')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))             
]