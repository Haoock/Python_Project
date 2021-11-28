pclub = ["王一凡","邓中正","谢宇翔","王启瑞","张永泰","史可兮"]
bclub = ["刘天义","郑传浩","刘思恬","谢宇翔"]

"""
finalclub = []
finalclub.extend(pclub)
finalclub.extend(bclub)
"""
finalclub = pclub + bclub
print(finalclub)
finalclub = set(finalclub)
print(finalclub)
print(list(finalclub))



