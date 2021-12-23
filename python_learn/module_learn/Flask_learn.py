# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2021.12.22
# @Function: 简单测试和使用Flask
from flask import Flask

'''
接下来，我们创建一个该类的实例，第一个参数是应用模块或者包的名称。 
如果你使用单一的模块（如本例），你应该使用 __name__ ，
因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同（ 也即是 '__main__' 或实际的导入名）。
这是必须的，这样 Flask 才知道到哪去找模板、静态文件等等。
'''
app = Flask(__name__)

'''
然后，我们使用 route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数。
'''
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # host：这会让操作系统监听所有公网 IP。即网络中其它任何的地方都可以访问。
    # 否则只能在本机访问该服务器
    # debug：True：虽然 run() 方法适用于启动本地的开发服务器，但是你每次修改代码后都要手动重启它。
    # 这样并不够优雅，而且 Flask 可以做到更好。如果你启用了调试支持，服务器会在代码修改后自动重新载入，
    # 并在发生错误时提供一个相当有用的调试器。
    app.run(debug=True)
