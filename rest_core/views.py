from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from rest_core.models import Task
import requests#cuz we need to send req to cukcoo api
import clamd#clamav api
import yara#yara tools
import os#for deleting files

def CreateTask(request):#finished
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                file = {"file": ("temp_file_name", request.FILES['file'])}
                HEADERS = {"Authorization": "Bearer 41R9M2urGhpWhWU8Ly6TWw"}
                r = requests.post("http://192.168.227.128:8090/tasks/create/file", headers=HEADERS, files=file)
                json = r.json()
                task = Task.objects.create(taskID = int(json['task_id']),owner = request.user,file = request.FILES['file'])
                cd = clamd.ClamdNetworkSocket()
                scan = cd.scan(task.file.path)
                if scan[task.file.path][0] == 'OK':
                    task.detection = "Not Detected"
                elif scan[task.file.path][0] == 'FOUND':
                    task.detection = "Detected"
                else:
                    task.detection = scan[task.file.path][0]
                task.save()
                return HttpResponse(status=200,content='OK')
            except Exception as e:
                return HttpResponse(status=400,content=e)
        else:
            return HttpResponse(status=401,content='You should Login')
    else:
        return HttpResponse(status=400,content='You should make a POST request.')

def Report(request,taskID):#finished
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                task = Task.objects.get(taskID = taskID)
                if task.owner == request.user:
                    HEADERS = {"Authorization": "Bearer 41R9M2urGhpWhWU8Ly6TWw"}
                    r = requests.get("http://192.168.227.128:8090/tasks/report/"+str(taskID), headers=HEADERS)
                    json = r.json()
                    return JsonResponse(json , safe=True)
                else:
                    return HttpResponse(status=400,content='Access deny')
            except Exception as e:
                return HttpResponse(status=400,content=e)
        else:
            return HttpResponse(status=401,content='You should Login')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def Status(request,taskID):#finished
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                task = Task.objects.get(taskID = taskID)
                if task.owner == request.user:
                    HEADERS = {"Authorization": "Bearer 41R9M2urGhpWhWU8Ly6TWw"}
                    r = requests.get("http://192.168.227.128:8090/tasks/view/"+str(taskID), headers=HEADERS)
                    json = r.json()
                    return JsonResponse(json , safe=True)
                else:
                    return HttpResponse(status=400,content='Access deny')
            except Exception as e:
                return HttpResponse(status=400,content=e)
        else:
            return HttpResponse(status=401,content='You should Login')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def Delete(request,taskID):#finished
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                task = Task.objects.get(taskID = taskID)
                if task.owner == request.user:
                    if os.path.exists(task.file.path):
                        os.remove(task.file.path)
                    task.delete()
                    HEADERS = {"Authorization": "Bearer 41R9M2urGhpWhWU8Ly6TWw"}
                    r = requests.get("http://192.168.227.128:8090/tasks/delete/"+str(taskID), headers=HEADERS)
                    return HttpResponse(status=200,content='OK')
                else:
                    return HttpResponse(status=400,content='Access deny')
            except Exception as e:
                return HttpResponse(status=400,content=e)
        else:
            return HttpResponse(status=401,content='You should Login')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def Login(request):#finished
    if request.method == 'POST':
        if not request.user.is_authenticated:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse(status=200,content='OK')
            else:
                return HttpResponse(status=401,content='Username or Password is wrong')
        else:
            return HttpResponse(status=401,content='Probably you are logged in.')
    else:
        return HttpResponse(status=400,content='You should make a POST request.')

