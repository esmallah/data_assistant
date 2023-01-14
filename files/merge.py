import pandas as pd
import openpyxl
import os

#os.chdir("D:\2work\programing\2data_analysis")


class Merge():
    """this class provide name of work books and sheet names for merge sheets"""
    def __init__(self,folder,connector,readfile1,sheet_name1,readfile2,sheet_name2,writefile,writesheet):
        self.folder=folder
        self.connector=connector
        self.readfile1=readfile1
        self.sheet_name1=sheet_name1
        self.readfile2=readfile2
        self.sheet_name2=sheet_name2
        self.writefile=writefile
        self.writesheet=writesheet

    def vlookup(self):
        os.chdir(self.folder)
        #file_identifier = "*.XLS"
        #THIS_FOLDER = os.path.abspath(self.folder)
        
        item_table=pd.read_excel(self.readfile1)
        monthly_sheet=pd.read_excel(self.readfile2,sheet_name=self.sheet_name2)
        results=monthly_sheet.merge(item_table,on=self.connector)
        results.index.name = None
        writer = pd.ExcelWriter(self.writefile)
        results.to_excel(writer,self.writesheet)
        writer.save()
class Union():
    def __init__(self,folder,connector1,connector2,readfile1,sheet_name1,readfile2,sheet_name2,writefile,writesheet):
        self.folder=folder
        self.connector1=connector1
        self.connector2=connector2
        self.readfile1=readfile1
        self.sheet_name1=sheet_name1
        self.readfile2=readfile2
        self.sheet_name2=sheet_name2
        self.writefile=writefile
        self.writesheet=writesheet
    def connect(self):
        THIS_FOLDER = os.path.abspath(self.folder)
        copyed_file = os.path.join(THIS_FOLDER,self.readfile1)
        master_file = os.path.join(THIS_FOLDER,self.readfile2)

        results=pd.merge(master_file,copyed_file,left_on=self.connector1,right_on=self.connector2)

        writer = pd.ExcelWriter(writefile)

        results.to_excel(writer,writesheet)

        writer.save()