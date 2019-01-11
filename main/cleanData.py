'''
Created on 2018年11月8日

@author: jiqy1
'''
import main.connectToAccess as source
import pandas as pd
import datetime

class CleanData(object):
    def __init__(self):
        self.table=source.getData()
        """用于分类的标签"""
        self.bad_one_label="不合,拒絕在Y主政的政府中任職,拒絕在Y的主政期出仕,拒絕會面,欲辟Y為幕僚但被拒絕,拒為Y之黨,拒Y游説".split(",")
        self.bad_two_label="反對/攻訐,彈劾,反對/不支持Y的政策,排擠,得罪Y,忌/惡,批評,反對Y稱帝,以詩諷忤Y,與Y爭權,其黨攻訐Y,反對赦免,遭Y新法支持者排擠,遭Y蔡京勢力排擠".split(",")
        self.bad_three_label="陷害Y,其（或追隨者）殺害Y,逮捕,鞫治,建議處決Y,籌劃謀殺,下令處決,處決,逃離Y的統治區,王安石新法反對者".split(",")
        self.good_one_label="門客為Y,恩主是Y,黨羽為Y,黨魁為Y,政見趨同,副Y出使,以Y為謀士,以宦官事Y".split(",")
        self.good_two_label="欣賞/器重,支持,喜爱,稱道Y之政績,護佑Y,擁立Y,王安石新法支持者".split(",")
        self.good_three_label="因與Y的交往受牽連,其同犯被指為Y".split(",")
        """存储分类后数据的列表"""
        self.bad_one_list=[]
        self.bad_two_list=[]
        self.bad_three_list=[]
        self.good_one_list=[]
        self.good_two_list=[]
        self.good_three_list=[]
        """分类"""
        for row in self.table.iterrows():
            #print(row[1][3])
            if (row[1][3] in self.bad_one_label)&(row[1][1]!="<待删除>"):
                #print(list(row[1]))
                self.bad_one_list.append(list(row[1]))
            elif(row[1][3] in self.bad_two_label)&(row[1][1]!="<待删除>"):
                self.bad_two_list.append(list(row[1]))
            elif(row[1][3] in self.bad_three_label)&(row[1][1]!="<待删除>"):
                self.bad_three_list.append(list(row[1]))
            elif(row[1][3] in self.good_one_label)&(row[1][1]!="<待删除>"):
                self.good_one_list.append(list(row[1]))
            elif(row[1][3] in self.good_two_label)&(row[1][1]!="<待删除>"):
                self.good_two_list.append(list(row[1]))
            elif(row[1][3] in self.good_three_label)&(row[1][1]!="<待删除>"):
                self.good_three_list.append(list(row[1]))
        #self.bad_one_table = pd.DataFrame(bad_one_list)
        
    
    def get_table(self,type):
        if(type =="bad_one"):
            return pd.DataFrame(self.bad_one_list)
        elif(type=="bad_two"):
            return pd.DataFrame(self.bad_two_list)
        elif(type=="bad_three"):
            return pd.DataFrame(self.bad_three_list)
        elif(type =="good_one"):
            return pd.DataFrame(self.good_one_list)
        elif(type=="good_two"):
            return pd.DataFrame(self.good_two_list)
        elif(type=="good_three"):
            return pd.DataFrame(self.good_three_list)
    
    
    def get_quick_table(self,type):
        if(type =="bad_one"):
            return self.table[self.table[3].isin(self.bad_one_label)]
        elif(type=="bad_two"):
            return self.table[self.table[3].isin(self.bad_two_label)]
        elif(type=="bad_three"):
            return self.table[self.table[3].isin(self.bad_three_label)]
        elif(type =="good_one"):
            return self.table[self.table[3].isin(self.good_one_label)]
        elif(type=="good_two"):
            return self.table[self.table[3].isin(self.good_two_label)]
        elif(type=="good_three"):
            return self.table[self.table[3].isin(self.good_three_label)]
#print(bad_one_label)

if __name__=='__main__':
    start=datetime.datetime.now()
    cleanData=CleanData()
    print(cleanData.get_quick_table("bad_one"))
    print(cleanData.get_quick_table("bad_two"))
    print(cleanData.get_quick_table("bad_three"))
    print(cleanData.get_quick_table("good_one"))
    print(cleanData.get_quick_table("good_two"))
    print(cleanData.get_quick_table("good_three"))
    stop=datetime.datetime.now()
    delta=stop-start
    print(delta.seconds)