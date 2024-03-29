# coordinates
import sys
import pygame


def run_game():
    # 初始化pygame
    pygame.init()
    # 设置屏幕大小
    screen = pygame.display.set_mode([800, 600])
    # 设置窗口的标题
    pygame.display.set_caption("Alien Invasion")
    # 加载图片
    ship = pygame.image.load("ship.bmp")
    # 设置背景颜色
    bg_color = (230, 230, 230)
    # 获取screen的区域坐标位置
    screen_rect = screen.get_rect()
    # 获取ship的区域坐标位置
    ship_rect = ship.get_rect()
    # 设置ship的位置为screen的中间底部
    ship_rect.centerx = screen_rect.centerx
    ship_rect.bottom = screen_rect.bottom
    while True:
        # 监视键盘和鼠标事件（事件循环）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(bg_color)
        screen.blit(ship, ship_rect)
        pygame.display.flip()


run_game()
