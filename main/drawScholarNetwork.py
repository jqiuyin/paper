'''
Created on 2019年1月13日

@author: qiuyin
'''

import networkx as nx
import matplotlib.pyplot as plt
import main.connectToAccess as source
from main.readScholarLabel import getScholarLabel
from main.createGraph import createGraph
table=source.getData()
scholarLabel=getScholarLabel()

data=table[table[3].isin(scholarLabel)]

scholarNetwork=createGraph(data)



G=scholarNetwork.getGraph()
edgesList=scholarNetwork.getEdgesList()


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=[9,9])
locations=nx.kamada_kawai_layout(G)

nx.draw_networkx_edges(G, locations, edgelist=edgesList,width=0.3, edge_color='r', alpha=0.4)
nx.draw_networkx_nodes(G, locations,node_color='g', node_size=[i[1]**1.3 for i in nx.degree(G)],alpha=0.8)
for people in nx.degree(G):
    location=locations.get(people[0])
    #print(location)
    nx.draw_networkx_labels(G, pos={people[0]:location},labels={people[0]:people[0]}, font_size=people[1]**0.5)
# nx.draw_networkx(G,pos=locations,with_labels=False,node_size=[i[1] for i in nx.degree(G)])


plt.show()
