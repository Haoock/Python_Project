import pygame


class Ship():
    def __init__(self, screen):
        " 初始化飞船 "
        self.screen = screen

        # 导入图片
        self.ship = pygame.image.load("ship.bmp")
        self.ship_rect = self.ship.get_rect()
        self.screen_rect = screen.get_rect()
        #  设置ship的位置为screen的中间底部
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.move_right = False
        self.move_left = False

    def update(self):
        """根据移动标志来调整飞船的位置"""
        # 通过标志位并且还要限制飞船的位置
        if self.move_right and self.ship_rect.right < self.screen_rect.right:
            self.ship_rect.centerx += 1
        if self.move_left and self.ship_rect.left > 0:
            self.ship_rect.centerx -= 1

    def ship_blip(self):
        self.screen.blit(self.ship, self.ship_rect)
