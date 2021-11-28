class Gun:
    def __init__(self, bullet_num, clip_num, damage):
        self.bullet_num = bullet_num
        self.clip_num = clip_num
        self.damage = damage

    def print_Gun(self):
        print("伤害：", self.damage)
        print("当前弹夹剩余子弹：", self.bullet_num)
        print("备用弹夹数：", self.clip_num)


class SpecialGun(Gun):
    def __init__(self, gun_name, bullet_num, clip_num, damage, total_damage=0):
        super().__init__(bullet_num, clip_num, damage)
        self.gun_name = gun_name
        self.__total_bullet = bullet_num + clip_num * bullet_num
        self.total_damage = total_damage

    def print_Gun(self):
        print("枪的名称：", self.gun_name)
        print("总伤害为：", self.total_damage)
        super().print_Gun()

    def fire(self, bullet_num, hit_num):
        if self.__total_bullet < bullet_num:
            print("提示：子弹不够")
            self.bullet_num = 0
        else:
            self.__total_bullet -= bullet_num
            # 还剩几个弹夹的子弹：
            self.clip_num = self.__total_bullet // self.bullet_num
            # 当前弹夹剩下的子弹如下：
            self.bullet_num = self.__total_bullet % self.bullet_num
        self.total_damage = self.damage * hit_num


Ak47 = SpecialGun("Ak47", 30, 3, 30)
pistal = SpecialGun("沙漠之鹰", 7, 5, 40)
Ak47.fire(62, 2)
Ak47.print_Gun()
pistal.fire(9, 1)
print("*" * 50)
pistal.print_Gun()
