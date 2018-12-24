'''
Created on 2018年12月24日

@author: jiqy1
'''
import networkx as nx
import matplotlib.pyplot as plt
import main.cleanData as data
data=data.CleanData()

result=data.get_table("bad_one")
print(result)
G=nx.Graph()
G.add_edge("a", "b")
plt.figure()
nx.draw(G,  node_color='y' , with_labels=True,node_size=800)
plt.show()