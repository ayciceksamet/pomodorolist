from django.contrib import admin
from .models import PomodoroList
# Register your models here.


class PomodoroListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(PomodoroList, PomodoroListAdmin)
