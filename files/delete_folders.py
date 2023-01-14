import os
import win32com.client
import re
import shutil

class delete_files():
    def __init__(self,folder,folder2):
            self.folder=folder
            self.folder2=folder2
        
    #path = (r'D:\2work\07-PR production\INS-PR-P-01 اجراء انتاج الفوم')
    # to convert) and if so stop executing the script. 
    def delete_word_excel(self):
        
        for dirpath, dirnames, filenames in os.walk(self.folder):
            for f in filenames:  
                if f.endswith(".docx") :
                
                    os.remove(os.path.join(dirpath,f))
                    print("all words files has deleted")
                if f.endswith(".doc"):
                
                    os.remove(os.path.join(dirpath,f))
                    print("all old words files has deleted")
                if f.endswith(".xlsx"):
                    os.remove(os.path.join(dirpath,f))
                    print("all excel files has deleted")
                if f.endswith(".xls"):
                    os.remove(os.path.join(dirpath,f))
                    print("all old excel files has deleted")
