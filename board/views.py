from django.shortcuts import render
from django.http import HttpResponseRedirect
from board.models import Board
from board.models import User
from django.shortcuts import redirect
# Create your views here.


# def writeform(request):
#     #인증체크
#     if request.session['authouser'] is None :
#         return HttpResponseRedirect('/로그인폼/')

def list(request):
    board_list = Board.objects.all().order_by('-regdate')

    content = {'board_list': board_list}

    return render(request, 'board/list.html',content)


def writeform(request):
     #인증체크
    try:
        if request.session['authuser'] is not None:
            return render(request,'board/write.html')
    except:
        return HttpResponseRedirect('/user/loginform')

def insert(request):
    board = Board()
    id = request.POST['user_id']
    result=User.objects.filter(id=id)
    board.user = result[0]
    board.title = request.POST['title']
    board.content = request.POST['content']


    board.save()

    return HttpResponseRedirect('/board/')

def delete(request):
    # temp =request.GET['user_id']

    # user_id = request.session['authuser']['id']
    id =request.GET['id']
    Board.objects.filter(id=id).delete()

    return HttpResponseRedirect('/board/')

def view(request):
    id=request.GET['id']
    board=Board.objects.filter(id=id)
    content = {'board': board[0]}
    return render(request,'board/view.html',content)


def modifyform(request):
    id = request.GET['id']
    board = Board.objects.filter(id=id)
    content = {'board' : board[0]}
    return render(request, 'board/modifyform.html', content)

def modify(request):
    id = request.POST['id']
    board = Board.objects.get(id=id)
    board.title = request.POST['title']
    board.content = request.POST['content']

    board.save()
    return HttpResponseRedirect('/board/view?id='+id)
