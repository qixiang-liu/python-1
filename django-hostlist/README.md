[toc]

### 1、流程：

-  设计url：
 ```
url(r'^timer/',timer), #timer(request) 
 ```
- 构建视图函数：
 ```
 在views.py：
 def timer(request):
     import time
     ctime=time.time()
     return render(request,'timer.html',{'ctime':ctimer})
 ```
- templates:
```
timer.html
<p>当前时间：{{ ctime }}</p>
```

### 2、url控制器（路由层）：
- 简单配置
- 分组
```
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/([0-9]{4})/$', views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
```
- 有名分组
- 分发
- 反向解析
```
    url(r'^login/', login,name='name_login'), #制作别名
    <form action="{% url 'name_login' %}" method="post"> {# 在template中就可以使用别名来访问#}
    
    from django.conf.urls import url,include
    url(r'^app01/',include('app01.urls'),), #分组，app01/xxx/都去app01目录下面的urls的文件中找路径
    
    #url 的路径与正则匹配
    url(r'^book/(\d+)$', book_detail), #book_detail(request,\d+)
    url(r'^book_achrive/(\d+)/(\d+)$', book_achrive),  # book_detail(request,\d+,\d+)
    url(r'^book_achrive/(?P<year>\d+)/(?P<month>\d+)$', book_achrive),  # book_detail(request,year=\d+,month=\d+) #有名分组
    
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
```
### 3、MTV-view（视图层）：负责业务逻辑，并在适当的时候调用Model和Template
- 请求对象
- 响应对象
```
def login(requests):
    if requests.method=='GET':
        print(requests.GET)  #获取get请求的内容，使用get获取值，使用getlist获取一个列表<QueryDict: {'a': ['1']}>
        print(requests.POST) #获取
        print(requests.method) #查看请求方式
        print(requests.path) #查看请求路径
        print(requests.path_info)
        print(requests.body) #post请求的原始数据

        return render(requests,"login.html"，locals()) #locals可以把前面函数定义的变量类全部传给templates中
    else:
        user=requests.POST.get('user')
        pwd=requests.POST.get('pwd')
        if 1:
            return redirect('/app01/timer/') #跳转，302跳转
        return HttpResponse('登录成功') #直接返回结果
```
### 4、MTV-Template（模板层）：负责如何把页面展示给用户
- 渲染变量
- 渲染标签
```
def template(request):
    l=[11,22,33] #列表
    dic={'lqx':12,'wsw':43} #字典
    class Foo(): #类
        def __init__(self,name):
            self.name=name #类属性
        def learning(self): #类方法
            print('learing')
            return 'def---learing'
    alex=Foo('alex')
    egon=Foo('egon')
    person_list=[alex,egon]

    import datetime
    now=datetime.datetime.now()
    print(now)
    file_size=12313123124324234
    content="hello yuan world ............."
    s="<a href='http://www.baidu.com'>hello</a>"
    # render(request,'template.html',{'l':l,'dic':dic})
    return render(request, 'temp.html', locals())


<h3>变量</h3>
<!--句点符-->
<!--获取传进来的列表的值，或者列表-->
<p>{{ l }}</p>
<p>{{ l.0 }}</p>
<!--获取字典中的值-->
<p>{{ dic }}</p>
<p>{{ dic.lqx }}</p>
<!--获取一个对象中的属性，或者方法-->
<p>{{ alex.name }}</p>
<p>{{ alex.learning }}</p><!--获取一个对象中的方法-->
<hr>
<!--循环一个列表并且打印出来列表中的每个对象的属性，或者方法-->
{% for person in person_list %}
    <p>{{ person.learning }}</p>
    <p>{{ person.name }}</p>
{% endfor %}
<hr>

<h3>过滤器</h3>
<!--过滤器的使用-->
<!--add的使用-->
<p>{{ l.1|add:1000 }}</p>  <!--把列表中的一个值加1000，返回到页面-->
<p>{{ now|date:"Y-m-d" }}</p>  <!--时间格式化-->
<p>{{ file_size|filesizeformat }}</p> <!--文件大小展示-->
<p>{{ content|truncatechars:8 }}</p><!--指摘取一部分显示到前端页面-->
<p>{{ s }}</p>  <!--后端给的什么变量，前端就输出什么-->
hr
<h3>标签</h3>

{#for循环中有一个forloop，是for循环自带的一个cont，每次循环就加1#}
{% for person in person_list %}
    <p>{{ forloop.counter }} {{ person.name }}:{{ person.age }}</p>
{% endfor %}

{#if 标签的使用#}
{% if 2 == 2 %}
    <p>yuan</p>
    {% else %}
     <P>lqx</P>
{% endif %}
<hr>

{#如果第一次访问，就直接发post请求，就会被拦截掉，返货403 forbidden掉#}
{# csrf_token的意思的临时关闭csrf功能 #}
{% csrf_token %}
```
- 自定义过滤器和标签
```


#自定义一个标签或者一个过滤器
from django import template
register=template.Library()

@register.filter
def multi_filter(x,y):

    return x * y


@register.simple_tag
def multi_tag(x, y):
    return x * y
    
{#导入一个模块,需要在自己的app中创建一个目录名字叫templatetags的目录，然后定格导入模块#}
{% load my_filers_tags %}
.
..
....
<h4>自定义过滤器或者标签</h4>
{#|左边一个参数，右边一个参数#}
<p>{{ l.0|multi_filter:20 }}</p>
<p>{% multi_tag 20 40 %}</p>
```
### 5、MTV-Model（模型层）：负责业务对象与数据库的对象（ORM）
- ORM-对象关系映射
```
class Book(model.Model):
		    title=models.CharFiled(max_length=32)
			
create table book (
		     title varchar(32)			
		)
		
类名        ------表名
类属性      ------表字段
类实例对象  ------表记录
```
- 单表记录操作
```
Book
    id    title
    1     python
	2     java
```
- - 添加记录：
```
# 方式1：
# obj新添加记录对象
obj=Book.objects.create(title="python")
# 方式2：
obj=Book(title="java")
obj.save() 
```
- - 查询记录：
```
obj=Book.objects.{<1>/<2>/<3>/<4>/<5>/<6>/<7>/<8>....}
    <1> all():                 查询所有结果
	<2> filter(**kwargs):      它包含了与所给筛选条件相匹配的对象
	<3> get(**kwargs):         返回与所给筛选条件相匹配的对象，返回结果有且只有一个，
 如果符合筛选条件的对象超过一个或者没有都会抛出错误。	 
	<5> exclude(**kwargs):     它包含了与所给筛选条件不匹配的对象
	<4> values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
							   model的实例化对象，而是一个可迭代的字典序列
	*<9> values_list(*field):      它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
	<10> count():              返回数据库中匹配查询(QuerySet)的对象数量。
	<11> first():              返回第一条记录
	<12> last():               返回最后一条记录
	<13> exists():            如果QuerySet包含数据，就返回True，否则返回False
	<6> all().order_by(*field):      对查询结果排序
	<7> all().reverse():             对查询结果反向排序
	<8> values(*field).distinct():   从返回结果中剔除重复纪录,必须要和values（），一起使用
```
- - 模糊查询：
```
 ret=Book.objects.filter(title__startswith='py')
#title__lt(小于)、title__in=([11,22,33])(包含这个里面的)、title__contains(包含就可以)，title__icontains（不区分大小写），title__range（范围）
rets=Book.objects.filter(price__gt=200)
```
- - 更新记录：
```
Book.objects.filter(price=123,title="python").update(title="python123") 
```
- - 删除记录：
```
Book.objects.filter(price=123,title="python").delete()
```
- mysql表关系
- 一对多关系：
```
    #关联字段（publish）：to_field，关联那个字段，不写默认关联主键，
    publish=models.ForeignKey(to="Publish",default=1)  #book_obj.publish:得到的结果是与这本书籍关联的出版社对象
```
- 多对多关系：
```
	Book
	   title=...
        # 多对多,写上这个字段，会自动生成Author2Book这张表,把book表和Author表创建一个新的表
        author=models.ManyToManyField('Author') #book_obj.author.all()：就可以得到于这本书关联的全部作者对象，是QuerySet类型
       authors=
       
	Publish
	   name=....
	   
	Author
	   name=....
	<!--book_author--> 会自动生成第三张表
	  
```
