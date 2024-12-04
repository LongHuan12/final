from django.contrib import admin

from .models import Property, Reservation

class PropertyAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'price_per_night', 'bedrooms', 'bathrooms', 'guests', 'country', 'category', 'landlord')

admin.site.register(Property, PropertyAdmin)
admin.site.register(Reservation)