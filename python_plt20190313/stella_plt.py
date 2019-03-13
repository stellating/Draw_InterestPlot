#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 设置横纵坐标的名称以及对应字体格式
font1 = {'family': 'Times New Roman',
         'weight': 'heavy',
         'size': 20,
         }
plt.rc('font', **font1)  # pass in the font dict as kwargs
    # 设置title和x，y轴的label
f=open('fpsforstella.csv','r')
line = f.readline()
listX = []
listY = []
listName = []
while line:
	a = line.split(',')
	name = a[0]
	X = float(a[1])
	Y = float(a[2])
	listName.append(name)
	listX.append(X) # 将其添加在列表之中
	listY.append(Y)
	line = f.readline()
f.close()
print(listX)
print(listY)
X_data = listX
Y_data = listY

#print(type(X_data))

N = len(X_data)
#colors = np.random.rand(N) # 随机产生50个0~1之间的颜色值
#col=['c', 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
col=['c', 'b', 'g', 'r', 'c', 'm', 'y', 'k'] #边界颜色不能设为白色，否则会看不到
len_col = len(col)
#area = np.pi * (10 * np.random.rand(N))**2  # 点的半径范围:0~15

#markers_market=['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x', 'X', 'D', 'd', '|', '_']
markers_market=['.', ',', 'o', 'v', '^', '<', '>', '8', 's', 'p', 'P', '*', 'h', 'H', 'D', 'd'] #剔除那些没有边界的markers
len_markers = len(markers_market)
#print(np.random.randint(len_markers))
#print(markers_market[0])
#markers_market[np.random.randint(len_markers)] #[0,len_markers)

# for i in range(len(X_data)):
p1 = plt.scatter(X_data[0], Y_data[0], c='',s=200, alpha=1, marker=markers_market[1],edgecolors=col[0],linewidths=2, label='ACT')

p2 = plt.scatter(X_data[1], Y_data[1], c='',s=200, alpha=1, marker=markers_market[2],edgecolors=col[1],linewidths=2, label='MDNET')

p3 = plt.scatter(X_data[2], Y_data[2], c='',s=200, alpha=1, marker=markers_market[3],edgecolors=col[2],linewidths=2, label='ADNET')

p4 = plt.scatter(X_data[3], Y_data[3], c='',s=200, alpha=1, marker=markers_market[4],edgecolors=col[7],linewidths=2 , label='meta-sdnet')

p5 = plt.scatter(X_data[4], Y_data[4], c='',s=200, alpha=1, marker=markers_market[5],edgecolors=col[4],linewidths=2 , label='meta-crest')

p6 = plt.scatter(X_data[5], Y_data[5], c='',s=200, alpha=1, marker=markers_market[6],edgecolors=col[0],linewidths=2 , label='VITAL')

p7 = plt.scatter(X_data[6], Y_data[6], c='',s=200, alpha=1, marker=markers_market[7],edgecolors=col[6],linewidths=2 , label='siamFC')

p8 = plt.scatter(X_data[7], Y_data[7], c='',s=200, alpha=1, marker=markers_market[8],edgecolors=col[2],linewidths=2, label='MCCT')

p9 = plt.scatter(X_data[8], Y_data[8], c='',s=200, alpha=1, marker=markers_market[9],edgecolors=col[3],linewidths=2, label='CRAC-MDNet')

p10 = plt.scatter(X_data[9], Y_data[9], c='',s=200, alpha=1, marker=markers_market[10],edgecolors=col[1],linewidths=2 , label='SiamRPN')

p11 = plt.scatter(X_data[10], Y_data[10], c='',s=200, alpha=1, marker=markers_market[12],edgecolors=col[3],linewidths=2 , label='CRAC-Siam')

plt.legend(loc='lower right' ,ncol=3,fontsize=14)  #设置图例，分为3列展示

  #plt.scatter(X_data[i], Y_data[i], s=200, alpha=1, marker=markers_market[np.random.randint(len_markers)],edgecolors=col[np.random.randint(len_col)])





maxX = max(X_data)
minX = min(X_data)

maxY = max(Y_data)
minY = min(Y_data)
plt.xlim(minX-0.2, maxX+10)
plt.ylim(minY-5, maxY+5)
plt.axis()
plt.grid(linestyle='--')


plt.title("AUC for OPE and FPS")
plt.xlabel("FPS")
plt.ylabel("AUC for OPE")



#获得坐标轴的句柄
ax=plt.gca();
plt.xscale('symlog')
x = (0,1,2,4,6,8,10,20,40,60)
plt.xticks(x)
ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())

# 设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=15,width=2,bottom=True,top=True,left=True,right=True,direction='in')
tick_labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in tick_labels]

###设置坐标轴的粗细

ax.spines['bottom'].set_linewidth(2);
###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(2);
####设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(2);
###设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(2);
####设置上部坐标轴的粗细


plt.subplots_adjust(top=0.9,bottom=0.1,left=0.1,right=1,hspace=0,wspace=0) #设置存储时白边问题
plt.margins(0,0)

    # 保存图片到指定路径
plt.savefig("lalala3.png")
    # 展示图片 *必加
plt.show()
