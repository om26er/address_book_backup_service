from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=200, blank=True)
    email_home = models.EmailField(max_length=200, blank=True)
    email_work = models.EmailField(max_length=200, blank=True)
    phone_home = models.CharField(max_length=200, blank=True)
    phone_work = models.CharField(max_length=200, blank=True)
    address_home = models.CharField(max_length=500, blank=True)
    address_work = models.CharField(max_length=500, blank=True)
    date_of_birth = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=200, blank=True)
    job_title = models.CharField(max_length=200, blank=True)
