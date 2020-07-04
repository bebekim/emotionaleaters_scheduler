from django.contrib import admin
from .models import *

class ActAdmin(admin.ModelAdmin):
    model = Act
    list_display = ('name', 'category', 'builds_confidence', 'image')


class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    list_display = ('id', 'participant', 'scheduled_at')


class ScheduleActAdmin(admin.ModelAdmin):
    model = ScheduleAct
    list_display = ('schedule', 'act', 'created_at')


# Register your models here.
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(ScheduleAct, ScheduleActAdmin)
admin.site.register(ActionCategory)
admin.site.register(Act, ActAdmin)
