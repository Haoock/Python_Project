class Settings():
    # 开始添加子弹模块
    def __init__(self):
        # 游戏初始化设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 子弹的设置,创建
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # # 子弹的数量
        self.bullets_allowed = 5
