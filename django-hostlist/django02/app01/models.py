from django.db import models

# Create your models here.

#写上会创建一个名字叫app01_book的一张表，注释掉，会删除这张表
class Book(models.Model):
    #定义一个自增的ID键值
    id=models.AutoField(primary_key=True)
    #定义一个最大长度为32的varchar字段
    title=models.CharField(max_length=32)