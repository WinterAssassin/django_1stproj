from django.http import HttpResponse
from django.shortcuts import render
from .models import Members
# Create your views here.

def index(request):
    mymembers = Members.objects.all().values()
    # return render(request, 'members/myfirst.html')
    output = ""
    for x in mymembers:
        output += x["firstname"]

    return HttpResponse(output)