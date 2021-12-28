filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("文件不存在！")
else:
    print("....")
    
















'''
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

'''
