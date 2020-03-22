from django.shortcuts import render,HttpResponse,redirect

import time
# Create your views here.
def timer(requests):
    ctime=time.time()
    # return HttpResponse(ctime)
    return render(requests,"timer.html",{"timer":ctime})



def book_detail(requests,id):
    return HttpResponse(id)

def book_achrive(requests,year,month):
    return HttpResponse(year,month)


def login(requests):
    if requests.method=='GET':
        print(requests.GET)  #获取get请求的内容，使用get获取值，使用getlist获取一个列表<QueryDict: {'a': ['1']}>
        print(requests.POST) #获取
        print(requests.method) #查看请求方式
        print(requests.path) #查看请求路径
        print(requests.path_info)
        print(requests.body) #post请求的原始数据

        return render(requests,"login.html")
    else:
        user=requests.POST.get('user')
        pwd=requests.POST.get('pwd')
        if 1:
            return redirect('/app01/timer/')
        return HttpResponse('登录成功')

def template(request):
    l=[11,22,33]
    dic={'lqx':12,'wsw':43}
    class Foo():
        def __init__(self,name):
            self.name=name
        def learning(self):
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
    return render(request, 'temp.html', locals())  #locals可以把前面函数定义的变量类全部传给templates中




#数据库操作
from .models import * #引入models里面的方法和对象
def add(request):
    #添加一本书，方式1
    # obj=Book.objects.create(title='python',price=123,create_time='2012-12-12')
    # print(obj.title)

    #方式2：
    obj=Book(title='php',price=123,create_time='2012-12-12',publish_id=2)
    obj.save()
    return HttpResponse('添加成功')

def query(request):
    #1、all()方法得到的返回值是一个Queryset
    book_list=Book.objects.all()
    print(book_list)

    #2、filter() 拿到也是一个Queryset #过滤满足filter后面条件的结果
    book_list=Book.objects.filter(title='python')[0]
    print(book_list.pk)

    # book_list=Book.objects.filter(price=123,title='python')[0]
    # print(book_list)

    #3、get() model对象 #有且只有一个查询结果，get才有意义，找多了没有，都会报错
    # book=Book.objects.get(price=123,title='python')
    # print(book)

    #4、order_by 排序,加个-,就是降序
    book=Book.objects.all().order_by('id') #升序
    # book = Book.objects.all().order_by('-id')  # 加个-,就是降序
    book_list=Book.objects.all().order_by('price')
    print(book_list)

    #5、count 数数
    c=Book.objects.all().order_by('price').count()
    print(c)

    #6、first()
    first=Book.objects.all()[0]
    first = Book.objects.all().first()

    #7、exists() 如果book表中有书，就打印ok，如果没有，就不打印
    ret=Book.objects.all().exists()  #判断book表中是否有数据
    if ret:
        print('ok')

    #8、distinct() 在返回结果中去重
    # Book.objects.all().difference() #这样查询一点意义都没有，原因是会打印出来主键，主键是不会重复的。所以distinct是无效的
    ret=Book.objects.all().values('title').distinct()
    print(ret)


    #9、values() #只打印某一个列
    ret=Book.objects.all().values('title','price')
    print(ret) #<QuerySet [{'title': 'python'}, {'title': 'python'}, {'title': 'python'}, {'title': 'php'}]>
   # '''#values，其实就是做了一个下面的操作
   # temp=[]
   # for obj in Book.objects.all():
   #      temp.append({
   #          "title":obj.title,
   #          "price":obj.price
   #      })
   # '''
    ret=Book.objects.all().values_list('title','price') #只是把打印的结果变成元组，打印出来
    print(ret)

    #10、模糊查询：__ 双下划线
    ret=Book.objects.filter(title__startswith='py')
    # lt(小于)、in=([11,22,33])(包含这个里面的)、contains(包含就可以)，icontains（不区分大小写），range（范围）
    rets=Book.objects.filter(price__gt=200)

    return HttpResponse('OK')

def delete(request):
    Book.objects.filter(price=123,title='python').delete()
    return HttpResponse('ok')

def update(request):
    Book.objects.filter(price=234,title='python').update(title='python213')
    return HttpResponse('ok')


#多对多查询
def books(request):

        book_list=Book.objects.all()
        #一对多查询
        book_obj=Book.objects.filter(id=14).first()
        # print(book_obj.publish.name)
        # print(book_obj.publish.email)

        #多对多的查询
        book_obj=Book.objects.filter(id=14).first()
        # print(book_obj.author.all())
        return render(request,'books.html',locals())


