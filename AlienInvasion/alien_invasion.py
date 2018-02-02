# -*- coding: utf-8 -*-
# Created by: ZhaoDongshuang
# Created on: 18-1-29

import pygame

from pygame.sprite import Group

from AlienInvasion.scoreboard import Scoreboard
from AlienInvasion.settings import Settings
from AlienInvasion.ship import Ship
from AlienInvasion.game_stats import GameStats
from AlienInvasion.button import Button


import AlienInvasion.game_functions as game_functions


def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    bullets = Group()

    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # 创建存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # 创建 Play 按钮
    play_button = Button(ai_settings, screen, "Play")

    while True:
        game_functions.check_events(ai_settings, screen, stats, scoreboard,
                                    play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            game_functions.update_bullets(ai_settings, screen, stats,
                                          scoreboard, ship, aliens, bullets)
            game_functions.update_aliens(ai_settings, stats, scoreboard, screen,
                                         ship, aliens, bullets)

        game_functions.update_screen(ai_settings, screen, stats, scoreboard,
                                     ship, aliens, bullets, play_button)


run_game()

