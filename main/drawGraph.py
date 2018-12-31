'''
Created on 2018年12月24日

@author: jiqy1
'''
import networkx as nx
import matplotlib.pyplot as plt
import main.cleanData as data

data=data.CleanData()

result=data.get_table("bad_one")
#print(result[[1,4]])
G=nx.MultiGraph()
for row in result[[1,4]].iterrows():
    #print(row[1][4])
    G.add_edge(str(row[1][1]), str(row[1][4]))

#print(nx.degree(G))
#print([i[1]*30 for i in nx.degree(G)])
# G.add_edge("a", "b")
#print(nx.kamada_kawai_layout(G))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()   
locations=nx.kamada_kawai_layout(G)
for people in nx.degree(G):
    location=locations.get(people[0])
    #print(location)
    nx.draw_networkx_labels(G, pos={people[0]:location},labels={people[0]:people[0]}, font_size=people[1]**0.8)
nx.draw_networkx(G,pos=nx.kamada_kawai_layout(G),with_labels=False,node_size=[i[1]**1.8 for i in nx.degree(G)])
plt.show()
