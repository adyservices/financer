from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from.models import Payments,Transactions
from.serializers import PaymentsSerializer,TransactionsSerializer

# Perform CRUD operations for Payments
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated,])
def payments_operations(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        event_id = request.GET.get('event')
        if id is not None:
            try:
                payments_data = Payments.objects.get(Q(id=id)&Q(active=True))
                serializer = PaymentsSerializer(payments_data)
                return Response(serializer.data)
            except Payments.DoesNotExist:
                return Response("Data not found",status=status.HTTP_404_NOT_FOUND)
        elif event_id is not None:
            try:
                payments_data = Payments.objects.filter(Q(event_id=event_id)&Q(active=True))
                serializer = PaymentsSerializer(payments_data,many=True)
                return Response(serializer.data)
            except Payments.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = PaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        payments = Payments.objects.get(id=request.data['id'])
        serializer = PaymentsSerializer(payments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        id = request.GET.get('id')
        try:
            payments_data = Payments.objects.get(id=id)
            payments_data.active = False
            payments_data.save()
            return Response("bill removed",status=status.HTTP_200_OK)
        except Payments.DoesNotExist:
            return Response("Some thing went wrong contact admin",status=status.HTTP_404_NOT_FOUND)

# Perform CRUD operations for Transactions
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated,])
def transactions_operations(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        payment_id = request.GET.get('payment_id')
        if id is not None:
            try:
                transactions_data = Transactions.objects.get(Q(id=id)&Q(active=True))
                serializer = TransactionsSerializer(transactions_data)
                return Response(serializer.data)
            except Transactions.DoesNotExist:
                return Response("Data not found",status=status.HTTP_404_NOT_FOUND)
        elif payment_id is not None:
            try:
                transactions_data = Transactions.objects.filter(Q(payment_id=payment_id)&Q(active=True))
                serializer = TransactionsSerializer(transactions_data,many=True)
                return Response(serializer.data)
            except Transactions.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = TransactionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = request.data.get('id')
        transactions_data = Transactions.objects.get(Q(id=id)&Q(active=True))
        serializer = TransactionsSerializer(transactions_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        id = request.GET.get('id')
        try:
            transactions_data = Transactions.objects.get(Q(id=id)&Q(active=True))
            transactions_data.active = False
            transactions_data.save()
            return Response("bill removed",status=status.HTTP_200_OK)
        except Transactions.DoesNotExist:
            return Response("Some thing went wrong contact admin",status=status.HTTP_404_NOT_FOUND)


