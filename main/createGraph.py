'''
Created on 2018年12月24日

@author: jiqy1
'''
import networkx as nx


class CreateGraph(object):
    
    def __init__(self,egleList=None):
        self.G=nx.Graph()
        if(not egleList is None):
            self.addEgle(egleList)

    def addEgle(self,egleList):
        for row in egleList[[1,4]].iterrows():
            self.G.add_edge(str(row[1][1]), str(row[1][4]))
        self.G.remove_edges_from(nx.selfloop_edges(self.G))
    def getGraph(self):
        return self.G
    
    def getEdgesList(self):
        return list(self.G.edges())



