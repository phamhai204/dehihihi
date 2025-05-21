from django.contrib import admin
from .models import Service, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'appointment_date', 'created_at')
    list_filter = ('service', 'appointment_date')
    search_fields = ('user__username', 'service__name')
from .models import Barber

@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule')
