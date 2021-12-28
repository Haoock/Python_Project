# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2021/12/26 7:00 下午
# @Function: 主要是学习使用py2neo来连接neo4j并且使用基础语法

from py2neo import *


# 首先是连接neo4j数据库
graph = Graph('http://127.0.0.1:7474', auth=("neo4j", "123456"))

# 创建两个节点
# 首先是定义节点类型
# 其次是分别给予这两个节点属性name
test_node_1 = Node("Person", name="test_node_1")
test_node_2 = Node("Person", name="test_node_2")
graph.create(test_node_1)
graph.create(test_node_2)

# 节点之间的关系，关系的类型为Call，关系也可以有属性：count
node_1_call_node_2 = Relationship(test_node_1, 'CALL', test_node_2)
node_1_call_node_2['count'] = 1
node_2_call_node_1 = Relationship(test_node_2,'CALL',test_node_1)
node_2_call_node_1['count'] = 2
graph.create(node_1_call_node_2)
graph.create(node_2_call_node_1)

