# -*- coding: utf-8 -*-
# Created by: ZhaoDongshuang
# Created on: 18-2-5

import csv

from datetime import datetime
from matplotlib import pyplot as plt


# 从文件中获取日期、最高气温和最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# 给图表区域着色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


# example 02 start
# # 从文件中获取日期和最高气温
# filename = 'sitka_weather_2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     dates, highs = [], []
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#
#         high = int(row[1])
#         highs.append(high)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red')
#
# # 设置图形的格式
# plt.title("Daily high temperatures - 2014", fontsize=24)
# plt.xlabel('', fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.show()
# example 02 end


# example 01 start
# # 从文件中获取最高气温
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     # print(header_row)
#     # 打印每个元素的索引及其值
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
#
#     highs = []
#     for row in reader:
#         high = int(row[1])
#         highs.append(high)
#     # print(highs)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(highs, c='red')
#
# # 设置图形的格式
# plt.title("Daily high temperatures, July 2014", fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.show()
# example 01 end


