# 导入pygame模块
import pygame, sys
# 初始化pygame
pygame.init()
# 创建一个窗口，我们将在这个窗口里显示游戏元素
screen = pygame.display.set_mode([1200, 800])

# 程序主循环
while True:
    # 获取事件
    for event in pygame.event.get():
        # 判断是否为退出事件
        if event.type == pygame.QUIT:
            # 退出pygame
            pygame.quit()
            sys.exit()
    # 绘制屏幕内容
    pygame.display.flip()
