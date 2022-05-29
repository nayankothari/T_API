from django.urls import path
from api import views
from django.contrib import admin

admin.site.site_header = "Twin Book"
admin.site.index_title = "Features"
admin.site.site_title = "Twin Book"


urlpatterns = [
    path('reward_data_detail', views.RewardDetail.as_view(), name="particular_reward_detail"),
    path('save_reward', views.SaveRewardDetail.as_view(), name="save_reward"),
    path('save_discount_reward_data', views.SaveDiscountDetail.as_view(), name="discount_detail"),
    path('get_reward_status', views.RewardStatusView.as_view(), name="status_detail"),
    path("get_reward_transaction_history", views.CustomerRewardTransactions.as_view(), name="transaction"),
    path("get_reward_transaction_history_by_card", views.CustomerRewardTransactionsByCard.as_view(), name="transaction"),
    path('reward_status_for_office_card', views.RewardStatusForOfficeAndCard.as_view(), name="office_card_reward_status"),
    path('update_reward_details', views.UpdateRewardDetail.as_view(), name="update_reward_details"),
    path('update_discount_details', views.UpdateDiscountDetail.as_view(), name="update_discount_details"),
    path('save_customer_details', views.CustomerDetailAPI.as_view(), name="customer_details"),
    path('customer_details_update', views.CustomerDetailUpdate.as_view(), name="update_customer_details"),
    path('get_customer_details_office_mobile', views.CustomerDetail_Office_Mobile.as_view(), name="customer_office_mobile"),
    path('get_customer_details_office_card', views.CustomerDetail_Office_Card.as_view(), name="customer_office_card"),
    path('get_customer_details_office_mobile_card', views.CustomerDetail_Office_Mobile_Card.as_view(),
         name="customer_office_mobile_card"),
    path('r_ins', views.KeyInstallation.as_view(), name="r_ins"),
    path('r_sta', views.Activation_detail.as_view(), name="r_sta"),
    path('available_packages', views.PaclageInstaller.as_view(), name="Available packages"),
]


