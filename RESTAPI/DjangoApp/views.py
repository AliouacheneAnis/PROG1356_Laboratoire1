from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from DjangoApp.serializers import UserSerializer, GroupSerializer

# lien vers templates HTML
def Resource1(request):
    return render(request, 'DjangoApp/Resource1.html')

def Resource2(request):
    return render(request, 'DjangoApp/Resource2.html')

def Resource3(request):
    return render(request, 'DjangoApp/Ressource3.html')

def Resource4(request):
    return render(request, 'DjangoApp/Ressource4.html')

#endpoint 
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
