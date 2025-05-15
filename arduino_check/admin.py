from django.contrib import admin

from .models import Patient
from .models import Arduino
from .models import ArduinoLog


admin.site.site_header = "Pulso-UI Admin"
admin.site.site_title = "Pulso-UI Admin Portal"
admin.site.index_title = "Pulso-UI Portal"



admin.site.register(Patient)
admin.site.register(Arduino)
admin.site.register(ArduinoLog)