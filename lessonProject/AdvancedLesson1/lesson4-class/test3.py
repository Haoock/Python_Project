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
        print("开始打印")
        print(self.brand, self.model, self.year)

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has %d miles on it." %self.odometer_reading)

    def increment_odometer(self,miles):
        self.odometer_reading += miles

        
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    #后面再定义一个方法来指出电瓶的续航里程
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """ 初始化父类的属性，再初始化电动汽车特有的属性 """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()

# 最后再通过电池的容量来得出续航里程
my_tesla.battery.get_range()
