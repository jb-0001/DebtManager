from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newtransaction/', views.new_transaction, name='transaction form')
]
