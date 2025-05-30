from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from transaction.models import Wallet, Transaction
from transaction.serializers import TransactionSerializer, WalletSerializer
from django.db.models import F
from rest_framework.views import APIView
from user.permissions import IsTechnician
from django.http import HttpResponse, JsonResponse
from user.permissions import IsHeadmaster


class Deposite(CreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset= Transaction.objects.all()
    serializer_class= TransactionSerializer

    def perform_create(self, serializer):
        wallet, _ = Wallet.objects.get_or_create(user=self.request.user)
        serializer.save(wallet= wallet, status= 'pending')


class AproveTransaction(APIView):
    permission_classes= [IsTechnician]

    def post(self, request, pk):
        try:
            transaction= Transaction.objects.get(pk= pk, status= 'pending')
        except Transaction.DoesNotExist:
            return JsonResponse({'message': 'Transaction not found'}, status= 404)
        
        transaction.status= 'approved'
        transaction.save()

        Wallet.objects.filter(pk=transaction.wallet.pk).update(
            balance=F('balance') + transaction.amount
        )

        return JsonResponse({'message': 'Transaction approved'}, status= 200)

class ShowBalance(ListAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= WalletSerializer

    def get_queryset(self):
        return Wallet.objects.filter(user= self.request.user)


class LsTransactions(ListAPIView):
    permission_classes= [IsHeadmaster]
    serializer_class= TransactionSerializer
    queryset= Transaction.objects.all()