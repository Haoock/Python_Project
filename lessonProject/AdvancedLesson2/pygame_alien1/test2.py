import sys
import pygame


# load image
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景  设置
    screen = pygame.display.set_mode((1200, 800))  # 显示窗口，游戏的所有图形元素都将在其中绘制
    pygame.display.set_caption("Alien Invasion")  # 设置窗口的标题
    # 设置背景色
    bg_color = (230, 230, 230)
    # 导入图片
    ship = pygame.image.load("ship.bmp")
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件（事件循环）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 每次循环时都重绘屏幕
        screen.fill(bg_color)
        # 将ship复制到screen上
        screen.blit(ship, [0, 0])

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
