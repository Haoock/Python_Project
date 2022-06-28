import pygame
import sys
from bullet1 import Bullet


# 增加飞船向上和向下移动的功能
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
                # if len(bullets) < setting.bullets_allowed:
                #     new_bullet = Bullet(setting, screen, ship)
                #     bullets.add(new_bullet)
                # 当按下空格的时候创建一颗子弹
                new_bullet = Bullet(setting, screen, ship)
                # 之后将其加入到编组bullets中
                # new_bullet.bullet_left = False
                # new_bullet.bullet_right = False
                new_bullet.bullet_forward = True
                bullets.add(new_bullet)
            elif event.key == pygame.K_UP:
                ship.move_up = True
            elif event.key == pygame.K_DOWN:
                ship.move_down = True
            # elif event.key == pygame.K_a:
            #     new_bullet = Bullet(setting, screen, ship)
            #     # 之后将其加入到编组bullets中
            #     new_bullet.bullet_left = True
            #     new_bullet.bullet_right = False
            #     new_bullet.bullet_forward = False
            #     bullets.add(new_bullet)
            # elif event.key == pygame.K_d:
            #     new_bullet = Bullet(setting, screen, ship)
            #     # 之后将其加入到编组bullets中
            #     new_bullet.bullet_left = False
            #     new_bullet.bullet_right = True
            #     new_bullet.bullet_forward = False
            #     bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:
                ship.move_left = False
            elif event.key == pygame.K_UP:
                ship.move_up = False
            elif event.key == pygame.K_DOWN:
                ship.move_down = False


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
