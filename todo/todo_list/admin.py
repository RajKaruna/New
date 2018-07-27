from django.contrib import admin
from . import models


class ListAdmin(admin.ModelAdmin):
	list_display=("item", "completed", "date")


# Register your models here.
admin.site.register(models.List, ListAdmin)
