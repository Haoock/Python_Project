import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景  设置
    game_setting = Settings()
    screen = pygame.display.set_mode((game_setting.screen_width,
                                      game_setting.screen_height))  # 显示窗口，游戏的所有图形元素都将在其中绘制
    pygame.display.set_caption("Alien Invasion")  # 设置窗口的标题

    # 获取屏幕区域的位置坐标
    screen_rect = screen.get_rect()
    # 创建一艘飞船
    ship = Ship(screen)
    # 开始游戏的主循环
    while True:
        gf.event_handler(ship)
        ship.update()
        gf.update_screen(game_setting, screen, ship)


run_game()

