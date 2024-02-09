from django.shortcuts import render


def portfolio(request):
    return render(request, 'portfolio/index.html')

def facturacion(request):
    return render(request, 'under_construction.html')

def whappip(request):
    return render(request, 'under_construction.html')

def wiki(request):
    return render(request, 'under_construction.html')

def marketing(request):
    return render(request, 'under_construction.html')

def landing(request):
    return render(request, 'under_construction.html')
