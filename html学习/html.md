[TOC]

# HTML简介
## web服务本质
`浏览器发请求-->HTTP协议-->服务端接收请求-->服务端返回响应-->服务端把HTML文件内容发给浏览器-->浏览器渲染页面`
```
import socket

sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(5)

while True:
    conn,addr=sk.accept()
    data=conn.recv(8096)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"<h1>Hello world!</h1>")
    conn.close()
```
## HTML是什么?
>`1、超文本标记语言是一种用于创建网页的标记语言`
>`2、本质上是浏览器可识别的规则`
>`3、网页文件的扩展名：html或者htm`
>`4、HTML是一种标记语言，不是一种编程语言`
## HTML文档结构
```
<!DOCTYPE html>  #声明为html5文档
<html lang="zh-CN"> #是文档的开始标记和结束标记，是html页面的跟元素，在他之间是头部（head）和主体（body）
<head> #定义了html文档的开头部分，他们之间的内容不会在浏览器的文档窗口显示，包含了文档的元（meta）数据
  <meta charset="UTF-8">
  <title>css样式优先级</title> #定义了网页标题，在浏览器标题栏显示
</head>
<body> #之间的文本是可见的网页主题内容

</body>
</html>
```
## HTML标签格式
>`标签的语法：
><标签名 属性1=“属性值1” 属性2=“属性值2”……>内容部分</标签名>
><标签名 属性1=“属性值1” 属性2=“属性值2”…… />`

`1、标签是由尖括号包围的关键字`
`2、成对出现`
`3、也有部分是单独出现的如（<br/>、<hr/>、<img src="1.jpg"/>等）`
`4、标签中可以带属性，也可以不带属性`

	几个很重要的属性：
	id：定义标签的唯一ID，HTML文档树中唯一
	class：为html元素定义一个或多个类名（classname）(CSS样式类名)
	style：规定元素的行内样式（CSS样式）`
	
	HTML注释  <!--注释内容-->
	#<!DOCTYPE>标签
	<!DOCTYPE> 声明必须是 HTML 文档的第一行，位于 <html> 标签之前。
	<!DOCTYPE> 声明不是 HTML 标签；它是指示 web 浏览器关于页面使用哪个 HTML 版本进行编写的指令。

# HTML常用标签
## head内常用标签
| 标签                |            意义            |
| ------------------- | :------------------------: |
| `<title></title> `  |        定义网页标题        |
| `<style></style>`   |       定义内部样式表       |
| `<script></script>` | 定义JS代码或引入外部JS文件 |
| `<link/>`           |     引入外部样式表文件     |
| `<meta/>`           |       定义网页原信息       |

### Meta标签
`meta标签介绍：
	<meta>元素可提供有关页面的原信息（mata-information）,针对搜索引擎和更新频度的描述和关键字
	<meta>标签位于文档的头部，不包含任何内容
	<meta>提供的信息是用户不可见的
	<meta>标签的组成分为：http-equiv属性和name属性`
#### http-equiv属性：
`相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确地显示网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值`
```
<!--2秒后跳转到对应的网址，注意引号-->
<meta http-equiv="refresh" content="2;URL=https://www.oldboyedu.com">
<!--指定文档的编码类型-->
<meta http-equiv="content-Type" charset=UTF8">
<!--告诉IE以最高级模式渲染文档-->
<meta http-equiv="x-ua-compatible" content="IE=edge">
```
#### ame属性：
`主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的`
```
<meta name="keywords" content="meta总结,html meta,meta属性,meta跳转">
<meta name="description" content="老男孩教育Python学院">
```
## Body内常用标签
### 基本标签（块级标签和内联标签）
| 标签              |    意义    |
| ----------------- | :--------: |
| `<b>加粗</b> `    |    加粗    |
| `<i>斜体</i>`     |    斜体    |
| `<u>下划线</u>`   |   下划线   |
| `<s>删除</s>`     |    删除    |
| `<p>段落标签</p>` |  段落标签  |
| `<h1>标题1</h1>`  |   标题1    |
| `<h2>标题2</h2>`  |   标题2    |
| `<h3>标题3</h3>`  |   标题3    |
| `<br>`            |    换行    |
| `<hr>`            | 水平分割线 |
### 特殊字符
| 标签   |   意义   |
| ------ | :------: |
| `空格` | `&nbsp;` |
| `>`    |  `&gt;`  |
| `<`    |  `&lt;`  |
| `&`    | `&amp;`  |
| `￥`   | `&yem;`  |
| `©`    | `&copy;` |
| `®`    | `&reg;`  |
### div标签和span标签
`div标签用来定义一个块级元素，并无实际的意义，主要通过css为其赋予不同的表现`
`span标签用来定义内联（行内）元素，并无实际的意义，主要通过css为其赋予不同的表现`
>HTML标签的分类：
>   1、块儿级标签，默认独占一行（整个浏览器的宽度）可以设置长和高
>   2、行内标签（内联标签）长度由自己的内容来决定的，无法设置长和高
>HTML嵌套的规则：
>   1、块儿级标签可以嵌套行内标签（div标签可以嵌套div标签）
>   2、P标签不能嵌套div标签
### img标签
`<img src="图片的路径" alt="图片未加载成功时的提示" title="鼠标悬浮时提示信息" width="宽" height="高(宽高两个属性只用一个会自动等比缩放)">`
### a标签
`<a></a>标签：超链接标签,如下`
	`<a href="http://www.oldboyedu.com" target="_blank" >点我</a>`
#### href属性
`href属性指定目标网页地址，该地址可以有几种类型：
1、绝对url-指向另一个站点（比如href=“http://www.jd.com”）
2、相对url-指当前站点中确切的路径（href=“index.html”）
3、锚url-指向页面中的锚（href=“#top”）`
#### target属性
`1、_blank表示在新标签页中打开目标网页
 2、_self表示在当前标签页打开目标网页`
