'''
Created on 2018年12月24日

@author: jiqy1
'''
import networkx as nx
import matplotlib.pyplot as plt
import main.cleanData as data
 
data=data.CleanData()

bad_one=data.get_quick_table("bad_one")
bad_two=data.get_quick_table("bad_two")
bad_three=data.get_quick_table("bad_three")
good_one=data.get_quick_table("good_one")
good_two=data.get_quick_table("good_two")
good_three=data.get_quick_table("good_three")

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

def getGraph():
    return G





