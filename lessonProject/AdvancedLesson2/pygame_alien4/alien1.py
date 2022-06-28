# -*- coding: utf-8 -*-
# @Author  : Haock
# @Time    : 2021/12/30 1:57 下午
# @Function: Alien类
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, setting, screen):
        super(Alien, self).__init__()
        self.setting = setting
        self.screen = screen

        # 导入图片
        self.image = pygame.image.load('../pygame_alien3/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 外星人x的准确位置
        self.x = float(self.rect.x)

    def alien_blip(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # self.x += self.setting.alien_speed
        # 外星人向左移动或者向右移动
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


