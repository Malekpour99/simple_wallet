from django.db import models

from accounts.models import User


class Wallet(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="wallets",
    )
    balance = models.DecimalField(
        default=0,
        max_digits=16,
        decimal_places=8,
    )
