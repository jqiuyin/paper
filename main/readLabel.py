'''
Created on 2019年1月13日

@author: qiuyin
'''
'''
从文件系统中读取筛选数据所需的标签
'''
def getScholarLabel():
    scholar_label=[]
    with open('scholar_label.txt','r',encoding='UTF-8') as read:
        for i in read:
            scholar_label.append(i.strip('\n'))
            
    return scholar_label
        
def getPoliticalLable():
    politic_label=[]
    with open('politic_lable.txt','r',encoding='UTF-8') as read:
        for i in read:
            politic_label.append(i.strip('\n'))
            
    return politic_label

def getLable(filename):
    label=[]
    with open(filename,'r',encoding='UTF-8') as read:
        for i in read:
            label.append(i.strip('\n'))
            
    return label


if __name__=='__main__':
    print(getScholarLabel())