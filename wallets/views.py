from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Wallet
from .serializers import WalletSerializer


class WalletUpdateAPIView(APIView):
    def post(self, request, *args, **kwargs):

        serializer = WalletSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    wallet = serializer.save()

                return Response(
                    {
                        "user_id": wallet.user.id,
                        "new_balance": str(wallet.balance),
                    },
                    status=status.HTTP_200_OK,
                )

            except Wallet.DoesNotExist:
                return Response(
                    {"error": "Wallet not found for this user"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            except Exception as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
