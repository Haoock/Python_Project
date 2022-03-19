import pygame
import sys
from bullet1 import Bullet
from alien1 import Alien


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


def update_bullets(setting, screen, ship, aliens, bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(setting, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(setting, screen, ship, aliens, bullets):
    # 检查是否有子弹击中了外星人，如果有则删除相应的子弹和外星人。
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        create_alien_group(setting, screen, ship, aliens)


"""创建外星人群"""


def create_alien_group(setting, screen, ship, aliens):
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    # 添加高度
    alien_height = alien.rect.height
    available_space_x = setting.screen_width - 2 * alien_width
    # 计算可用高度空间
    available_space_y = (setting.screen_height - (3 * alien_height) - ship.rect.height)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # 计算可以创建的行数
    number_rows = int(available_space_y / (2 * alien_height))
    # 创建多行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            alien = Alien(setting, screen)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            # alieny的位置
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            aliens.add(alien)


def check_alien_edges(setting, aliens):
    """外星人到达边缘的时候采取相应的措施"""
    for alien in aliens.sprites():
        # 如果某一个外星人到达了屏幕边缘，也要将整个外星人群整体下移。
        if alien.check_edges():
            change_alien_direction(setting, aliens)
            break


def change_alien_direction(setting, aliens):
    """将外星人整体下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += setting.alien_drop_speed
    setting.fleet_direction *= -1


def update_aliens(setting, screen, ship, aliens):
    """需要删除之前的update_aliens检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    check_alien_edges(setting, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        if setting.ship_left > 0:
            setting.ship_left -= 1
        else:
            setting.game_active = False
    check_aliens_bottom(setting, screen, aliens)


def check_aliens_bottom(setting, screen, aliens):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            if setting.ship_left > 0:
                setting.ship_left -= 1
            else:
                setting.game_active = False
