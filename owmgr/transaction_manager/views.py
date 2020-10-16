from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .forms import *


# Create your views here.

def index(request):
    form = TransactionForm()
    transactions = Transaction.objects.all()

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'transactions': transactions, 'form': form}
    return render(request, 'list.html', context=context)


def new_transaction(request):
    form = TransactionForm()

    context = {'form': form}
    return render(request, 'form.html', context=context)
