from django.contrib import admin
from fatecore.models import *

class AspectsInline(admin.StackedInline):
  model = FateAspect
  extra = 5

class StuntsInline(admin.StackedInline):
  model = FateStunt
  extra = 2

class SkillsInline(admin.TabularInline):
  model = FateSkill
  extra = 6

class CharacterAdmin(admin.ModelAdmin):
  inlines = [SkillsInline, AspectsInline, StuntsInline]
  list_display = ('name', 'refresh', 'physical_stress_boxes', 'mental_stress_boxes')

# Register your models here.
admin.site.register(FateCharacter, CharacterAdmin)
