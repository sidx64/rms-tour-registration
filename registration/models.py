from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class RMSIndia2019(models.Model):
    fname = models.CharField(max_length=255, blank=False, null=False)
    lname = models.CharField(max_length=255, blank=False, null=False)
    email_id = models.EmailField(max_length=255, blank=False, null=False)
    mobile_number = models.CharField(max_length=255, blank=False, null=False)
    designation = models.CharField(max_length=255, blank=False, null=False)
    organization = models.CharField(max_length=255, blank=False, null=False)
    is_student = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=255, blank=False, null=True)
    is_verified = models.BooleanField(default=False)
    verification_time = models.DateTimeField(blank=True, null=True)
    request_datetime = models.DateTimeField(auto_now_add=True , blank=True)
    modified_datetime = models.DateTimeField(auto_now=True , blank=True)



