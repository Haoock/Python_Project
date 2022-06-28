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
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 外星人x的准确位置
        self.x = float(self.rect.x)

    def alien_blip(self):
        self.screen.blit(self.image, self.rect)


