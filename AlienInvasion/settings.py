# -*- coding: utf-8 -*-
# Created by: ZhaoDongshuang
# Created on: 18-1-29


class Settings:
    """存储设置信息"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)

        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_count_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移,为 -1 表示向左移
        self.fleet_direction = 1
