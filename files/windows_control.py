import os
import openpyxl
from openpyxl import Workbook
import pandas as pd

list_files=[]
class Files_control():
    def __init__(self,folder,folder2):
        self.folder=folder
        self.folder2=folder2
    def get_Files_names (path,outputpath): 
        os.chdir(outputpath)
        with open("F01-INS-QES-P-02_documentation_master_list.xls", "w") as a:
            for path, subdirs, files in os.walk(path):
                for filename in files:
                    f = os.path.join( filename)
                    list_files.append(str(f))
        print(list_files[10])

    #    f= open('list.xlsx','w')  
    #   for index,filename in enumerate(list_files):
    #      f.write("%s. %s \n"%(index,filename.encode("utf-8")))
        
        wb = openpyxl.Workbook()
        ws = wb.active

        ws.title = "list"
        r = 2  # start at fourd row
        c = 1 # column 'a'
        for item in list_files:
            ws.cell(row=r, column=c).value = item
            r += 1 # Column 'b'
        r = 2
        c += 1
        wb.save("list.xlsx")
        return list_files

    
    #2 write xcel file for folders name
    def get_folders_list (path,outputpath): 
        os.chdir(outputpath)
        folders= os.listdir (path) # get all files' and folders' names in the current directory
        result = ['the departments']
        for folder in folders: # loop through all the files and folders
            if os.path.isdir(os.path.join(os.path.abspath(path), folder)): # check whether the current object is a folder or not
                result.append(folder) 
        result.sort()
        f= open('list.xlsx','w')
        for index,folder in enumerate(result):
            f.write("%s. %s \n"%(index,folder))
        f.close()

    def resize_image(path):
        #!/usr/bin/python
        from PIL import Image
        import os, sys

        #path = "/root/Desktop/python/images/"
        dirs = os.listdir( path )

        def resize():
            for item in dirs:
                if os.path.isfile(path+item):
                    im = Image.open(path+item)
                    f, e = os.path.splitext(path+item)
                    imResize = im.resize((200,200), Image.ANTIALIAS)
                    imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

        resize()
    def creatfolders(self,path,outputpath):
        os.chdir(path)
        
        if not os.path.exists(outputpath):
            os.makedirs(outputpath)