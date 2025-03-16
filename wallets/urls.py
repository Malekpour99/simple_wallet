from django.urls import path

from .views import WalletUpdateAPIView

urlpatterns = [
    path(
        "balance/",
        WalletUpdateAPIView.as_view(),
        name="update-balance",
    )
]
