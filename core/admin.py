from django.contrib import admin
from .models import Position, Service, Employee, Feature


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("position", "is_active", "modified")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service", "icon", "is_active", "modified")

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "is_active", "modified")
    
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "modified")