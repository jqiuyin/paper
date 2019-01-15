'''
Created on 2019年1月11日

@author: qiuyin
'''
import networkx as nx
import pandas as pd


class Statistics(object):
    def __init__(self,graph):
        G=graph

    def getDegreeCentrality(self):
        degreeCentrality=pd.Series(nx.degree_centrality(self.G),name='度中心性').sort_values(ascending=False)
        return degreeCentrality
    
    def getBetweennessCentrality(self):
        betweennessCentrality=pd.Series(nx.betweenness_centrality(self.G),name='中介中心性').sort_values(ascending=False)
        return betweennessCentrality
    
    def getClosenessCentrality(self):
        closenessCentrality=pd.Series(nx.closeness_centrality(self.G),name='接近中心性').sort_values(ascending=False)
        return closenessCentrality
    
    def getEigenvectorCentrality(self):
        eigenvectorCentrality=pd.Series(nx.eigenvector_centrality(self.G),name='特征向量中心性').sort_values(ascending=False)
        return eigenvectorCentrality
    


