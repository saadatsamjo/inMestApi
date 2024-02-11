# users/models.py

from django.db import models

class IMUser(models.Model):
    EIT = 'EIT'
    TEACHING_FELLOW = 'TEACHING_FELLOW'
    ADMIN_STAFF = 'ADMIN_STAFF'
    ADMIN = 'ADMIN'
    USER_TYPE_CHOICES = [
        (EIT, 'EIT'),
        (TEACHING_FELLOW, 'Teaching Fellow'),
        (ADMIN_STAFF, 'Admin Staff'),
        (ADMIN, 'Admin'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=EIT)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Cohort(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_member')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohort_member')

    def __str__(self):
        return f'{self.member} - {self.cohort}'

