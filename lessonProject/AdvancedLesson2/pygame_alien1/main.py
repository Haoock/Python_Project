import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景  设置
    game_setting = Settings()
    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))  # 显示窗口，游戏的所有图形元素都将在其中绘制
    pygame.display.set_caption("Alien Invasion")  # 设置窗口的标题

    # 获取屏幕区域的位置坐标
    screen_rect = screen.get_rect()
    # 创建一艘飞船
    ship = Ship(screen)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件（事件循环）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 右移
                if event.key == pygame.K_RIGHT:
                    ship.ship_rect.centerx += 1
                elif event.key == pygame.K_LEFT:  # 左移
                    ship.ship_rect.centerx -= 1
        # 每次循环时都重绘屏幕
        screen.fill(game_setting.bg_color)

        # 将ship复制到screen上
        ship.ship_blip()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()

