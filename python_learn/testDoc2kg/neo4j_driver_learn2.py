from neo4j import GraphDatabase


dic = {'1':"fdsa", '2': "fdsa1232 "}
print(dic.values())
# driver = GraphDatabase.driver("bolt://10.176.40.125:7687", auth=("neo4j", "doc2kg_root"), encrypted=False)
#
#
# def find_doc_nodes(tx):
#     res = ['大数据技术体系', '大数据资源全生命周期流转', '典型状态', '依据', '大数据采集', '大数据存储', '大数据计算', '大数据分析',
#            '大数据融合共享', '大数据治理', '大数据安全保障', '大数据应用支撑八个子体系', '大数据采集子体系', '大数据生命周期中',
#            '第一个环节', '整个技术体系', '数据引接技术支撑', '大数据存储', '大数据资源', '存储能力', '大数据处理', '分析', '应用',
#            '基础共性支撑', '大数据计算', '大数据分析', '大数据资源转换', '大数据价值信息获取', '大数据融合共享', '大数据资源流通支撑能力',
#            '大数据治理', '大数据高效管理能力', '大数据安全保障', '大数据全生命周期', '安全监管', '防护能力', '大数据应用支撑',
#            '大数据资源开发', '分析', '流通环境']
#
#     res = ['大数据技术体系', '大数据资源全生命周期流转', '典型状态']
#     link_entity_name_set = set(res)
#     link_entity_name_join_string = ""
#     for link_entity_name in link_entity_name_set:
#         link_entity_name_join_string += "'" + link_entity_name + "'" + ','
#     cypher1 = "match p=(a)-[*1..{}]->(b) where b.name in [{}] return p".format(2, link_entity_name_join_string[:-1])
#     result = tx.run(cypher1)
#     lst = []
#     for record in result:
#         print(record)
#         print(record['p'])
#         lst.append(record)
#     return lst
#
#
# with driver.session() as session:
#     res = session.read_transaction(find_doc_nodes)
#     print(type(res[0]))
#     print(res)
#
# driver.close()
