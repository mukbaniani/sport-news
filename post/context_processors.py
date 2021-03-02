from .models import League
from django.shortcuts import render

def get_leagues(request):
    leagues = League.objects.all()
    data = {"leagues": leagues}
    return data