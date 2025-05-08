from django.urls import path
from transaction.views import Deposite, AproveTransaction, ShowBalance, LsTransactions

urlpatterns = [
    path('deposite', Deposite.as_view()),
    path('approve-transaction/<int:pk>', AproveTransaction.as_view()),
    path('ls-balance', ShowBalance.as_view()),
    path('ls-transactions', LsTransactions.as_view()),
]
