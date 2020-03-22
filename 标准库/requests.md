[TOC]

# get请求
```python
无参树实例
import requests
ret= requests.get('https://github.com/timeline.json')

print(ret.url)
print(ret.text)

# 有参数实例

import requests
#get传参
payload={'key':'value1','key2','value2'}
ret= requests.get('https://github.com/timeline.json',params=payload)

print(ret.url)
print(ret.text)
```

# post请求
```PYTHON
# 基本post实例
import requests

payload={'key':'value1','key2':'value2'}
ret=requests.post('https://github.com/timeline.json',params=payload)
print(ret.text)

#发送请求头和数据实例

import requests
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

ret = requests.post(url, data=json.dumps(payload), headers=headers)

print ret.text
print ret.cookies
```
# 其他请求
```python
requests.get(url,params=None,**kwargs)

requests.post(rul,data=None,json=None,**kwargs)

requests.head(url, **kwargs)

requests.delete(url, **kwargs)

requests.patch(url, data=None, **kwargs)

requests.options(url, **kwargs)

# 以上方法均是在此方法的基础上构建
requests.request(method, url, **kwargs)
```
# request参数介绍
## method_url
```PYTHON
requests.request(method='get',url='http://127.0.0.1:80/text/')
requests.request(method='post',url='http://127.0.0.1:80/text/')
```
## params
> 可以是[dict,str,bytes]
```PYTHON
#way1
requests.request(method='get',
                 url="http://127.0.0.1:80/text/",
                 params={'k1':'value1','k2':'value2'}
                 )
# way2
requests.request(method='get',
                 url='http://127.0.0.1:8000/test/',
                 params="k1=v1&k2=水电费&k3=v3&k3=vv3"
                 )
# way3，下面params不支持汉字进行转码
#使用汉字转码会报错：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 9: ordinal not in range(128)
requests.request(method='get',
                 url='http://127.0.0.1:8000/test/',
                 params=bytes("k1=v1&k2=k2&k3=v3&k3=vv3", encoding='utf8')
                 )
```
## data
>可以是[dict,str,bytes,FileObject]
```PYTHON
#way1--dict
requests.request(method='POST',
                 url='http://127.0.0.1:8000/test/',
                 data={'k1': 'v1', 'k2': '水电费'})
#way2--str
requests.request(method='POST',
                 url='http://127.0.0.1:8000/test/',
                 data="k1=v1; k2=v2; k3=v3; k3=v4"
)
#way3--bytes
requests.request(method='POST',
                url='http://127.0.0.1:8000/test/',
                data="k1=v1;k2=v2;k3=v3;k3=v4",
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
)
#way4--fileobject
requests.request(method='POST',
                 url='http://127.0.0.1:8000/test/',
                 data=open('data_file.py', mode='r', encoding='utf-8'), # 文件内容是: k1=v1;k2=v2;k3=v3;k3=v4
                 headers={'Content-Type': 'application/x-www-form-urlencoded'}
)
```
## json
```PYTHON
# 将json中对应的数据进行序列化成一个字符串，json.dumps(...)
# 然后发送到服务器端的body中，并且Content-Type是 {'Content-Type': 'application/json'}
requests.request(method='POST',
                 url='http://127.0.0.1:8000/test/',
                 json={'k1': 'v1', 'k2': '水电费'})
```
## headers
```PYTHON
# 发送请求头到服务器端
requests.request(method='POST',
                 url='http://127.0.0.1:8000/test/',
                 json={'k1': 'v1', 'k2': '水电费'},
                 headers={'Content-Type': 'application/x-www-form-urlencoded'}
                 )
```
## cookies
```PYTHON
# 发送Cookie到服务器端
requests.request(method='POST',
                 url='http://127.0.0.1:8000/test/',
                 data={'k1': 'v1', 'k2': 'v2'},
                 cookies={'cook1': 'value1'},
                 )
# 也可以使用CookieJar（字典形式就是在此基础上封装）
from http.cookiejar import CookieJar
from http.cookiejar import Cookie

obj = CookieJar()
obj.set_cookie(Cookie(version=0, name='c1', value='v1', port=None, domain='', path='/', secure=False, expires=None,
                      discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False,
                      port_specified=False, domain_specified=False, domain_initial_dot=False, path_specified=False)
               )
requests.request(method='POST',
                 url='http://127.0.0.1:8000/test/',
                 data={'k1': 'v1', 'k2': 'v2'},
                 cookies=obj)
```
## files
```python
#发送文件
file_dict = {
'f1': open('readme', 'rb')
}
requests.request(method='POST',
url='http://127.0.0.1:8000/test/',
files=file_dict)

#发送文件，定制文件名
file_dict = {
'f1': ('test.txt', open('readme', 'rb'))
}
requests.request(method='POST',
url='http://127.0.0.1:8000/test/',
files=file_dict)

#发送文件，定制文件名
file_dict = {
'f1': ('test.txt', "hahsfaksfa9kasdjflaksdjf")
}
requests.request(method='POST',
url='http://127.0.0.1:8000/test/',
files=file_dict)

#发送文件，定制文件名
file_dict = {
     'f1': ('test.txt', "hahsfaksfa9kasdjflaksdjf", 'application/text', {'k1': '0'})
}
requests.request(method='POST',
                  url='http://127.0.0.1:8000/test/',
                  files=file_dict)
```
## auth
```PYTHON
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

ret = requests.get('https://api.github.com/user',
                  auth=HTTPBasicAuth('wupeiqi', 'sdfasdfasdf')
                  )
print(ret.text)

ret = requests.get('http://192.168.1.1',
                   auth=HTTPBasicAuth('admin', 'admin')
                   )
ret.encoding = 'gbk'
print(ret.text)

ret = requests.get('http://httpbin.org/digest-auth/auth/user/pass',
                   auth=HTTPDigestAuth('user', 'pass')
                   )
print(ret)
```

## timeout
```PYTHON
ret = requests.get('http://google.com/', timeout=1)
print(ret)

ret = requests.get('http://google.com/', timeout=(5, 1))
print(ret)
```

## allow_redirects
>如果允许POST / PUT / DELETE重定向，则设置为True。
```PYTHON
ret = requests.get('http://127.0.0.1:8000/test/', allow_redirects=False)
print(ret.text)
```
## proxies(代理)
```PYTHON
proxies = {
    "http": "61.172.249.96:80",
    "https": "http://61.185.219.126:3128",
}

proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}

ret = requests.get("http://www.proxy360.cn/Proxy",
                   proxies=proxies)
print(ret.headers)


from requests.auth import HTTPProxyAuth

proxyDict = {
    'http': '77.75.105.165',
    'https': '77.75.105.165'
}
auth = HTTPProxyAuth('username', 'mypassword')

r = requests.get("http://www.google.com",
                 proxies=proxyDict,
                 auth=auth)
print(r.text)
```
## stream(流式请求)
```PYTHON
ret = requests.get('http://127.0.0.1:8000/test/', stream=True)
print(ret.content)
ret.close()

from contextlib import closing
with closing(requests.get('http://httpbin.org/get', stream=True)) as r:
# 在此处理响应。
for i in r.iter_content():
print(i)
```
## session
```PYTHON
import requests

session = requests.Session()

### 1、首先登陆任何页面，获取cookie

i1 = session.get(url="http://dig.chouti.com/help/service")

### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
i2 = session.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': "8615131255089",
        'password': "xxxxxx",
        'oneMonth': ""
    }
)

i3 = session.post(
    url="http://dig.chouti.com/link/vote?linksId=8589623",
)
print(i3.text)

```
