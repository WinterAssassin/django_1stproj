from django.http import HttpResponse
from django.shortcuts import render
from .models import Members
# Create your views here.

def index(request):
    mymembers = Members.objects.all().values()
    context = {'mymembers': mymembers}
    return render(request, 'members/index.html', context=context)