'''
Created on 2018年12月24日

@author: jiqy1
'''
import networkx as nx
import matplotlib.pyplot as plt
import main.cleanData as data
 
data=data.CleanData()

bad_one=data.get_table("bad_one")
bad_two=data.get_table("bad_two")
bad_three=data.get_table("bad_three")
good_one=data.get_table("good_one")
good_two=data.get_table("good_two")
good_three=data.get_table("good_three")

#print(result[[1,4]])
G=nx.Graph()
goodList=[]
badList=[]
def addEgle(G,result,tpye):
    for row in result[[1,4]].iterrows():
    #print(row[1][4])
        if tpye == -1:
            badList.append((str(row[1][1]), str(row[1][4])))
        else:
            goodList.append((str(row[1][1]), str(row[1][4])))
        G.add_edge(str(row[1][1]), str(row[1][4]))
addEgle(G, bad_one, -1)
addEgle(G, bad_two, -1)
addEgle(G, bad_three, -1)
addEgle(G, good_one, 1)
addEgle(G, good_two, 1)
addEgle(G, good_three, 1)

#print(nx.degree(G))
#print(G.edges())
#print([i[1]*30 for i in nx.degree(G)])
# G.add_edge("a", "b")
#print(nx.kamada_kawai_layout(G))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=[18,18])   
locations=nx.kamada_kawai_layout(G)

nx.draw_networkx_edges(G, locations, edgelist=goodList,width=0.3, edge_color='r', alpha=0.4)
nx.draw_networkx_edges(G, locations, edgelist=badList,width=0.3, edge_color='b', alpha=0.4)
nx.draw_networkx_nodes(G, locations,node_color='g', node_size=[i[1]**1.3 for i in nx.degree(G)],alpha=0.8)
for people in nx.degree(G):
    location=locations.get(people[0])
    #print(location)
    nx.draw_networkx_labels(G, pos={people[0]:location},labels={people[0]:people[0]}, font_size=people[1]**0.5)
# nx.draw_networkx(G,pos=locations,with_labels=False,node_size=[i[1] for i in nx.degree(G)])
plt.show()



