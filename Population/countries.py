# -*- coding: utf-8 -*-
# Created by: ZhaoDongshuang
# Created on: 18-2-5

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
