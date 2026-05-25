import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    Company,
    DataSource,
    RawRecord,
    EmissionRecord
)

from .serializers import EmissionRecordSerializer


@api_view(['POST'])
def upload_sap(request):

    file = request.FILES['file']

    df = pd.read_csv(file)

    company, _ = Company.objects.get_or_create(
        name="Demo Company"
    )

    source = DataSource.objects.create(
        company=company,
        source_type='sap',
        uploaded_file=file
    )

    for index, row in df.iterrows():

        suspicious = False

        quantity = float(row['Quantity'])

        if quantity < 0:
            suspicious = True

        RawRecord.objects.create(
            source=source,
            raw_json=row.to_dict(),
            row_number=index,
            ingestion_status='success'
        )

        EmissionRecord.objects.create(
            company=company,
            source=source,
            category='Fuel',
            scope='Scope 1',
            activity_date=row['PostingDate'],
            quantity=quantity,
            unit=row['Unit'],
            normalized_unit='L',
            emission_factor=2.68,
            calculated_emission=quantity * 2.68,
            suspicious=suspicious
        )

    return Response({
        "message": "SAP data uploaded successfully"
    })

@api_view(['POST'])
def upload_utility(request):

    file = request.FILES['file']

    df = pd.read_csv(file)

    company, _ = Company.objects.get_or_create(
        name="Demo Company"
    )

    source = DataSource.objects.create(
        company=company,
        source_type='utility',
        uploaded_file=file
    )

    for index, row in df.iterrows():

        suspicious = False

        usage = float(row['kWh'])

        if usage > 10000:
            suspicious = True

        RawRecord.objects.create(
            source=source,
            raw_json=row.to_dict(),
            row_number=index,
            ingestion_status='success'
        )

        EmissionRecord.objects.create(
            company=company,
            source=source,
            category='Electricity',
            scope='Scope 2',
            activity_date=row['BillingStart'],
            quantity=usage,
            unit='kWh',
            normalized_unit='kWh',
            emission_factor=0.82,
            calculated_emission=usage * 0.82,
            suspicious=suspicious
        )

    return Response({
        "message": "Utility data uploaded successfully"
    })
@api_view(['GET'])
def get_records(request):

    records = EmissionRecord.objects.all()

    serializer = EmissionRecordSerializer(
        records,
        many=True
    )

    return Response(serializer.data)


@api_view(['POST'])
def approve_record(request, pk):

    record = EmissionRecord.objects.get(id=pk)

    record.status = 'approved'

    record.save()

    return Response({
        "message": "Record approved"
    })
@api_view(['POST'])
def upload_travel(request):

    file = request.FILES['file']

    df = pd.read_csv(file)

    company, _ = Company.objects.get_or_create(
        name="Demo Company"
    )

    source = DataSource.objects.create(
        company=company,
        source_type='travel',
        uploaded_file=file
    )

    for index, row in df.iterrows():

        suspicious = False

        distance = row['DistanceKM']

        if pd.isna(distance):
            suspicious = True
            distance = 0

        RawRecord.objects.create(
            source=source,
            raw_json=row.to_dict(),
            row_number=index,
            ingestion_status='success'
        )

        EmissionRecord.objects.create(
            company=company,
            source=source,
            category='Business Travel',
            scope='Scope 3',
            activity_date='2026-01-01',
            quantity=float(distance),
            unit='km',
            normalized_unit='km',
            emission_factor=0.15,
            calculated_emission=float(distance) * 0.15,
            suspicious=suspicious
        )

    return Response({
        "message": "Travel data uploaded successfully"
    })