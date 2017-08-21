from django import forms
from django.contrib.gis import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget
from .models import Observation


class ObservationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

admin.site.register(Observation, ObservationAdmin)
