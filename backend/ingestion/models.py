from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):

    SOURCE_CHOICES = [
        ('sap', 'SAP'),
        ('utility', 'Utility'),
        ('travel', 'Travel'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES
    )

    uploaded_file = models.FileField(
        upload_to='uploads/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


class RawRecord(models.Model):

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    raw_json = models.JSONField()

    row_number = models.IntegerField()

    ingestion_status = models.CharField(
        max_length=20
    )

    error_message = models.TextField(
        blank=True
    )


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source = models.ForeignKey(
        DataSource,
        on_delete=models.SET_NULL,
        null=True
    )

    category = models.CharField(max_length=100)

    scope = models.CharField(max_length=20)

    activity_date = models.DateField()

    quantity = models.FloatField()

    unit = models.CharField(max_length=20)

    normalized_unit = models.CharField(max_length=20)

    emission_factor = models.FloatField()

    calculated_emission = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    suspicious = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )