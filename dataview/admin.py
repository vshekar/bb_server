from django.contrib import admin

# Register your models here.
from dataview.models import Patient, Donor, Donation, Serology

admin.site.register(Patient)
admin.site.register(Donation)
admin.site.register(Donor)
admin.site.register(Serology)