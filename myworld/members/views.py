from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Members
# Create your views here.

def index(request):
    mymembers = Members.objects.all().values()
    context = {'mymembers': mymembers}
    return render(request, 'members/index.html', context=context)

def add(request):
    return render(request, 'members/add.html')

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return redirect('index')

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect('index')

def update(request, id):
    mymember = Members.objects.get(id=id)
    context = {
        'mymember': mymember,
    }
    return render(request, 'members/update.html', context=context)

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return redirect('index')