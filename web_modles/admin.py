from django.contrib import admin
from web_modles import models
# Register your models here.


@admin.register(models.Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('hostname','last_time','join_time','is_pem')


@admin.register(models.Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'source_ip')
    search_fields = ('name', 'url')


@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('url','code','source_code', 'create_time')