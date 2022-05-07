from rest_framework import serializers
from api.models import RewardPointSystem, DiscountPointSystem, CustomerDetails


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


