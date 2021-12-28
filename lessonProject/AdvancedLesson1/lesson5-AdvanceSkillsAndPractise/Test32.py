def addNum(x, y):
    return x + y


def subNum(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# 用于判断是否是运算符，如果是则返回True，如果不是则返回False
def isOperator(opt):
    if opt == "+" or opt == "-" or opt == "*" or opt == "/":
        return True
    else:
        return False


while True:
    str_input = input("请输入算式：")
    if str_input == "!":
        print("程序结束")
        break
    inputNum1 = ""  # 运算符左边的数字
    inputNum2 = ""  # 运算符右边的数字
    operator = ""

    flag = False  # 这个Flag用于判断是运算符左边的数字还是运算符右边的数字
    for i in range(len(str_input)):
        if flag == False and isOperator(str_input[i]) == False:  # left Num
            inputNum1 += str_input[i]
        elif flag == False and isOperator(str_input[i]) == True:
            operator = str_input[i]
            flag = True
        elif flag == True and isOperator(str_input[i]) == False:  # right Num
            inputNum2 += str_input[i]
    inputNum1 = int(inputNum1)
    inputNum2 = int(inputNum2)
    if operator == "+":
        numSum = addNum(inputNum1, inputNum2)
    elif operator == "-":
        numSum = subNum(inputNum1, inputNum2)
    elif operator == "*":
        numSum = multiply(inputNum1, inputNum2)
    elif operator == "/":
        numSum = divide(inputNum1, inputNum2)
    print("计算结果为：%d" % numSum)
