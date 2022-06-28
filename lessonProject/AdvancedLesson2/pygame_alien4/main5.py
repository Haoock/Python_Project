import sys
import pygame
from settings5 import Settings
from ship1 import Ship
import game_functions5 as gf
from alien1 import Alien
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景  设置
    game_setting = Settings()
    screen = pygame.display.set_mode((game_setting.screen_width,
                                      game_setting.screen_height))  # 显示窗口，游戏的所有图形元素都将在其中绘制
    pygame.display.set_caption("Alien Invasion")  # 设置窗口的标题
    ship = Ship(screen)
    alien = Alien(game_setting, screen)
    bullets = Group()
    aliens = Group()
    gf.create_alien_group(game_setting, screen, ship, aliens)
    # 创建
    while True:
        # 将bullet的所有设置传给gf
        # 在gf中设置和更新bullets
        gf.event_handler(game_setting, screen, ship, bullets)
        if game_setting.game_active:
            ship.update()
            gf.update_bullets(game_setting, screen, ship, aliens, bullets)
            # 更新外星人的位置
            gf.update_aliens(game_setting, screen, ship, aliens)
        gf.update_screen(game_setting, screen, ship, aliens, bullets)


run_game()
