from django.urls import path
from .views import payments_operations,transactions_operations

urlpatterns = [
    path('add_payment/', payments_operations, name='add_payment'),
    path('delete_payment/', payments_operations, name='delete_payment'),
    path('edit_payment/', payments_operations, name='edit_payment'),
    path('view_payments/', payments_operations, name='view_payments'),

    path('add_transaction/', transactions_operations, name='add_transaction'),
    path('delete_transaction/', transactions_operations, name='delete_transaction'),
    path('edit_transaction/', transactions_operations, name='edit_transaction'),
    path('view_transactions/', transactions_operations, name='view_transactions'),
]