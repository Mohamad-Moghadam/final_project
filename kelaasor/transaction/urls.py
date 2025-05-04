from django.urls import path
from transaction.views import Deposite, AproveTransaction

urlpatterns = [
    path('deposite', Deposite.as_view()),
    path('approve-transaction/<int:pk>', AproveTransaction.as_view()),
]
