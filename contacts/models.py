from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField


class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9
        
    name = models.CharField(max_length=255)
    birthday = models.DateField(max_length=8, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)
