from django.shortcuts import render
from django.utils import timezone
from .models import Customer

def customer_list(request):
    customers = Customer.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'financial/customer_list.html', {'customers': customers})
