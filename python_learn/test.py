# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2021/12/27 11:25 上午
# @Function:

# candidate_dict = {'h1': 3, 'h2': 4, 'h3': 5}
# theme = max(candidate_dict, key=lambda x: candidate_dict[x])
# print(theme)
#
# a = [["1", "2"], ["3", "4"], ["5", "6"]]
# t = []
# [t.extend(i) for i in a]
# print(t)
from websocket import create_connection
import json

# ws = create_connection("ws://127.0.0.1:8009/websocket/2001")
ws = create_connection("ws://1.117.166.56:8001/websocket/220101")
# # 发送数据
message = {}
message["username"] = "2001"
message["content"] = "hello world"
json_str = json.dumps(message)
ws.send(json_str)
# 接收数据
result = ws.recv()
print(result)
# 关闭
ws.close()

