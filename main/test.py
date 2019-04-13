'''
Created on 2019年3月31日

@author: qiuyin
'''
import matplotlib.pyplot as plt
import main.connectToAccess as source
from main.readLabel import getScholarLabel
from main.readLabel import getPoliticalLable
from main.createGraph import CreateGraph
import main.cleanData as cd
import main.drawNetwork as dn
import importlib

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dynasties={
    '唐':[618,907],
    '宋':[960,1279],
    '元':[1279,1367],
    '明':[1368,1644],
    '清':[1644,1911]
}
font_size=0.3
fig=plt.figure(figsize=(9,4))
poltList=[]
for i in range(1,3):
    poltList.append(fig.add_subplot(1,2,i))
importlib.reload(dn)
i=0
value = dynasties['清']
table=source.getData(start=value[0],end=value[1])
scholarLabel=getScholarLabel()
cleanData=cd.CleanData(label=scholarLabel,table=table)
data=cleanData.get_table()
scholarNetwork=CreateGraph(data)
G=scholarNetwork.getGraph()
drawNetwork=dn.DrawNetwork(poltList[i],G,font_size=font_size)
drawNetwork.draw()
i=i+1
politicalLabel=getPoliticalLable()
cleanData=cd.CleanData(label=politicalLabel,table=table)
data=cleanData.get_table()
politicalNetwork=CreateGraph(data)
G=politicalNetwork.getGraph()
drawNetwork=dn.DrawNetwork(poltList[i],G,font_size=font_size)
drawNetwork.draw()
i+1
plt.show()