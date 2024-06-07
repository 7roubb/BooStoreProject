
# Create your views here.


from django.shortcuts import render ,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
 
def home(request):

    person = Customer.objects.all()
    order = Order.objects.all()
    book = Book.objects.all()
    in_order = Order.objects.filter(status='IN ORDER').count()
    delivered = Order.objects.filter(status='DELIVERED').count()
    cancelled = Order.objects.filter(status='CANCELLED').count()
    returned = Order.objects.filter(status='RETURNED').count()
    pending = Order.objects.filter(status='PENDING').count()
    delivering = Order.objects.filter(status='DELIVERING').count()
    context = {'persons':person 
               , 'book':book ,
                'order':order,
                'in_order':in_order,
                'delivered':delivered,
                'cancelled':cancelled,
                'returned':returned,
                'pending':pending,
                'delivering':delivering}

    return render(request,'dashbored.html',context)



def customer(request,pk):
    person = Customer.objects.get(id=pk)
    orders = person.order_set.all()
    return render(request,'customer.html' ,{'persons':person,'orders':orders})

def book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')
    
    books= Book.objects.all()
    context = {'books':books}

    return render(request,'book.html',context)

def create(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'OrderForm.html',context)

def update(request,pk): 
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance= order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'OrderForm.html',context)

def delete_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'dashbored.html', context)



def delete_book(request,pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST' :
        book.delete()
        return redirect('/books')
    context = {'book':book}
    return render(request,'book.html',context)