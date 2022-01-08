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
        self.scrren = screen




