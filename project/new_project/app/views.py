from django.shortcuts import render
from app.models import Rabotnichki

def index_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html', context = {'workers_data' : Rabotnichki.objects.all()})
