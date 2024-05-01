from django.urls import path
from wallet import views

urlpatterns = [
    path('create_wallet/', views.create_wallet, name='create_wallet'),
    path('credit_money/', views.credit_money, name='credit_money'),
    path('debit_money/', views.debit_money, name='debit_money'),
    path('get_balance/<int:user_id>/', views.get_balance, name='get_balance'),
    path('get_transaction_history/<int:wallet_id>/<str:start_date>/<str:end_date>/', views.get_transaction_history, name='get_transaction_history'),
]
