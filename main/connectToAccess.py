import pypyodbc
import pandas

def getData():
    str='Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=C:\\Users\\jiqy1\\Desktop\\CBDB_aw_20180831\\CBDB_aw_20180831\\CBDB_aw_20180831\\CBDB_20180831_DATA1.mdb'
    db=pypyodbc.win_connect_mdb(str)
    curser=db.cursor()
    curser.execute("select t1.c_personid , t1.c_name_chn , t1.c_index_year , c_assoc_desc_chn , t2.c_name_chn  from BIOG_MAIN as t1 , BIOG_MAIN as t2 , ASSOC_DATA , ASSOC_CODES where (t2.c_personid = ASSOC_DATA.c_assoc_id) and (ASSOC_DATA.c_assoc_code = ASSOC_CODES.c_assoc_code) and (t1.c_personid = ASSOC_DATA.c_personid) and (t1.c_index_year>=960 and t1.c_index_year<=1279)")
    result=curser.fetchall()
    table=pandas.DataFrame([row for row in result])
    #pandas.set_option('display.max_rows',None)
    return table
    
