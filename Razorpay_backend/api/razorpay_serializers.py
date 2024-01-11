from rest_framework import serializers
from ..models import Transaction


class CreateOrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()


class TransactionModelSerializer(serializers.Serializer):

    class Meta:
        model = Transaction
        fields = ["payment_id", "order_id", "signature", "amount"]

