import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形像处理矩形一样处理游戏元素
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 调整游戏元素的水平或垂直位置， 可使用属性x和y，它们分别是相应矩形左上角的x和y坐标。
        # 要将游戏元素居中，可设置相应rect对象的属性center、centerx或centery。
        # 要让游戏元素 与屏幕边缘对齐，可使用属性top、bottom、left或right;
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 飞船中心的x坐标
        self.rect.bottom = self.screen_rect.bottom  # 飞船下边缘的y坐标

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            # 更新飞船的center值，而不是rect
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            # 更新飞船的center值，而不是rect
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
