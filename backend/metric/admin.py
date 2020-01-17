from django.contrib import admin
from .models import Metric


class MetricAdmin(admin.ModelAdmin):
  list_display = ['name',  'description',  'value',  'date_registered',]

admin.site.register(Metric,MetricAdmin)