def Logout(request):#finished
    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
            return HttpResponse(status=200,content='OK')
        else:
            return HttpResponse(status=401,content='you not logged in')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def Signup(request):#finished
    if request.method == 'POST':
        if not request.user.is_authenticated:
            if(request.POST['password']==request.POST['confirm_password']):
                try:
                    User.objects.get(username = request.POST['username'])
                    return HttpResponse(status=401,content='username exist try another')
                except:
                    user = User.objects.create_user(request.POST['username'] , request.POST['email'] , request.POST['password'])
                    user.first_name = request.POST['firstname']
                    user.last_name = request.POST['lastname']
                    user.save()
                    
                    username = request.POST['username']
                    password = request.POST['password']
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return HttpResponse(status=200,content='OK')
                    else:
                        return HttpResponse(status=401,content='Username or Password is wrong')
            else:
                return HttpResponse(status=401,content='Password most equal to Confirm Password')
        else:
            return HttpResponse(status=401,content='Probably you are logged in with your account.')
    else:
        return HttpResponse(status=400,content='You should make a POST request.')

def DeleteAccount(request):#finished
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                for item in Task.objects.filter(owner = request.user):
                    if os.path.exists(item.file.path):
                        os.remove(item.file.path)
                    HEADERS = {"Authorization": "Bearer 41R9M2urGhpWhWU8Ly6TWw"}
                    r = requests.get("http://192.168.227.128:8090/tasks/delete/"+str(item.taskID), headers=HEADERS)
                    item.delete()
                request.user.delete()
                logout(request)
                return HttpResponse(status=200,content='OK')
            except Exception as e:
                return HttpResponse(status=400,content=e)
        else:
            return HttpResponse(status=401,content='You did not logged in')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def PasswordChange(request):#finished
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.check_password(request.POST['password']):
                if request.POST['new_password'] == request.POST['confirm_password'] and request.POST['new_password'] != '' and request.POST['confirm_password'] != '':
                    request.user.set_password(request.POST['new_password'])
                    request.user.save()
                    return HttpResponse(status=200,content='OK')
                elif request.POST['new_password'] != request.POST['confirm_password'] and request.POST['new_password'] != '' and request.POST['confirm_password'] != '':
                    return HttpResponse(status=400,content='New Password field most be equal to confirm password field.')
                else:
                    return HttpResponse(status=400,content='Field(s) is Null')
            else:
                return HttpResponse(status=401,content='Password is wrong')
        else:
            return HttpResponse(status=401,content='You should Login')
    else:
        return HttpResponse(status=400,content='You should make a POST request.')


def EmailChange(request):#finished
    if request.method == 'POST':
        if request.user.is_authenticated:
            request.user.email = request.POST['email']
            request.user.save()
            return HttpResponse(status=200,content='OK')
        else:
            return HttpResponse(status=401,content='You should Login')
    else:
        return HttpResponse(status=400,content='You should make a POST request.')

def getProfile(request):#finished
    if request.method == 'GET':
        if request.user.is_authenticated:
            data = {'username':request.user.username,'email':request.user.email}
            return JsonResponse(data , safe=True)
        else:
            return HttpResponse(status=401,content='You should Login')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def getFilelist(request):#finished
    if request.method == 'GET':
        if request.user.is_authenticated:
            data = {'items':[]}
            for item in Task.objects.filter(owner = request.user):
                HEADERS = {"Authorization": "Bearer 41R9M2urGhpWhWU8Ly6TWw"}
                r = requests.get("http://192.168.227.128:8090/tasks/view/"+str(item.taskID), headers=HEADERS)
                json = r.json()
                temp = {'task_id':str(item.taskID),'name':item.file.name,'size':str(item.file.size),'detection':item.detection,'status':json['task']['status']}
                data['items'].append(temp)
            return JsonResponse(data , safe=True)
        else:
            return HttpResponse(status=401,content='You should Login')
    else:
        return HttpResponse(status=400,content='You should make a GET request.')

def YaraMatch(request,taskID):#finished
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                task = Task.objects.get(taskID = taskID)
                if task.owner == request.user:
                    rules = yara.compile(source = request.POST['YaraEditor'])
                    match = rules.match(task.file.path)
                    return JsonResponse({'resualt':match} , safe=True)
                else:
                    return HttpResponse(status=400,content='Access deny')
            except Exception as e:
                return HttpResponse(status=400,content=e)
        else:
            return HttpResponse(status=401,content='You should Login')
    else:
        return HttpResponse(status=400,content='You should make a POST request.')
