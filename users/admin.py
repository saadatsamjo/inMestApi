from django.contrib import admin
from .models import *
from .serializers import *


admin.site.register(IMUser, UserSerializer)
admin.site.register(Cohort, CohortSerializer)
admin.site.register(CohortMember, CohortMemberSerializer)
