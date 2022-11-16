from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Customers


@login_required(redirect_field_name='login')
def home(request):
    customers = Customers.objects.all()
    generated_tickets = Customers.objects.filter(status=True).count()
    outstanding_tickets = Customers.objects.filter(status=False).count()
    progress = (generated_tickets/customers.count()) * 100
    
    return render(request, 'pages/home.html', {'customers':customers, 'generated_tickets':generated_tickets,
                                               'outstanding_tickets':outstanding_tickets, 'progress': f'{progress:.2f}'})
