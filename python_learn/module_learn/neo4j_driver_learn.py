# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2021/12/26 10:31 下午
# @Function: 使用neo4j Driver来连接neo4j
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

