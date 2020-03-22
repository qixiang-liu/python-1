
"""django02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import HttpResponse,render,redirect
from app01 import models

def index(request):
    #所有和请求相关的数据都封装到这个request参数中
    #return HttpResponse("This is index page!")
    return redirect("http://www.baidu.com")   #返回url跳转

def home(request):
    return render(request,"home.html")  #返回网页信息

def login(request):
    #如果是POST请求，表示页面上给我提交数据了
    error_msg=''
    if request.method =="POST":
        #我要从提交的数据中取到email和pwd
        email=request.POST.get("email2")
        pwd= request.POST.get("pwd")
        print(email,pwd)
        if email == "alex@1.com" and pwd=="alexdsb":
            #登录成功
            return redirect("http://www.baidu.com")
        else:
            error_msg="邮箱或者密码错误"
            return render(request,"login.html",{"error":error_msg})

    #相等于执行了
    # with open("login.html","rb") as f:
    #     ret=f.read()
    #     return ret
    return render(request,"login.html",{"error":error_msg})

#展示书列表的函数
def book_list(request):
    #找到所有的书
    books=models.Book.objects.all()
    return render(request,"book_list.html",{'book_list':books})

#添加新书
def add_book(request):
    #如果请求方式是post，表示前端页面添加完成正在提交新书的信息
    if request.method=="POST":
        new_book_name=request.POST.get("book_name")
        #去数据里面创建新的书
        models.Book.objects.create(title=new_book_name)
        #跳转会之前展现数据列表的页面
        return redirect("/book_list/")
    #返回一个页面让用户填写新书的相关信息
    return render(request,"add_book.html")

#删除书
def delete_class(request):
    #取到要删除的书的ID，如何从get请求中，获取数据
    delete_id=request.GET.get("id")

    #根据id值去数据库中取对应的数据
    models.Book.objects.get(id=delete_id).delete() #找到并删除
    return redirect("/book_list/")


#编辑书
def edit_book(request):
    #如果是post请求，就表名前端页面编辑完了，把新的书信息发过来
    if request.method=="POST":
        #取到正在编辑书的ID
        book_id=request.POST.get("book_id")
        #取到编辑之后的书的名字
        new_book_title=request.POST.get("book_name")
        #更新书的数据
        book_obj=models.Book.objects.get(id=book_id)
        book_obj.title=new_book_title
        book_obj.save()
        return redirect("/book_list/")
    #先取到当前编辑书的ID值
    edit_id=request.GET.get("id")
    #根据id值取出book的的名字
    book=models.Book.objects.get(id=edit_id)
    #返回一个编辑书的页面
    return render(request,"edit_book.html",{"book":book})

