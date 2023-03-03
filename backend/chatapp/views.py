from django.shortcuts import render
from .serializers import * 
from rest_framework import viewsets      
from .models import *                 

class MessageView(viewsets.ModelViewSet):  
    serializer_class = MessageSerializer   
    queryset = Message.objects.all()   