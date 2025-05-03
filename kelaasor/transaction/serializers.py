from rest_framework.serializers import ModelSerializer
from transaction.models import Wallet, Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model= Transaction
        fields= '__all__'


class WalletSerializer(ModelSerializer):
    class Meta:
        model= Wallet
        fields= '__all__'