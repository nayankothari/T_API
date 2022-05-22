from django.contrib import admin
from api.models import *


class KeyMgmtSearch(admin.ModelAdmin):
    search_fields = ["public_key", "head_office", "number", "email", "system_id"]
    readonly_fields = ["created"]

class RewardPoint(admin.ModelAdmin):
    readonly_fields = ["created", "updated_date"]

class DiscountPoint(admin.ModelAdmin):
    readonly_fields = ["created", "updated_date"]

class CustomerDetail(admin.ModelAdmin):
    readonly_fields = ["created", "updated_date"]

admin.site.register(RewardPointSystem, RewardPoint)
admin.site.register(DiscountPointSystem, DiscountPoint)
admin.site.register(CustomerDetails, CustomerDetail)
admin.site.register(KeyManagement, KeyMgmtSearch)
