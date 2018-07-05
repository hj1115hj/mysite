from django.shortcuts import render

# Create your views here.
from django.db.models import Count
from django.shortcuts import render
from guestbook.models import Guestbook
from django.http import HttpResponseRedirect

# Create your views here.

def list(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')

    context = {'guestbook_list': guestbook_list}

    return render(request, 'guestbook/list.html',context)

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')

def deleteform(request):
    id= request.GET.get('id','')
    #print("id =======%s" %(id))
    context = {'id': id}
    return render(request,'guestbook/deleteform.html',context)

def delete(request):
    id =request.POST['id']
    password = request.POST['password']
    #print("id =======%s" % (id))
    result=Guestbook.objects.filter(id=id).filter(password = password).all().order_by('-regdate')
    cnt=result.count()
    if cnt !=0:
        Guestbook.objects.filter(id=id).filter(password=password).delete()

    return HttpResponseRedirect('/guestbook')