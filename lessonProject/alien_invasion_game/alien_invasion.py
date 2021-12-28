# 导入pygame模块
import pygame, sys
from settings import Settings
from ship import Ship


def run_game():
    # 初始化pygame
    pygame.init()
    # 使用Settings类
    ai_settings = Settings()
    # 创建一个窗口，我们将在这个窗口里显示游戏元素
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(screen)

    # 程序主循环
    while True:
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # 获取事件
        for event in pygame.event.get():
            # 判断是否为退出事件
            if event.type == pygame.QUIT:
                # 退出pygame
                pygame.quit()
                sys.exit()
        # 绘制屏幕内容
        pygame.display.flip()


run_game()
