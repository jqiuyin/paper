'''
Created on 2019年1月13日

@author: qiuyin
'''

def getScholarLabel():
    scholar_label=[]
    with open('scholar_label.txt','r',encoding='UTF-8') as read:
        for i in read:
            scholar_label.append(i.strip('\n'))
            
    return scholar_label
        