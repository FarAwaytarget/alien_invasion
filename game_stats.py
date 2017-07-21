class GameStats():
    """docstring for FameStats."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # 让游戏一开始处于非活动状态
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        # initialization game running maybe statistics message
        self.score = 0
        self.ships_left = self.ai_settings.ship_limit
