'''
Created on 2019年1月13日

@author: qiuyin
'''

import networkx as nx
import matplotlib.pyplot as plt
import main.connectToAccess as source
from main.readLabel import getScholarLabel
from main.createGraph import CreateGraph
table=source.getData()
scholarLabel=getScholarLabel()

data=table[table[3].isin(scholarLabel)]

scholarNetwork=CreateGraph(data)



G=scholarNetwork.getGraph()
# print(nx.number_of_selfloops(G))
gG=nx.k_core(G, k=4)
#gG=G
edgesList=list(gG.edges())
    
    
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=[9,9])
locations=nx.kamada_kawai_layout(G)

nx.draw_networkx_edges(gG, locations, edgelist=edgesList,width=0.3, edge_color='r', alpha=0.4)
#nx.draw_networkx_nodes(gG, locations,node_color='g', node_size=[i[1]**1.3 for i in nx.degree(gG)],alpha=0.8)
nx.draw_networkx_nodes(gG, locations,node_color='g', node_size=10,alpha=0.8)
for people in nx.degree(gG):
    location=locations.get(people[0])
    #print(location)
    nx.draw_networkx_labels(gG, pos={people[0]:location},labels={people[0]:people[0]}, font_size=10)
# nx.draw_networkx(G,pos=locations,with_labels=False,node_size=[i[1] for i in nx.degree(G)])


plt.show()
