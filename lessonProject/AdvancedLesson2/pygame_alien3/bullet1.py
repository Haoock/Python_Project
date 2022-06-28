import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, setting, screen, ship):
        """在飞船所在的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        # 再设置正确的位置，子弹应该从飞船的顶端发射
        self.rect.centerx = ship.ship_rect.centerx
        self.rect.top = ship.ship_rect.top
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.color = setting.bullet_color

        # 增加子弹的飞行方向
        self.bullet_forward = True
        self.bullet_left = False
        self.bullet_right = False

    def update(self):
        """用于管理子弹的移动：需要向上移动子弹"""
        if self.bullet_forward:
            self.y -= 1
        # elif self.bullet_left:
        #     self.y -= 1
        #     self.x -= 1
        # elif self.bullet_right:
        #     self.y -= 1
        #     self.x += 1
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
