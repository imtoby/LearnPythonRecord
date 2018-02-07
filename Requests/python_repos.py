# -*- coding: utf-8 -*-
# Created by: ZhaoDongshuang
# Created on: 18-2-6

import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行 API 调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
# 将 API 响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
# 探索有关仓库的信息
repo_dicts = response_dict['items']

# ################## example01 ##################
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # 可视化
# my_style = LS('#333366', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
# chart.add('', stars)
# chart.render_to_file('python_repos.svg')
# ################## example01 ##################

# ################## example02 ##################
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # 可视化
# my_style = LS('#333366', base_style=LCS)
# my_config = pygal.Config()                  # 用于定制图表的外观
# my_config.x_label_rotation = 45             # 标签绕 x 轴旋转 45 度
# my_config.show_legend = False               # 隐藏图例
# my_config.title_font_size = 24              # 设置图表标题的字体大小
# my_config.label_font_size = 14              # 设置图副标签的字体大小
# my_config.major_label_font_size = 18        # 设置主标签的字体大小
# my_config.truncate_label = 15               # 仅显示 15 个字符
# my_config.show_y_guides = False             # 隐藏图表中的水平线
# my_config.width = 1000                      # 设置自定义宽度
#
# chart = pygal.Bar(my_config, style=my_style)
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
#
# chart.add('', stars)
# chart.render_to_file('python_repos.svg')
# ################## example02 ##################


print("Number of items:", len(repo_dicts))


def stargazers_count(repo_dict_json):
    return repo_dict_json['stargazers_count']


def description(repo_dict_json):
    description_str = repo_dict_json['description']
    if description_str:
        return description_str
    else:
        return ""


names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': stargazers_count(repo_dict),
        'label': description(repo_dict),
        'xlink': str(repo_dict['html_url']),
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()                  # 用于定制图表的外观
my_config.x_label_rotation = 45             # 标签绕 x 轴旋转 45 度
my_config.show_legend = False               # 隐藏图例
my_config.title_font_size = 24              # 设置图表标题的字体大小
my_config.label_font_size = 14              # 设置图副标签的字体大小
my_config.major_label_font_size = 18        # 设置主标签的字体大小
my_config.truncate_label = 15               # 仅显示 15 个字符
my_config.show_y_guides = False             # 隐藏图表中的水平线
my_config.width = 1000                      # 设置自定义宽度

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
