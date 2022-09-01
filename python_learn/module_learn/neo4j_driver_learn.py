# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2021/12/26 10:31 下午
# @Function: 使用neo4j Driver来连接neo4j
# 安装neo4jDriver：pip3 install neo4j-driver

from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "123456"))


def find_nodes(tx):
    result = tx.run("MATCH (n) RETURN n LIMIT 2")
    lst = []
    print(type(result))
    for record in result:
        print(record)  # 这是每一条结果
        print(record.keys())  # 返回record中所有可以使用的关键字
        print(record.get('n'))  # 使用关键字来获取record中的值
        lst.append(record)
    return lst


def find_path(tx):
    result = tx.run("match p=(a)-[*1..2]->(b) where b.name in ['服务安全'] return p")
    print(type(result))
    lst = []
    for record in result:
        print(record)  # 这是每一条结果
        print(record.get('p'))  # 使用关键字来获取record中的值
        path = record.get('p')
        nodes = path.nodes
        relationship = path.relationships
        print(nodes)
        print(relationship)
        lst.append(record)
    return lst


with driver.session() as session:
    res = session.read_transaction(find_path)
    print(type(res[0]))
    print(res)

driver.close()
