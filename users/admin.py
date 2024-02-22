# users/admin.py
from django.contrib import admin
from .models import *
from .serializers import *


admin.site.register(IMUser)
admin.site.register(Cohort)
admin.site.register(CohortMember)
