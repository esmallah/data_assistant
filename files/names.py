#this is first manul machine learning for select and rename sheets and columns for set up pre database
import pandas as pd
import os

class Names():
    """this class provide  work books and sheet names as input """
    def __init__(self,folder,readfile1,sheet1,writefile,writesheet):
        self.folder=folder
        
        self.readfile1=readfile1
        self.sheet1=sheet1
        
        self.writefile=writefile
        self.writesheet=writesheet

    def sheets(self):
        c_t_reports=['تحليل  ','تحليل','التحليل','تحليل  ']
        
      
    def columns(self):
        '''for append all workbooks in the same directory  by indix handling by columns name'''
        

        os.chdir(self.folder)
        df = pd.read_excel(f,self.sheet1)
        
        # now save the data frame
        writer = pd.ExcelWriter(self.writefile)
        all_data.to_excel(writer,self.writesheet)
        writer.save()    
        
#mohamed_no3emy_sheets
