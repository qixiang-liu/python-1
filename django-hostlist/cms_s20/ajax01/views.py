from django.shortcuts import render,HttpResponse,redirect
from .models import *
import json
# Create your views here.


def demo(request):
    return render(request,'demo.html',locals())

def index(request):
    #获取cookies,如果没有那么就跳到login界面
    ret=request.COOKIES.get('is_login')
    if not ret:
        return redirect('/ajax01/login/')
    user=request.COOKIES.get('user')
    return render(request, 'index.html', locals())

def ajax_send(request):
    return HttpResponse('ajax_20')

def user_valid(request):
    if request.method=="GET":
        name=request.GET.get('name')
    if request.method=="POST":
        name = request.POST.get('name2')
    ret=ajax_User.objects.filter(name=name).first()
    print(ret)
    res={'state':True,'msg':''}
    if ret:
        res['state']=False
        res['msg']="用户已经存在"
    return HttpResponse(json.dumps(res))

def login(request):
    if request.method=="POST":
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        ret=ajax_UserInfo.objects.filter(user=user,pwd=pwd).first()
        if ret:
            #设置cookie：
            obj=HttpResponse('登录成功')
            obj.set_cookie('is_login','2312true')
            obj.set_cookie('user',user)
            return obj
            # return redirect('/ajax01/index/')
            # return HttpResponse('登录成功')
    return render(request,'login.html',locals())