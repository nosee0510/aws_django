from django.contrib import admin
from namecard.models import Namecard_TBL

# Register your models here.

@admin.register(Namecard_TBL)
class Namecard_TBLAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')

