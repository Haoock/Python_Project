def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


while True:
    name = input("Please enter a pizza name!")
    make_pizza(name)
    if name == 'q':
        break
