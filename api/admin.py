from django.contrib import admin
from api.models import *


class KeyMgmtSearch(admin.ModelAdmin):
    search_fields = ["public_key", "head_office", "number", "email", "system_id"]


admin.site.register(RewardPointSystem)
admin.site.register(DiscountPointSystem)
admin.site.register(CustomerDetails)
admin.site.register(KeyManagement, KeyMgmtSearch)
