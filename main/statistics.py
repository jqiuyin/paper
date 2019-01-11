'''
Created on 2019年1月11日

@author: qiuyin
'''
import main.createGraph
import networkx as nx
import pandas as pd
import threading
import time
G=main.createGraph.getGraph();
degreeCentrality=None
betweennessCentrality=None
closenessCentrality=None
eigenvectorCentrality=None


def t1():
    degreeCentrality=pd.Series(nx.degree_centrality(G),name='度中心性').sort_values(ascending=False)
    print(degreeCentrality)
def t2():
    betweennessCentrality=pd.Series(nx.betweenness_centrality(G),name='中介中心性').sort_values(ascending=False)
    print(betweennessCentrality)
def t3():
    closenessCentrality=pd.Series(nx.closeness_centrality(G),name='接近中心性').sort_values(ascending=False)
    print(closenessCentrality)
def t4():
    eigenvectorCentrality=pd.Series(nx.eigenvector_centrality(G),name='特征向量中心性').sort_values(ascending=False)
    print(eigenvectorCentrality)

start=time.time()
# threading.Thread(target=t1).start()
# threading.Thread(target=t2).start()
# threading.Thread(target=t3).start()
# threading.Thread(target=t4).start()

t1()
t2()
t3()
t4()

stop=time.time()
print(stop-start)


