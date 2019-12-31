# dappx/admin.py
from django.contrib import admin
from dappx.models import UserProfileInfo, User,SubmissionForm
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(SubmissionForm)