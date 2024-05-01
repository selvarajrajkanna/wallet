from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer
from django.db import transaction

@api_view(['POST'])
def create_wallet(request):
    serializer = WalletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def credit_money(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        wallet_id = serializer.validated_data['wallet']
        amount = serializer.validated_data['amount']
        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(id=wallet_id)
            wallet.balance += amount
            wallet.save()
            serializer.save(transaction_type='Credit')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def debit_money(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        wallet_id = serializer.validated_data['wallet']
        amount = serializer.validated_data['amount']
        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(id=wallet_id)
            if wallet.balance >= amount + wallet.minimum_balance:
                wallet.balance -= amount
                wallet.save()
                serializer.save(transaction_type='Debit')
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_balance(request, user_id):
    try:
        wallet = Wallet.objects.get(user_id=user_id)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
    except Wallet.DoesNotExist:
        return Response({'error': 'Wallet does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_transaction_history(request, wallet_id, start_date, end_date):
    transactions = Transaction.objects.filter(wallet_id=wallet_id, timestamp__range=[start_date, end_date])
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)
