import sys
import pygame
from settings2 import Settings
from ship2 import Ship
import game_functions2 as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景  设置
    game_setting = Settings()
    screen = pygame.display.set_mode((game_setting.screen_width,
                                      game_setting.screen_height))  # 显示窗口，游戏的所有图形元素都将在其中绘制
    pygame.display.set_caption("Alien Invasion")  # 设置窗口的标题
    ship = Ship(screen)
    # 创建一个用于存储子弹的编组,用于存储所有有效的子弹
    bullets = Group()
    while True:
        # 将bullet的所有设置传给gf
        # 在gf中设置和更新bullets
        gf.event_handler(game_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # 每次循环都需要更新屏幕
        gf.update_screen(game_setting, screen, ship, bullets)


run_game()
