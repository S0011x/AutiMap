from django.contrib import admin
from .models import Request

# Register your models here.

class RequestAdmin(admin.ModelAdmin):
 list_display = ("times","date")



admin.site.register(Request, RequestAdmin)