### 列表
#### 无序列表
```
<ul type="disc">
	<li>第一项</li>
	<li>第二项</li>
</ul>
#type属性：
1、disc（实心圆点，默认值）
2、circle（空心圆圈）
3、square（实心方块）
4、none（无样式）
```
#### 有序列表
```
<ol type="1" start="2">
	<li>第一项</li>
	<li>第二项</li>
</ol>
#type属性：
1、1 数字列表，默认值
2、A 大写字母
3、a 小写字母
4、I 大写罗马
5、i 小写罗马
```
#### 标题列表
```
<dl>
	<dt>标题1</dt>
	<dd>内容1</dd>
	<dt>标题2</dt>
	<dd>内容1</dd>
	<dd>内容2</dd>
</dl>
```
### 表格
`表格的结构：`
```
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>表格示例</title>
</head>
<body>
<table border="1">
    <thead>
    <tr>
        <th>序号</th>
        <th>姓名</th>
        <th>爱好</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>1</td>
        <td>egon</td>
        <td>更更</td>
    </tr>
    <tr>
        <td>2</td>
        <td>www</td>
        <td>wanwan</td>
    </tr>
    </tbody>
</table>
</body>
</html>
```
#### 表格（table）属性
`border：表格边框
cellpadding：内边框
cellspacing：外边框
width：像素百分比（最好通过css来设置长宽）
rowspan：单元格竖跨多少行
colspan：单元格横跨多少列（合并单元格）`
### form
	功能：
	1、表单用于向服务器传输数据，从而实现用户与web服务器的交互
	2、表单能够包含input系列标签，比如文本字段，复选框，单选框，提交按钮等
	3、表单还可以包含textarea、select、fieldset和label标签
