from django.shortcuts import render
from datetime import datetime

def home(request):
    context = {
        'names': 'aime',
        'age': 25,
        'date':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    return render(request, 'home.html', context)
