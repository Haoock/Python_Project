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

    def ship_blip(self):
        self.screen.blit(self.ship, self.ship_rect)
