import pygame
import sys
from bullet2 import Bullet
from alien4 import Alien


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
                if len(bullets) < setting.bullets_allowed:
                    new_bullet = Bullet(setting, screen, ship)
                    bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:
                ship.move_left = False


def update_screen(settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都绘制新屏幕
    screen.fill(settings.bg_color)
    # 需要在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.ship_blip()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))


"""创建外星人群"""


def create_alien_group(setting, screen, aliens):
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    available_space_x = setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        # 创建一个外星人并将其加入当前行
        alien = Alien(setting, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

