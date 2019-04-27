'''
Created on 2018年11月8日

@author: jiqy1
'''
'''
根据传入标签列表筛选数据
'''
class CleanData(object):
    def __init__(self,label,table):
        self.table=table
        self.label=label
        
    def get_table(self):
        return self.table[self.table[3].isin(self.label)]
    