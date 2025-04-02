from django.contrib import admin
from .models import Measurement, Order

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]  # Automatically show all columns


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]  # Automatically show all columns