def addbook(request):
    if request.method=='POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        date=request.POST.get('date')
        publish_id=request.POST.get('publish_id')
        author_id_list=request.POST.getlist('author_id_list')  #可以获取一个列表
        #绑定一对多的关系，书籍与出版社的关系
        obj=Book.objects.create(title=title,price=price,create_time=date,publish_id=publish_id)
        print('author_id_list::::::'%author_id_list)
        #绑定书籍与作者的多对多的关系
        #不可行的，因为第三张表不是我们手动创建的
        # for author_id in author_id_list:
        #     A.objects.create(book_id=obj.pk,author_id=author_id)
        #可行的方案：django自动创建的表，可以自动生成表记录
        obj.author.add(*author_id_list) #*会自动循环列表，取值,添加，自动调用save方法
        #解除绑定关系
        # obj.author.remove(1)
        #clear清除全部信息
        # obj.author.clear()

        return redirect('/books/')

    else:
        publish_list=Publish.objects.all()
        author_list=Author.objects.all()

        return render(request,'addbook.html',locals())

def deler(request,id):
    Book.objects.filter(id=id).delete()
    return redirect('/books/')

def edit(request,id):
    if request.method=='POST':
        # id=request.POST.get('book_id')
        title=request.POST.get('title')
        price=request.POST.get('price')
        create_time=request.POST.get('date')
        publish=request.POST.get('publish_id')
        author_list=request.POST.getlist('author_id_list')
        # print(id,title,price,create_time,publish,author_list)
        obj = Book.objects.filter(id=id)
        print('>>>>>>%s'%obj)
        #方式1：
        Book.objects.filter(id=id).update(title=title,price=price,create_time=create_time,publish_id=publish)
        # #方式2：但是这个不能有额外的键值，只能一一对应
        # Book.objects.filter(id=id).update(**request.POST)


        # # 方式1：
        # book=Book.objects.filter(id=id).first()
        # book.author.clear()
        # book.author.add(*author_list)

        # #方式3：set直接可以传列表
        # book.author.set(author_list)

        #方式2：
        Book.objects.filter(id=id)[0].author.clear()  #直接使用clear清空第三张表的数据，然后在下面再次添加第三张表的关联数据就好了
        Book.objects.filter(id=id)[0].author.add(*author_list)
        return redirect('/books/')
    else:
        obj=Book.objects.filter(id=id)[0]
        print(obj)
        print(obj.pk)
        publish_list=Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,'edit.html',locals())


