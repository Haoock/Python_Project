# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2021/12/23 1:43 下午
# @Function:Flask中的Request学习

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'GET':
        # 假设有如下 URL
        # http://http://127.0.0.1:5000/login?name=john&age=20
        name = request.args.get("name")
        age = request.args.get("age")
        print(name)
        print(age)
        res = json.dumps(request.json)
        print(res)
    if request.method == 'POST':
        # 假设有如下 JSON 数据
        # {"obj": [{"name":"John","age":"20"}] }

        # 方法一：
        data = request.get_json()  # 获取 JSON 数据
        print(data)
        obj = data.get("obj", [])
        print(obj)
        # 方法二
        # data = request.json        # 获取 JOSN 数据
        # data = data.get('obj')     #  以字典形式获取参数

        return {
            'code': 200,
            'success': True,
            'msg': "",
            'data': None
        }


if __name__ == '__main__':
    app.run(debug=True)


