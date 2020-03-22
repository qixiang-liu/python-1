from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from . import models

def host_list(request):
    #去数据库中取出全部主机，展示到页面
    host_list=models.Host.objects.all()
    return render(request,"host_list.html",{"host_list":host_list})


def add_host(request):
    if request.method == "POST":
        hostname=request.POST.get("host_name")
        ip=request.POST.get("ip")
        memo=request.POST.get("memo")
        group=request.POST.get("group")

        models.Host.objects.create(name=hostname,ip=ip,memo=memo,group_id=group)
        return redirect("/host_list/")
    #去数据库中把所有的主机组查找出来
    group_list=models.HostGroup.objects.all()
    return render(request,"add_host.html",{"group_list":group_list})

def edit_host(request):
    if request.method == "POST":
        host_id=request.POST.get("host_id")
        obj=models.Host.objects.get(id=host_id)
        obj.name=request.POST.get("host_name")
        obj.memo=request.POST.get("host_memo")
        obj.ip=request.POST.get("host_ip")
        obj.group_id=request.POST.get("host_group")
        obj.save()

        return redirect("/host_list/")
    edit_id=request.GET.get("id")
    host=models.Host.objects.get(id=edit_id)
    group_list=models.HostGroup.objects.all()
    host_list=models.Host.objects.all()
    return render(request,"edit_host.html",{"host":host,"group_list":group_list})




def delete_host(request):
    if request.method == "GET":
        host_id=request.GET.get("id")
        models.Host.objects.get(id=host_id).delete()
    return redirect("/host_list/")