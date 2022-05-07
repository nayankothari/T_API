from django.db import models
from datetime import datetime
from django.utils import timezone


class RewardPointSystem(models.Model):
    office = models.CharField(max_length=256, blank=False)
    branch = models.CharField(max_length=256, blank=False)
    office_branch = models.CharField(max_length=256,
                                     blank=True)
    bill_number = models.CharField(max_length=256,
                                     blank=True)
    created = models.DateTimeField(auto_now_add=True,
                                   blank=True)
    updated_date = models.DateTimeField(blank=False,
                                        default=timezone.now())
    mobile_number = models.BigIntegerField(blank=True)
    customer = models.CharField(max_length=256, blank=True)
    card_number = models.CharField(max_length=256, blank=True)
    bill_amount = models.FloatField(blank=True)
    points = models.FloatField(blank=True)

    def __str__(self):
        return (str(self.office) + "_" + str(self.mobile_number))

class DiscountPointSystem(models.Model):
    office = models.CharField(max_length=256, blank=False)
    branch = models.CharField(max_length=256, blank=False)
    office_branch = models.CharField(max_length=256,
                                     blank=True)
    bill_number = models.CharField(max_length=256,
                                     blank=True)
    created = models.DateTimeField(auto_now_add=True,
                                   blank=True)
    updated_date = models.DateTimeField(blank=False,
                                        default=timezone.now())
    mobile_number = models.BigIntegerField(blank=True)
    customer = models.CharField(max_length=256, blank=True)
    card_number = models.CharField(max_length=256, blank=True)
    bill_amount = models.FloatField(blank=True)
    points = models.FloatField(blank=True)

    def __str__(self):
        return (str(self.office) + "_" + str(self.mobile_number))



class CustomerDetails(models.Model):
    uid = models.CharField(max_length=300, blank=False, unique=True) # it is the combination of ( office+"_"+Mob+"_"+card number )
    office = models.CharField(max_length=256, blank=False)
    branch = models.CharField(max_length=256, blank=False)
    office_branch = models.CharField(max_length=256,
                                     blank=True)
    created = models.DateTimeField(auto_now_add=True,
                                   blank=True)
    updated_date = models.DateTimeField(blank=False,
                                        default=timezone.now())
    customer_name = models.CharField(max_length=256, blank=True)
    number = models.BigIntegerField(blank=False)
    alt_number = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=200, blank=True)
    card_number = models.CharField(max_length=256, blank=False)
    date_for_BA = models.CharField(max_length=15, blank=True)
    birt_anny = models.IntegerField(blank=False)
    gender = models.IntegerField(blank=False)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.uid

class KeyManagement(models.Model):
    pass