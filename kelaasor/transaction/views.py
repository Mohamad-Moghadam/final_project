from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from transaction.models import Wallet, Transaction
from transaction.serializers import TransactionSerializer
from django.db.models import F

class Deposite(CreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset= Transaction.objects.all()
    serializer_class= TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        Wallet.objects.filter(user=self.request.user).update(
            balance=F('balance') + serializer.validated_data['amount']
        )