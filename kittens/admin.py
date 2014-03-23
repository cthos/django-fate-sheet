from django.contrib import admin
from kittens.models import Kitten

class KittenAdmin(admin.ModelAdmin):
  list_display = ['name', 'breed']

# Register your models here.
admin.site.register(Kitten, KittenAdmin)
