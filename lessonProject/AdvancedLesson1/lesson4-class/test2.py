# Car类和ElectricCar类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, brand, model, year):
        """初始化描述汽车的属性"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """打印整洁的描述性信息"""
        print(self.brand, self.model, self.year)

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has %d miles on it." % self.odometer_reading)

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("%s Gas ")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70  # 电动车的电池容量

    def describe_battery(self):
        """描述电动车电池容量的方法"""
        print("This car has %d -KWh battery" % self.battery_size)


# 普通汽车
my_used_car = Car('Audi', 'A4', "2020")
my_used_car.get_descriptive_name()
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# 电动汽车
my_tesla = ElectricCar('Tesla', 'Model S', 2017)
my_tesla.get_descriptive_name()
my_tesla.describe_battery()
