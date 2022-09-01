import json

with open("./files/index.json", 'r') as indexFile:
    js = json.load(indexFile)  # json.load是将json文件打开，将字符串变换成字典类型
    print(js)
    print(type(js))
    # 下面是得到reply
    reply_dict = js.get("reply", {})
    cm_dict = reply_dict.get("codemodel-v2", {})
    print(cm_dict)
    jsonFile = cm_dict.get("jsonFile", "")
    print(jsonFile)

with open("./files/codemodel.json", 'r') as codemodel:
    cm = json.load(codemodel)
    print(cm)
    paths_dict = cm.get("paths", {})
    print(paths_dict)
    configs_arr = cm.get("configurations", [])
    for cfg_dict in configs_arr:
        print(cfg_dict)




