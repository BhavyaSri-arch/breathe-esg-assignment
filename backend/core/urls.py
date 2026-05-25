from django.contrib import admin
from django.urls import path
from ingestion.views import get_records, upload_sap_csv

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/records/', get_records),
    path('api/upload/', upload_sap_csv),
]