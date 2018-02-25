from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Customer
from .models import Stock
from .models import Cryptocurrency


def customer_list(request):
    customers = Customer.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'financial/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    stocks = Stock.objects.filter(created__lte=timezone.now()).order_by('date_purchased')
    cryptocurrencies = Cryptocurrency.objects.filter(created__lte=timezone.now()).order_by('date_purchased')
    return render(request, 'financial/customer_detail.html', {'customer': customer, 'stocks': stocks,  'cryptocurrencies': cryptocurrencies},)

