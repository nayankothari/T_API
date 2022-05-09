import uuid
import random
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

def public_key():
    random_number = random.randrange(13, 16)
    uni_id = str(uuid.uuid4().hex[:random_number]).upper()
    return uni_id


class KeyManagement(models.Model):
    public_key = models.CharField(max_length=16, unique=True, default=public_key, editable=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    days_choics = (
        ("30", "30 days"),
        ("90", '90 days'),
        ("180", '180 days'),
        ("360", '360 days'))
    valid_for_days = models.CharField(max_length=3, choices=days_choics, blank=False)
    amount_choice = (
        ("0", "Free"),
        ("499", "499/-"),
        ("1399", '1399/-'),
        ("2499", '2499/-'),
        ("3999", '3999/-'))
    amount = models.CharField(max_length=4, choices=amount_choice, blank=False, default="Free")
    rps = models.BooleanField(default=True)
    cloud = models.BooleanField(default=True)
    backup = models.BooleanField(default=True)
    customer_name = models.CharField(max_length=255, blank=True)
    shop_name = models.CharField(max_length=355, blank=True)
    email = models.CharField(max_length=80, blank=True)
    number = models.CharField(max_length=15, blank=True)
    key_status = models.IntegerField(default=0)
    activated_date = models.DateTimeField(blank=True,
                                        default=timezone.now())
    system_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return (str(self.public_key) + "_" + str(self.key_status) + "_" + str(self.valid_for_days) + "_" + str(self.amount))