from django.contrib import admin
from .models import ClassSchedule, ClassAttendance, Query, QueryComment

admin.site.register(ClassSchedule)
admin.site.register(ClassAttendance)
admin.site.register(Query)
admin.site.register(QueryComment)
