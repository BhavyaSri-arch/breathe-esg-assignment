from django.contrib import admin
from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return Response({"message": "Backend Working"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/records/', home),
]