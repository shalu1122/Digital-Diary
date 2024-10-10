from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class Contact(models.Model):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    dob = models.DateField(blank=True, null=True)
    qualification = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    other_field = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
