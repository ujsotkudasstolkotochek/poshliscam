from django.shortcuts import render, redirect
from .models import Bin
from .forms import BinForm

def index_page(request):
    return render(request, 'index.html')

def create_page(request):
    form = BinForm()
    if request.method == 'POST':
        form = BimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bin_page')
    return render(request, 'create.html', context = {'form' : form})

def bin_page(request, pk):
    return render(request, 'bin_page', context = {'bin_data' : Bin.objects.get(id = pk)})
