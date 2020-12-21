<<<<<<< HEAD
from django.contrib import admin

# Register your models here.
=======
from django.contrib import admin


from .models import Flight, Airport, Passanger
# Register your models here.


class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


class PassangerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passanger, PassangerAdmin)
>>>>>>> 2107349304d3726ad311440039b24188491d769b
