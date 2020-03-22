[TOC]

# 字符生成列表：

`print(list('hello'))`

# 字符按照一定的规则生成列表：

```python
s='hello alex alex say hello sb sb'
l7=s.split()
print(l7)

//字符无损转换列表：
limit_res=['1,lqx,25,123,运维,1000,2013-11-01\n', '2,alex,26,186,运维,10000,2012-12-25\n','3,egon,25,155,Market,10000,2015-10-14\n', '4,刘祺祥,22,111,维护,10000,2017-8-1']
lis=[]
for i  in limit_res:
    lis.append(i)
>>>
>['1,lqx,25,123,运维,1000,2013-11-01\n']
```

# 字典元素生成列表：

```python
dic={'name':'lqx','age':18,'sex':'male'}
print(list(dic.items()))
```
# 字典key生成列表：

`print(list(dic.keys()))`

# 列表生成字典：

```python
lll={}
print(lll.fromkeys(lis))
```
# 字符生成字典：

```python
lll={}
print(lll.fromkeys('worl'))
```

#文件内容生成字典：

```python
#文件内容是
{'name':'lqx','age':'22'}
with open(db,encoding='utf-8') as f:
    dic=eval(f.read())
#eval拿到的就是dict类型

#文件内容是：
[1,2,3,4,5]
with open(db,encoding='utf-8') as f:
    lis=eval(f.read())
#eval拿到的就是list类型
```
#列表转换字符串：

```python
dic={'id': '6', 'name': '张松', 'age': '26', 'phone': '13683177094', 'dept': 'IT', 'enroll_date': '2013-10-08\n'}
lis=list(dic.values())
st=','.join(lis)
print(st)
>>>
>6,张松,26,13683177094,IT,2013-10-08

```