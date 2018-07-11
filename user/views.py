from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponseRedirect ,HttpResponse
# Create your views here.
from user.models import User


def joinform (request):
    return render(request, 'user/joinform.html')


def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')


def join(request):
    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    user.save()

    return HttpResponseRedirect('/user/joinsuccess')

def loginform(request):
    return render(request,'user/loginform.html')


def login(request):

    result = User.objects.filter(email = request.POST['email']).filter(password = request.POST['password'])

    #로그인 실패
    if len(result) == 0:
        return HttpResponseRedirect('/user/loginform?result=false')

    #session에다가 객체를 넣는지 안넣는지에 대한 차이
    authuser= result[0]
    request.session['authuser'] = model_to_dict(authuser)


    #  return HttpResponse(authuser)

    return HttpResponseRedirect('/')

def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')