# 使飞船能够左右移动
import pygame
import sys

# 练习或者作为Homework
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
    # 设置左移标记位，默认为True，不左移动
    ship_move_left = False
    while True:
        # 监视键盘和鼠标事件（事件循环）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship_move_right = True
                elif event.key == pygame.K_LEFT:
                    ship_move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship_move_right = False
                elif event.key == pygame.K_LEFT:
                    ship_move_left = False

        # 放飞船超过屏幕边界时候就停止
        if ship_move_right and ship_rect.right < screen_rect.right:
            ship_rect.centerx += 1
        if ship_move_left and ship_rect.left > 0:
            ship_rect.centerx -= 1
        screen.fill(bg_color)
        screen.blit(ship, ship_rect)
        pygame.display.flip()


run_game()

