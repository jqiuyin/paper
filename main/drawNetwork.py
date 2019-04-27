'''
Created on 2019年2月18日

@author: qiuyin
'''


import networkx as nx
'''
使用matplotlib将关系图绘制到自动画布中
'''
class DrawNetwork(object):
    def __init__(self,ax, Graph,font_size=0.2):
        self.g=Graph
        self.font_size=font_size
        self.ax=ax
    def draw(self):
        
        locations=nx.kamada_kawai_layout(self.g)
        edgesList=list(self.g.edges())
        nx.draw_networkx_edges(self.g, locations,ax=self.ax,edgelist=edgesList,width=0.3, edge_color='r')
        nx.draw_networkx_nodes(self.g, locations,ax=self.ax,node_color='g', node_size=[i[1]**1.3 for i in nx.degree(self.g)])
        for people in nx.degree(self.g):
            location=locations.get(people[0])
            nx.draw_networkx_labels(self.g,ax=self.ax, pos={people[0]:location},labels={people[0]:people[0]}, font_size=people[1]*self.font_size)
        
    