def multi_query(request):
    ######################基于对象的跨表查询###########################
    #----- 一对多：正向查询和反向查询

    #（正向查询） 查询id=1的书籍的出版社的名称
    obj=Book.objects.filter(id=20).first()
    print(obj.publish.name)

    #(反向查询)  查询苹果出版社出版过的图书名称
    publish_obj=Publish.objects.filter(name='橘子').first()
    print(publish_obj.book_set.all())#book_set,一对多的表去反向查询有关联字段的表的数据
    for book in publish_obj.book_set.all():
        print(book.title)

    #----- 多对多：
    #（正向查询） 查询java所有的作者名字
    obj=Book.objects.filter(title='java').first()
    print(obj.author.all().values())
    for i in obj.author.all():
        print(i.name)

    #(反向查询) 查询alex对应的所有数据
    obj=Author.objects.filter(name='alex').first()
    print(obj.book_set.all().values('title'))  #<QuerySet [{'title': 'php'}, {'title': 'php'}, {'title': 'java'}]>

    #一对一
    #(反向查询) 查询alex的手机号
    obj=Author.objects.filter(name='alex').first()
    print(obj)
    print(obj.authordetail.tel) #必须使用小写

    #（正向查询）查询手机号为18311166263的作者的名字
    obj=AuthorDetail.objects.filter(tel='18311166263').first()
    print(obj.author.name) #必须使用小写

    ##########################基于queryset的跨表查询##############################
    #一对多：
    #（正向查询）查询价格等于100的数据的出版社的名称：
    # 方法1：
    # book_list=Book.objects.filter(price=100)
    # for i in book_list:
    #     print(i.publish.name)
    #方法2：使用values，自动去循环，
    ret=Book.objects.filter(price=100).values('title','publish__name')
    print(ret)#[{},{},{}]
    ps='''
        values:
        temp=[]
        for book in Book.objects.filter(price=100):
            temp.append({'titel':book.title,
                         'publish__name':book.publish.name}
                        )
    '''
    #（反向查询） 查询苹果出版社出版过所有的书籍名称
    ret=Publish.objects.filter(name='苹果').values('book__title')
    print(ret)
    ps='''
        publish_obj=Publish.objects.filter(name='苹果').first()
    temp=[]
    for book in publish_obj.book_set.all():
        book.append({
            'book_title':book.title
        })
    '''

    #多对多：
    #（正向查询）查询java所有作者的名字：
    ret=Book.objects.filter(title='php').values('author__name','title').distinct() #distinct去重
    print(ret)

    #（反向查询）查询alex出版过的所有书籍名称：
    ret=Author.objects.filter(name='alex').values('book__title')
    print(ret)

    #一对一：
    #(反向查询)查询alex的手机号：
    obj=Author.objects.filter(name='alex').values('authordetail__tel')
    print(obj)  #<QuerySet [{'authordetail__tel': '18311166263'}]>

    #（正向查询）查询手机号为18311166263的作者的名字
    ret=AuthorDetail.objects.filter(tel='18311166263').values('author__name')
    print(ret)  #<QuerySet [{'author__name': 'alex'}]>

    #多表关联查询：查询手机号以1开头的作者出版社的书籍名称以及出版社的名称
    ret=AuthorDetail.objects.filter(tel__startswith='1').values('author__book__title','author__book__publish__name')
    print(ret)

    ##################################聚合与分组###################################
    #聚合：
    #统计所有书籍的平均价格
    from django.db.models import Avg,Count,Min,Max
    ret=Book.objects.all().aggregate(c=Avg('price'))
    print(ret)

    #分组：
    #查询每个出版社出版的书籍个数,加上一个c,会统计每个组的个数
    ret=Publish.objects.all().annotate(c=Count('book')).values('name','c')
    print(ret)

    #查询每一个作者出版的书籍的平均价格
    ret=Author.objects.all().annotate(price_avg=Avg('book__price')).values('name','price_avg')
    print(ret)

    #查询每一本书籍名称以及作者的个数
    ret=Book.objects.all().annotate(c=Count('author')).values('title','c')
    print(ret)

    #查询价格大于200的书籍以及每一本书的个数
    ret=Book.objects.filter(price__gt=200).values('title')
    print(ret)

    ################################F与Q的查询######################################
    from django.db.models import F,Q
    #F的使用：
    #求comment_num大于read_num的book的queryset对象
    ret=Book.objects.filter(comment_num__gt=F('read_num'))
    print(ret)
    ret=Book.objects.filter(comment_num__gt=F('read_num')*10)
    print(ret)

    ret=Book.objects.all().update(price=F('price')+100)

    #Q的使用：
    #以p开头，并且价格大于300
    ret=Book.objects.filter(title__startswith='p',price__gt=300)
    print(ret)

    #|和~的使用：|或的意思，~非的意思
    ret=Book.objects.filter(Q(title__startswith='p')|~Q(price__gt=300))
    print(ret)
    ret=Book.objects.filter(Q(title__startswith='p')|~Q(price__gt=300),create_time__year=2018)
    print(ret)

    ##############################作业###############################
    #1、查询苹果出版社出版过的价格大于1000的书籍的作者的email
    # publish-->book-->author-->detail  (values中是表_表_表_字段)
    publish_author_detail_email=Publish.objects.filter(name='苹果').first().book_set.filter(price__gt=1000).values('author__authordetail__email').distinct() #
    print(publish_author_detail_email)

    #2、查询alex出版过的所有书籍的名称以及书籍的出版社的名称
    author_book_publish=Author.objects.filter(name='alex').values('book__title','book__publish__name')
    print(author_book_publish)

    #3、查询2017年出版社过的所有书籍的作者名字以及出版社名称
    book_author_publish=Book.objects.filter(create_time__year=2017).values('author__name','publish__name')
    print(book_author_publish)

    #4、查询手机号为'1831111111'并且email以183111开头的作者写过的所有书籍名称以及书籍的出版社名称
    detail_author_book_publish=AuthorDetail.objects.filter(tel='1831111111',email__startswith='183111').values('author__book__title','author__book__publish__name')
    print(detail_author_book_publish)

    #5、查询年龄大于20岁的作者在哪些出版社出版过书籍
    author_publish_book=Author.objects.filter(age__gt=20).values('book__publish__name').distinct()
    print(author_publish_book)

    #6、查询每一个出版社的名称以及出版过的书籍个数
    publish_book=Publish.objects.all().annotate(c=Count('book')).values('name','c')
    print(publish_book)

    #7、查询每一个作者的名字以及出版过的所有书籍的最高价格
    author_book=Author.objects.all().annotate(c=Max('book__price')).values('name','c')
    print(author_book)

    #8、查询每一本书的名字，对应出版社名称以及作者的个数
    book_pulish_author=Book.objects.all().annotate(c=Count('author__name')).values('title','c')
    print(book_pulish_author)

    return HttpResponse(200)




