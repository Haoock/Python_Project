class Settings():
    # 开始添加子弹模块
    def __init__(self):
        # 游戏初始化设置
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 子弹的设置,创建
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # # 子弹的数量
        self.bullets_allowed = 5
        # 添加外星人的速度
        self.alien_speed = 1
        self.alien_drop_speed = 30
        # drop_speed表示外星人碰撞到屏幕边缘时，外星人群向下移动的距离
        # fleet_direction  为1表示右移，为-1表示左移
        self.fleet_direction = 1

        # 限制只存在一条飞船
        self.ship_left = 0
        # 游戏的状态
        self.game_active = True
