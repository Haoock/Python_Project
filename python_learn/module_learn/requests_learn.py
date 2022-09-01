import requests

r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}) # 豆瓣首页
print(r.status_code)
print(r.text)
print(r.encoding)

################################################################################################################
# requests中的session：
# 在requests里，session对象是一个非常常用的对象，这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。
# 1、创建session对象：
session = requests.session()
# 2、得到session对象就可以用它来发送请求了：
# response1 = session.get(url,params,headers)
# response1 = session.get(url,params,headers)

# requests也可以直接发请求，两者区别如下：
"""
常规操作是我们 通过调用登陆接口 来获取响应的 cookie信息。然后拿这个 cookie信息作为下一次请求的参数（cookie带有当前登陆人的信息）来请求 查询订单的接口
# 以下代码纯为了举例，没有效果的伪代码
import requests
# 登陆接口
response1 = requests.get(url_login,params,headers)
# 获取cookies信息
cookies = response.cookies
# 得到的cookies 是一个字典类型
cookie = cookies.get("cookies的key")
# 请求 查询接口
response2 = requests.get(search_url,params,headers,cookies=cookie)
# 查看查询响应的结果
response2.json()
————————————————
版权声明：本文为CSDN博主「6先生6」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_25986923/article/details/105332640
"""
# 使用session发送请求如下：
"""
# 以下代码纯为了举例，没有效果的伪代码
import requests
# 获取 session对象
session = requests.session()
# 登陆接口
response1 = session.get(url_login,params,headers)
# 请求 查询接口
response2 = session.get(search_url,params,headers)
# 查看查询响应的结果
response2.json()
————————————————
版权声明：本文为CSDN博主「6先生6」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_25986923/article/details/105332640
"""
# 可以发现session对象能够自动获取到cookie并且可以在下一次请求红自动带上我们所得到的的cookie信息，不用人为的去填写

