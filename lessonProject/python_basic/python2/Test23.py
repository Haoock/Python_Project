import math
def caculate_Area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("面积：%d" %area)
    else:
        print("不能构成三角形")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
caculate_Area(a, b, c)
