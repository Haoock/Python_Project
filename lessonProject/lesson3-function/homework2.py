def make_car(car_maker, type1, tow_package, color='red'):
    car_dic = {'car_maker': car_maker, 'type': type1, 'color': color, 'tow_package': tow_package}
    return car_dic


# 主程序
while True:
    car_maker_name = input("please enter a car maker name:")
    if car_maker_name == 'q':
        break
    type_name = input("Please enter a type name:")
    if type_name == 'q':
        break
    color_name = input("Please enter color name:")
    if color_name == 'q':
        break
    tow_package_name = input("What's tow_package(Ture or False):")
    if tow_package_name == 'q':
        break
    car = make_car(car_maker_name, type_name, tow_package=tow_package_name)
    print(car)

