from django.db import transaction
from rest_framework import serializers

from .models import Wallet
from accounts.models import User


class WalletSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(
        min_value=1,
        write_only=True,
    )
    amount = serializers.DecimalField(
        min_value=1,
        max_digits=16,
        decimal_places=8,
        write_only=True,
    )

    def validate_user_id(self, value):
        """Validate that the user exists"""
        try:
            User.objects.get(id=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        return value

    def create(self, validated_data):
        user_id = validated_data["user_id"]
        amount = validated_data["amount"]

        try:
            # Using select_for_update to lock the row and prevent race conditions
            with transaction.atomic():
                try:
                    wallet = Wallet.objects.select_for_update().get(user__id=user_id)
                except Wallet.DoesNotExist:
                    # Create wallet if it doesn't exist
                    user = User.objects.get(id=user_id)
                    wallet = Wallet(user=user)

                wallet.balance += amount
                wallet.save()

                return wallet
        except Exception as e:
            raise serializers.ValidationError(f"Failed to update wallet: {str(e)}")


# mostafababaii88@gmail.com
