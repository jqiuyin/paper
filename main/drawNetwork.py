'''
Created on 2019年2月18日

@author: qiuyin
'''
import networkx as nx
import matplotlib.pyplot as plt
import main.connectToAccess as source
from main.readLabel import getScholarLabel
from main.createGraph import CreateGraph
table=source.getData()
Network=CreateGraph(table)
G=Network.getGraph()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure() 
nx.draw_networkx(G)
plt.show()