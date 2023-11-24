from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_street = models.CharField(max_length=100, null=True, blank=True)
    address_city = models.CharField(max_length=50, null=True, blank=True)
    address_state = models.CharField(max_length=50, null=True, blank=True)
    address_zip = models.CharField(max_length=10, null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=[('Parent', 'Parent'), ('Child', 'Child')])
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
