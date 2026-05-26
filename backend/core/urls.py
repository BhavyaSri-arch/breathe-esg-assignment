from django.contrib import admin
from django.urls import path
from ingestion.views import get_records

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/records/', get_records),
]