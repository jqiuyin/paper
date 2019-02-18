import networkx as nx
import matplotlib.pyplot as plt
from main.createGraph import CreateGraph
from main.cleanData import CleanData
politicalNetwork=CreateGraph()
data=CleanData()



bad_one=data.get_quick_table("bad_one")
bad_two=data.get_quick_table("bad_two")
bad_three=data.get_quick_table("bad_three")
good_one=data.get_quick_table("good_one")
good_two=data.get_quick_table("good_two")
good_three=data.get_quick_table("good_three")

politicalNetwork.addEgle(bad_one)
politicalNetwork.addEgle(bad_two)
politicalNetwork.addEgle(bad_three)
politicalNetwork.addEgle(good_one)
politicalNetwork.addEgle(good_two)
politicalNetwork.addEgle(good_three)

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