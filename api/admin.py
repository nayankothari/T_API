from django.contrib import admin
from api.models import *


class KeyMgmtSearch(admin.ModelAdmin):
    search_fields = ["public_key", "head_office", "number", "email", "system_id"]
    readonly_fields = ["created"]
    list_filter = ["public_key", "number", "system_id"]
        
class RewardPoint(admin.ModelAdmin):
    readonly_fields = ["created", "updated_date"]
    list_filter = ["office", "branch"]
    search_fields = ["office", "branch"]

class DiscountPoint(admin.ModelAdmin):
    readonly_fields = ["created", "updated_date"]
    list_filter = ["office", "branch"]
    search_fields = ["office", "branch"]
    
class CustomerDetail(admin.ModelAdmin):
    readonly_fields = ["created", "updated_date"]
    list_filter = ["office", "branch", "number"]
    search_fields = ["office", "branch", "number"]

admin.site.register(RewardPointSystem, RewardPoint)
admin.site.register(DiscountPointSystem, DiscountPoint)
admin.site.register(CustomerDetails, CustomerDetail)
admin.site.register(KeyManagement, KeyMgmtSearch)
