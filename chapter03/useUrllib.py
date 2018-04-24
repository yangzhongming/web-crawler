'''
1.urlopen(): 浏览器发起请求
'''

# import urllib.request
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))

'''
2.type():查看输出响应类型
'''
# import urllib.request
# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))

'''
3.read():查看网页内容
'''
# import urllib.request
# response = urllib.request.urlopen('https://www.python.org')
# 返回响应的状态码
# print(response.status)
#返回响应的头信息
# print(response.getheaders())
#返回服务器
# print(response.getheader('Server'))

'''
4.data参数
'''
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

'''
5.timeout参数
'''
# import urllib.request
# response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# print(response.read())

'''
2.Request
'''
# import urllib.request
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# Request通过参数来构造发起的的请求
# Request(url,data=None,headers={},origin_req_host=None,unverifiable=False,method=None)
# from urllib import request,parse
# url = 'http://httpbin.org/post'                                              # url必填参数
# headers = {'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', # 请求头，通过修改User-Agent来伪装浏览器
#            'Host':'httpbin.org'
#            }
# dict = {'name':'Germy'}
# data = bytes(parse.urlencode(dict),encoding='utf8')                            # 必须传bytes,如果传入参数是字典，可通过urllib.parse转码
# req = request.Request(url=url,data=data,headers=headers,method='POST')
# reponse = request.urlopen(req)
# print(reponse.read().decode('utf-8'))

'''
2.Handler
'''
# from urllib.request import  HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
# from urllib.error import URLError
#
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,username,password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

'''
代理
'''
# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
#
# proxy_handler = ProxyHandler({'http':'http://127.0.0.1:9743',
#                               'https':'http://127.0.0.1:9743',
#                               })
#
# opener = build_opener(proxy_handler)
#
# try:
#     reponse = opener.open('https://www.baidu.com')
#     print(reponse.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

'''
Cookies
'''
# import http.cookiejar,urllib.request
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# reponse = opener.open('http://www.baidu.com')
#
# for item in cookie:
#     print(item.name+"="+item.value)

'''
Cookies 保存
'''
# import http.cookiejar,urllib.request
#
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)   # cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# reponse = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

# 使用LWPCookieJar
#生成cookies1.txt
# import http.cookiejar,urllib.request

# filename = 'cookies1.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# reponse = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

# 通过读取上述生成的cookies1.txt生成百度网页
import http.cookiejar,urllib.request
filename = 'cookies1.txt'
cookie = http.cookiejar.LWPCookieJar()
cookie.load(filename,ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
reponse = opener.open('http://www.baidu.com')
print(reponse.read().decode('utf-8'))