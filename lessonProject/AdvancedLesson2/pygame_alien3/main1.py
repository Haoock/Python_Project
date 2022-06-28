import sys
import pygame
from settings1 import Settings
from ship1 import Ship
import game_functions1_last_homework as gf
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
        # 编组进行更新，会自动对其中的每个子弹调用update 函数
        bullets.update()
        # 当子弹到达屏幕顶端的时候，删除子弹
        # 不能从列表或者编组中删除条目，必须遍历编组的副本。
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        # 每次循环都需要更新屏幕
        gf.update_screen(game_setting, screen, ship, bullets)


run_game()
