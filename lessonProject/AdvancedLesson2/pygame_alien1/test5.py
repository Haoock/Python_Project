import pygame
import sys


# keyboardEventLearn

def run_game():
    pygame.init()
    screen = pygame.display.set_mode([1200, 800])
    pygame.display.set_caption("Alien Invasion")  # 设置窗口的标题
    ship = pygame.image.load("ship.bmp")
    bg_color = (230, 230, 230)
    screen_rect = screen.get_rect()
    ship_rect = ship.get_rect()
    ship_rect.centerx = screen_rect.centerx
    ship_rect.bottom = screen_rect.bottom
    # 设置右移标记位，默认为False，不右移
    ship_move_right = False
    while True:
        # 监视键盘和鼠标事件（事件循环）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship_move_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship_move_right = False

        # 如果右移位为True，则不断向右边移动
        # if ship_move_right:
        #     ship_rect.centerx += 1

        # 放飞船超过屏幕边界时候就停止
        if ship_move_right and ship_rect.right < screen_rect.right:
            ship_rect.centerx += 1
        screen.fill(bg_color)
        screen.blit(ship, ship_rect)
        pygame.display.flip()


run_game()
