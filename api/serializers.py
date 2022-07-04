from rest_framework import serializers
from api.models import RewardPointSystem, DiscountPointSystem, CustomerDetails, KeyManagement, Ftp
from api.models import Packages


class RPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardPointSystem
        fields = ['office', 'branch', 'office_branch',
                  'bill_number', 'mobile_number', 'customer',
                  'card_number', 'bill_amount', 'points']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class DPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountPointSystem
        fields = ['office', 'branch', 'office_branch',
                  'bill_number', 'mobile_number', 'customer',
                  'card_number', 'bill_amount', 'points']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = ['uid', 'office','branch', 'office_branch',
                  'customer_name', 'number', 'alt_number', 'email',
                  'card_number', 'date_for_BA', 'birt_anny',
                  'gender', 'address']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class RPSSerializerTxn(serializers.ModelSerializer):
    class Meta:
        model = RewardPointSystem
        fields = ['office', 'branch', 'office_branch',
                  'bill_number', 'mobile_number', 'customer',
                  'card_number', 'bill_amount', 'points', 'created']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class DPSSerializerTxn(serializers.ModelSerializer):
    class Meta:
        model = DiscountPointSystem
        fields = ['office', 'branch', 'office_branch',
                  'bill_number', 'mobile_number', 'customer',
                  'card_number', 'bill_amount', 'points', 'created']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class KeyManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyManagement
        fields = ["valid_for_days", "rps", "cloud", "backup", "customer_name",
                "shop_name", "head_office", "branch", "passkey", "email", "number", "key_status", "activated_date",
                "system_id", "access_token", "drive_folder", "local_path"]
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ["type", "basic_price", "final_price", "link"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class FtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ftp
        fields = ["access_token", "drive_folder", "local_path", "port", "path"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
