from django.shortcuts import render
from portfolio.models import User


def index(request):
    return render(request, 'portfolio_app/index.html')