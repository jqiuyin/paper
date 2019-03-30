import networkx as nx
import matplotlib.pyplot as plt
from main.createGraph import CreateGraph
from main.cleanData import CleanData
politicalNetwork=CreateGraph()
data=CleanData()
politicalNetwork=CreateGraph()
G=politicalNetwork.getGraph()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=[9,9])  
# edgelist = list(G.edges())
# print(edgelist)
gG=nx.k_core(G, k=3)
locations=nx.kamada_kawai_layout(gG)
edgesList=list(gG.edges())
 
nx.draw_networkx_edges(gG, locations, edgelist=edgesList,width=0.3, edge_color='r', alpha=0.4)
nx.draw_networkx_nodes(gG, locations,node_color='g', node_size=[i[1]**1.3 for i in nx.degree(gG)],alpha=0.8)
for people in nx.degree(gG):
    location=locations.get(people[0])
    nx.draw_networkx_labels(gG, pos={people[0]:location},labels={people[0]:people[0]}, font_size=people[1])
plt.show()