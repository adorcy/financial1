from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Customer
from .models import Stock
from .models import Cryptocurrency
from .forms import CustomerForm
from .forms import StockForm
from .forms import CryptocurrencyForm
from django.shortcuts import redirect

def customer_list(request):
    customers = Customer.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'financial/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    stocks = Stock.objects.filter(created__lte=timezone.now()).order_by('date_purchased')
    cryptocurrencies = Cryptocurrency.objects.filter(created__lte=timezone.now()).order_by('date_purchased')
    return render(request, 'financial/customer_detail.html', {'customer': customer, 'stocks': stocks,  'cryptocurrencies': cryptocurrencies},)

def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'financial/stock_detail.html', {'stock': stock})

def cryptocurrency_detail(request, pk):
    cryptocurrency = get_object_or_404(Cryptocurrency, pk=pk)
    return render(request, 'financial/cryptocurrency_detail.html', {'cryptocurrency': cryptocurrency})

def customer_new(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created = timezone.now()
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'financial/customer_edit.html', {'form': form})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.modified = timezone.now()
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'financial/customer_edit.html', {'form': form})

def stock_new(request):
    form = StockForm()
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created = timezone.now()
            stock.date_purchased = timezone.now()
            stock.save()
            return redirect('stock_detail', pk=stock.pk)
    else:
        form = StockForm()
    return render(request, 'financial/stock_edit.html', {'form': form})

def cryptocurrency_new(request):
    form = CryptocurrencyForm()
    if request.method == "POST":
        form = CryptocurrencyForm(request.POST)
        if form.is_valid():
            cryptocurrency = form.save(commit=False)
            cryptocurrency.created = timezone.now()
            cryptocurrency.date_purchased = timezone.now()
            cryptocurrency.save()
            return redirect('cryptocurrency_detail', pk=cryptocurrency.pk)
    else:
        form = CryptocurrencyForm()
    return render(request, 'financial/cryptocurrency_edit.html', {'form': form})

def stock_edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.modified = timezone.now()
            stock.save()
            return redirect('stock_detail', pk=stock.pk)
    else:
        form = StockForm(instance=stock)
    return render(request, 'financial/stock_edit.html', {'form': form})

def cryptocurrency_edit(request, pk):
    cryptocurrency = get_object_or_404(Cryptocurrency, pk=pk)
    if request.method == "POST":
        form = CryptocurrencyForm(request.POST, instance=cryptocurrency)
        if form.is_valid():
            cryptocurrency = form.save(commit=False)
            cryptocurrency.modified = timezone.now()
            cryptocurrency.save()
            return redirect('cryptocurrency_detail', pk=cryptocurrency.pk)
    else:
        form = CryptocurrencyForm(instance=cryptocurrency)
    return render(request, 'financial/cryptocurrency_edit.html', {'form': form})


