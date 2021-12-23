import sys
import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景  设置
    screen = pygame.display.set_mode((1200, 800))  # 显示窗口，游戏的所有图形元素都将在其中绘制
    pygame.display.set_caption("Alien Invasion")  # 设置窗口的标题
    # 设置背景色的该变量
    i = 0
    j = 0
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件（事件循环）
        for event in pygame.event.get():
            print("检查程序中的事件")
            if event.type == pygame.KEYUP:
                print("程序安全退出！")
                pygame.quit()
                sys.exit()

        # 设置背景颜色并让其变化
        # bg_color = (i, j, 230)
        # i += 1
        # j += 1
        # if i > 255:
        #     i = 0
        # if j > 255:
        #     j = 0
        bg_color = (255, 0, 0)
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
