'''
Created on 2019年2月18日

@author: qiuyin
'''

import matplotlib.pyplot as plt
import pandas as pd


data={"唐":[0,0,0],
     "宋":[34,26,24],
     "元":[27,22,3],
     "明":[30,25,12],
     "清":[2,2,0]}
frame=pd.DataFrame(data,index=['度中心性','中介中心性','接近中心性'])

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(frame["唐"],marker='s',linestyle="--")
ax.plot(frame["宋"],marker='o',linestyle="--")
ax.plot(frame["元"],marker='^',linestyle="--")
ax.plot(frame["明"],marker='*',linestyle="--")
ax.plot(frame["清"],marker='+',linestyle="--")
ax.legend(loc="best")
plt.show()
