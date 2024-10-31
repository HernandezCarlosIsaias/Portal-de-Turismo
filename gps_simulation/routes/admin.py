from django.contrib import admin

# Register your models here.

from .models import City, Route, Lugar_Turistico

admin.site.register(City)
admin.site.register(Route)
admin.site.register(Lugar_Turistico)
