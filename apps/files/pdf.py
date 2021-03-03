import os
import win32com.client   #pip install -U pypiwin32
import re
import shutil
from time import strftime

# to
#  convert) and if so stop executing the script. 
class Convert():
    """this class provide editing tools for excel"""
    def __init__(self,folder,folder2):
        self.folder=folder
        self.folder2=folder2
        
    def convert_word(self):
        
        path = (self.folder)
        try:
            word_file_names = []
            word = win32com.client.Dispatch('Word.Application')
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:  
                    if f.endswith(".docx")  :
                        new_name = f.replace(".docx", ".pdf")
                        in_file =(dirpath + '/'+ f)
                        new_file =(dirpath + '/' + new_name)
                        doc = word.Documents.Open(in_file)
                        doc.SaveAs(new_file, FileFormat = 17)
                        doc.Close()

                    if f.endswith(".doc")   :  #there eroro happen there some files not convert if has .DOC
                        new_name = f.replace(".doc", ".pdf")
                        in_file =(dirpath +'/' + f)
                        new_file =(dirpath +'/' + new_name)
                        doc = word.Documents.Open(in_file)
                        doc.SaveAs(new_file, FileFormat = 17)
                        doc.Close()
        except Exception as e:
            print (e)
        finally:

            word.Quit()

    def convert_excel(self):
        os.chdir(self.folder)

        path = (self.folder)

            # Program to convert the data from an xlsx file to PDF.

        try:
                file_names = []
                excel = win32com.client.Dispatch('Excel.Application')
                for dirpath, dirnames, filenames in os.walk(path):
                    for f in filenames:  
                        if f.endswith(".xlsx") :
                            new_name = f.replace(".xlsx", ".pdf")
                            in_file =(dirpath + '/'+ f)
                            new_file =(dirpath + '/' + new_name)
                            doc = excel.Workbooks.Open(in_file)
                            doc.ExportAsFixedFormat(0,new_file)
                            doc.Close()

                        if f.endswith(".xls"):
                            new_name = f.replace(".xls", ".pdf")
                            in_file =(dirpath +'/' + f)
                            new_file =(dirpath +'/' + new_name)
                            doc = excel.Workbooks.Open(in_file)
                            doc.ExportAsFixedFormat(0,new_file)
                            doc.Close()
        except Exception as e:
            print (e)
        finally:

            excel.Quit()

    #def convert_power_point():
    #def convert_visio():
    #_______________________________________________________________________
    def delete_files(self):
        path=self.folder
        
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
#_________________________________________________________________________________

    def move_pdf(self):
        # to collect pdf files and move it in the same subfolders in other place
        path = (self.folder)
        path2= (self.folder2)
        root_src_dir = os.path.join(path,'source')
        root_target_dir = os.path.join(path,'target')

        operation= 'move' # 'copy' or 'move'

        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_target_dir)
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                if operation is 'copy':
                    shutil.copy(src_file, dst_dir)
                elif operation is 'move':
                    shutil.move(src_file, dst_dir)


    def count_files(filetype):
        path = (r"D:\2work\programing\1stleader\files\specifications")
        ''' (str) -> int
        Returns the number of files given a specified file type.
        >>> count_files(".docx")
        11
        '''
        count_files = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:  
                if f.endswith(filetype) :
                    count_files += 1
                return count_files

        # Try to open win32com instance. If unsuccessful return an error message.

        num_docx = count_files(".docx")

        num_doc = count_files(".doc")



        print ("\n", strftime("%H:%M:%S"), "Finished converting files.")

        # Count the number of pdf files.

        num_pdf = count_files(".pdf")   

        print ("\nNumber of pdf files: ", num_pdf)

        # Check if the number of docx and doc file is equal to the number of files.

        if num_docx + num_doc == num_pdf:
            print ("\nNumber of doc and docx files is equal to number of pdf files.")
        else:
            print ("\nNumber of doc and docx files is not equal to number of pdf files.")

    def convert_pdf_to_png(self):
        from pdf2image import convert_from_path

        os.chdir(self.folder)
        pages = convert_from_path('w1', 500)
        for page in pages:
            page.save('out.jpg', 'JPEG')    
