from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def Home(request):
    if request.user.is_authenticated:
        return render(request, 'Home.html',{"auth":True})
    else:
        return render(request, 'Home.html',{"auth":False})

def Filelist(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'Filelist.html')
        else:
            return redirect('/Login/')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')
    
def Report(request,taskID):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'Report.html')
        else:
            return redirect('/Login/')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def YaraEditor(request,taskID):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'YaraEditor.html')
        else:
            return redirect('/Login/')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def ProfileEditor(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'ProfileEditor.html')
        else:
            return redirect('/Login/')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def Login(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'Login.html')
        else:
            return redirect('/Filelist/')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def Signup(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'Signup.html')
        else:
            return redirect('/Filelist/')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def Logout(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'Logout.html')
        else:
            return redirect('/Home/')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def DeleteAccount(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'DeleteAccount.html')
        else:
            return redirect('/Login/')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html',{"auth":True})
    else:
        return render(request, 'about.html',{"auth":False})
