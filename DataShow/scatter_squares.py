# *- coding: utf-8 -*
# Created by: ZhaoDongshuang
# Created on: 2018/2/4

import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 自定义颜色
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# plt.scatter(x_values, y_values, c=(0, 0.8, 0.8), edgecolor='none', s=40)

# 使用颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 自动保存图表
# 第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，可省略这个实参
# plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()
