import os
import sys
import pygame

# 使窗口居中
os.environ["SDL_VIDEO_CENTERED"] = "1"
# os.environ["SDL_VIDEO_WINDOW_POS"] = "1664, 300"

# MyGame 默认值
GAME_NAME = "My Game"
SCREEN_SIZE = 640, 480
DISPLAY_MODE = pygame.HWSURFACE | pygame.DOUBLEBUF
LOOP_SPEED = 60
FONT_NAME = "../../resources/Minecraft.ttf"
FONT_SIZE = 16
KEY_PAUSE = pygame.K_PAUSE


class MyGame(object):

    def __init__(self, **kwargs):
        pygame.init()
        pygame.mixer.init()
        self.game_name = kwargs.get("game_name") or GAME_NAME
        pygame.display.set_caption(self.game_name)
        self.screen_size = kwargs.get("screen_size") or SCREEN_SIZE
        self.screen_width, self.screen_height = self.screen_size
        self.display_mode = kwargs.get("display_mode") or DISPLAY_MODE
        self.icon = kwargs.get("icon") or None
        self.icon and pygame.display.set_icon(pygame.image.load(self.icon))
        self.screen = pygame.display.set_mode(self.screen_size,
                                              self.display_mode)
        self.loop_speed = kwargs.get("loop_speed") or LOOP_SPEED
        self.font_name = kwargs.get("font_name") or FONT_NAME
        self.font_size = kwargs.get("font_size") or FONT_SIZE
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.clock = pygame.time.Clock()
        self.now = 0
        self.background = pygame.Surface(self.screen_size)

        self.key_bindings = {}                      # 按键与函数绑定字典
        self.add_key_binding(KEY_PAUSE, self.pause)

        self.game_actions = {}                      # 游戏数据更新动作

        self.draw_actions = [self.draw_background]  # 画面更新动作列表

        self.running = True
        self.draw = pygame.draw

    def run(self):
        """主循环"""
        while True:
            self.now = pygame.time.get_ticks()
            self.process_events()
            if self.running:
                self.update_gamedata()
            self.update_display()
            self.clock.tick(self.loop_speed)

    def pause(self):
        """暂停游戏"""
        self.running = not self.running
        if self.running:
            for action in self.game_actions.values():
                if action["next_time"]:
                    action["next_time"] = self.now + action["interval"]

    def process_events(self):
        """事件处理"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                action, kwargs = self.key_bindings.get(event.key, (None, None))
                action(**kwargs) if kwargs else action() if action else None

    def update_gamedata(self):
        """更新游戏数据"""
        for action in self.game_actions.values():
            if not action["next_time"]:
                action["run"]()
            elif self.now >= action["next_time"]:
                action["next_time"] += action["interval"]
                action["run"]()

    def update_display(self):
        """更新画面显示"""
        for action in self.draw_actions:
            action()
        pygame.display.flip()

    def draw_background(self):
        """绘制背景"""
        self.screen.blit(self.background, (0, 0))

    def add_key_binding(self, key, action, **kwargs):
        """增加按键绑定"""
        self.key_bindings[key] = action, kwargs

    # TODO: 更新动作若有次序要求，则用字典保存不合适
    def add_game_action(self, name, action, interval=0):
        """添加游戏数据更新动作"""
        next_time = self.now + interval if interval else None
        self.game_actions[name] = dict(run=action,
                                       interval=interval,
                                       next_time=next_time)

    def add_draw_action(self, action):
        """添加画面更新动作"""
        self.draw_actions.append(action)

    def draw_text(self, text, loc, color, bgcolor=None):
        if bgcolor:
            surface = self.font.render(text, True, color, bgcolor)
        else:
            surface = self.font.render(text, True, color)
        self.screen.blit(surface, loc)

    def draw_cell(self, xy, size, color1, color2=None):
        x, y = xy
        rect = pygame.Rect(x * size, y * size, size, size)
        self.screen.fill(color1, rect)
        if color2:
            self.screen.fill(color2, rect.inflate(-4, -4))

    def quit(self):
        """退出游戏"""
        pygame.quit()
        sys.exit(0)


if __name__ == '__main__':
    MyGame().run()