**表单属性：**
| 属性             |                         描述                         |
| ---------------- | :--------------------------------------------------: |
| `accept-charset` |  规定在被提交表单中使用的字符集（默认：页面字符集）  |
| `action`         |      规定向何处提交表单的地址（url）(提交页面)       |
| `autocomplete`   |       规定浏览器应该自动完成表单（默认：开启）       |
| `enctype`        |      规定被提交数据的编码（默认：url-encoded）       |
| `method`         |   规定在提交表单时所用的 HTTP 方法（默认：GET）。    |
| `name`           | 规定识别表单的名称（对DOM使用：document forms name） |
| `novalidate`     |                 规定浏览器不严重表单                 |
| `target`         |      规定action属性中地址的目标（默认：_self）       |
```
<!DOCTYPE html>
<html>
<body>

<form action="/demo/demo_form.asp">
First name:<br>
<input type="text" name="firstname" value="Mickey">
<br>
Last name:<br>
<input type="text" name="lastname" value="Mouse">
<br><br>
<input type="submit" value="Submit">
</form> 

<p>如果您点击提交，表单数据会被发送到名为 demo_form.asp 的页面。</p>

</body>
</html>

```
**表单元素：**
```
#表单工作原理：
#访问者在浏览有表单的网页时，可填写必需的信息，然后按某个按钮提交。这些信息通过Internet传送到服务器上。
from django.conf.urls import url
from django.shortcuts import HttpResponse

def upload(request):
    print("request.GET:", request.GET)
    print("request.POST:", request.POST)

    if request.FILES:
        filename = request.FILES["file"].name
        with open(filename, 'wb') as f:
            for chunk in request.FILES['file'].chunks():
                f.write(chunk)
            return HttpResponse('上传成功')
    return HttpResponse("收到了！")

urlpatterns = [
    url(r'^upload/', upload),
]
```
### input
| type 属性值 |   表现形式   |                    对应代码                    |
| ----------- | :----------: | :--------------------------------------------: |
| text        | 单行输入文本 |             `<input type=text" />`             |
| password    |  密码输入框  |          `<input type="password"  />`          |
| date        |  日期输入框  |            `<input type="date" />`             |
| checkbox    |    复选框    | `<input type="checkbox" checked="checked"  />` |
| radio       |    单选框    |           `<input type="radio"  />`            |
| submit      |   提交按钮   |     `<input type="submit" value="提交" />`     |
| reset       |   重置按钮   |     `<input type="reset" value="重置"  />`     |
| button      |   普通按钮   |  `<input type="button" value="普通按钮"  />`   |
| hidden      |  隐藏输入框  |           `<input type="hidden"  />`           |
| file        |  文本选择框  |            `<input type="file"  />`            |
<p>&nbsp;属性说明:</p>
<ul>
<li>name：表单提交时的“键”，注意和id的区别</li>
<li>value：表单提交时对应项的值
<ul>
<li>type="button", "reset", "submit"时，为按钮上显示的文本年内容</li>
<li>type="text","password","hidden"时，为输入框的初始值</li>
<li>type="checkbox", "radio", "file"，为输入相关联的值</li>
</ul>
</li>
<li>checked：radio和checkbox默认被选中的项</li>
<li>readonly：text和password设置只读</li>
<li>disabled：所有input均适用</li>
</ul>

### select标签

```
<form action="" method="post">
  <select name="city" id="city">
    <option value="1">北京</option>
    <option selected="selected" value="2">上海</option>
    <option value="3">广州</option>
    <option value="4">深圳</option>
  </select>
</form>
```
<p>属性说明：</p>
<ul>
    <li>multiple:布尔属性，设置后为多选，否则默认单选</li>
    <li>disabled:禁用</li>
    <li>selected:默认选中该项</li>
    <li>value:定义提交时的选项值</li>
</ul>
### label标签
`定义：<label>标签为input元素定义标注（标记）`
**说明：**
	`1、label元素不会向用户呈现任何特殊效果
	2、<label>标签的for属性值应当与相关元素的id属性值相同`
```
<form action="">
  <label for="username">用户名</label>
  <input type="text" id="username" name="username">
</form>
```

### textarea多行文本标签
```
<textarea name="memo" id="memo" cols="30" rows="10">
  默认内容
</textarea>
```
<p>属性说明：</p>
<ul>
	<li>name：名称</li>
		<li>rows：行数</li>
			<li>cols：列数</li>
						<li>disabled：禁用</li>
</ul>