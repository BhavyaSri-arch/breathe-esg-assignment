from django.urls import path

from .views import (
    upload_sap,
    get_records,
    upload_utility,
    upload_travel,
    approve_record
)

urlpatterns = [
    path('upload/sap/', upload_sap),
    path('records/', get_records),
    path('records/<int:pk>/approve/', approve_record),
    path('upload/utility/', upload_utility),
    path('upload/travel/', upload_travel),
]