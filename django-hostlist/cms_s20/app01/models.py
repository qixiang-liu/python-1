from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=6,decimal_places=2) #数字最多6位，必须有俩个小数位
    create_time=models.DateField()
    memo=models.CharField(max_length=32,default='')
    comment_num=models.IntegerField(default=0)
    poll_num=models.IntegerField(default=0)
    read_num=models.IntegerField(default=0)

    #关联字段（publish）：to_field，关联那个字段，不写默认关联主键，
    publish=models.ForeignKey(to="Publish",default=1)  #book_obj.publish:得到的结果是与这本书籍关联的出版社对象
    # 多对多,写上这个字段，会自动生成Author2Book这张表,把book表和Author表创建一个新的表
    author=models.ManyToManyField('Author') #book_obj.author.all()：就可以得到于这本书关联的全部作者对象，是QuerySet类型
    def __str__(self):return self.title

#一对多的关系，BOOK---->publish
class Publish(models.Model):
    name=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
    def __str__(self):return self.name
#多对多的关系：Book--->author表，多对多然后生成第3张表，第3张表的名字叫book_author,自动生成一个主键，book_id,author_id字段
class Author(models.Model):
    name=models.CharField(max_length=32)
    age = models.IntegerField(default=0)
    #<QuerySet [<Author: Author object>, <Author: Author object>, <Author: Author object>]>
    def __str__(self):return self.name

#一对一的关系：
class AuthorDetail(models.Model):
    tel=models.CharField(max_length=32)
    email=models.EmailField()
    #一对一的关系建立的字段
    author=models.OneToOneField('Author')
    def __str__(self):return self.email

# class Author2Book(models.Model):
#     book_id=models.ForeignKey('Book')
#     author_id=models.ForeignKey('Author')