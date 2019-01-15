import networkx as nx
import matplotlib.pyplot as plt
from main.createGraph import createGraph
from main.cleanData import CleanData

politicalNetwork=createGraph()
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
locations=nx.kamada_kawai_layout(G)
edgesList=politicalNetwork.getEdgesList()

nx.draw_networkx_edges(G, locations, edgelist=edgesList,width=0.3, edge_color='r', alpha=0.4)
nx.draw_networkx_nodes(G, locations,node_color='g', node_size=[i[1]**1.3 for i in nx.degree(G)],alpha=0.8)
for people in nx.degree(G):
    location=locations.get(people[0])
    nx.draw_networkx_labels(G, pos={people[0]:location},labels={people[0]:people[0]}, font_size=people[1]**0.5)
plt.show()