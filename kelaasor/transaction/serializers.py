from rest_framework.serializers import ModelSerializer
from transaction.models import Wallet, Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model= Transaction
        fields= '__all__'
        read_only_fields= ['wallet']


class WalletSerializer(ModelSerializer):
    class Meta:
        model= Wallet
        fields= '__all__'