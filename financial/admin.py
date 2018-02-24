from django.contrib import admin
from .models import Customer
from .models import Stock
from .models import Cryptocurrency

admin.site.register(Customer)
admin.site.register(Stock)
admin.site.register(Cryptocurrency)