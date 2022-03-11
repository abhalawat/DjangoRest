from django.contrib import admin
from .models import Species


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ['name','birth_year','eye_color','species']


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ['first','parent_n']