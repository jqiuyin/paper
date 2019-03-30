'''
Created on 2018年11月8日

@author: jiqy1
'''
import main.connectToAccess as source
from main.readLabel import getScholarLabel

class CleanData(object):
    def __init__(self,table=source.getData(),lable):
        self.table=table
        self.lable=lable
        
    def get_table(self):
        return self.table[self.table[3].isin(self.lable)]
    

if __name__=='__main__':
    cleanData=CleanData()
    print(cleanData.get_table(label=getScholarLabel()))