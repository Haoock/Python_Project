import pygame
import sys
from bullet2 import Bullet


def event_handler(setting, screen, ship, bullets):
    # 处理鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 右移
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
            elif event.key == pygame.K_LEFT:  # 左移
                ship.move_left = True
            elif event.key == pygame.K_SPACE:
                # 当按下空格的时候创建一颗子弹
                new_bullet = Bullet(setting, screen, ship)
                # 之后将其加入到编组bullets中
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:
                ship.move_left = False


def update_screen(settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都绘制新屏幕
    screen.fill(settings.bg_color)
    # 需要在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.ship_blip()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
