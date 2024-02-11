from django.contrib import admin
from .models import IMUser, Cohort, CohortMember

admin.site.register(IMUser)
admin.site.register(Cohort)
admin.site.register(CohortMember)


