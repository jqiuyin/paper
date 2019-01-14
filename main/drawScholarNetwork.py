'''
Created on 2019年1月13日

@author: qiuyin
'''

import networkx as nx
import matplotlib.pyplot as plt
import main.connectToAccess as source
from main.readScholarLabel import getScholarLabel
table=source.getData()
scholarLabel=getScholarLabel()

data=table[table[3].isin(scholarLabel)]
print(data)

G=nx.Graph()
  
for row in data[[1,4]].iterrows():
    #print(row[1][4])
    G.add_edge(str(row[1][1]), str(row[1][4]))
  
   
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=[9,9])







          
locations=nx.kamada_kawai_layout(G)
  
nx.draw_networkx(G, locations, node_size=[i[1]**1.3 for i in nx.degree(G)], with_labels=False)
plt.show()
