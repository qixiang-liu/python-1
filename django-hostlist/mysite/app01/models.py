from django.db import models

# Create your models here.

#主机管理系统

class Host(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64)
    ip=models.GenericIPAddressField(unique=True) #不能重复
    memo=models.CharField(max_length=128,null=True)  #表示可以为空

    #外键关联的字段在数据库中创建字段时会自动添加一个id
    group = models.ForeignKey(to="HostGroup")  # 通过外键和hostgroup关联
    #通过管理的外键能直接找到关联的对象   主机对象->关联对象

#业务线
class HostGroup(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)

