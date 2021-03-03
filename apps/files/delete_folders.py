import os
import win32com.client
import re
import shutil

path = (r'D:\2work\07-PR production\INS-PR-P-01 اجراء انتاج الفوم')
# to convert) and if so stop executing the script. 
def delete_word_excel():
    
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:  
            if f.endswith(".docx") :
            
                os.remove(os.path.join(dirpath,f))

            if f.endswith(".doc"):
            
                os.remove(os.path.join(dirpath,f))
            if f.endswith(".xlsx"):
                os.remove(os.path.join(dirpath,f))

            if f.endswith(".xls"):
                os.remove(os.path.join(dirpath,f))