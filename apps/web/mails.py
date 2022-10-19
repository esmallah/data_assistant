
from csv import list_dialects
import win32com.client as win32
import pandas as pd
import openpyxl as xl
from openpyxl import load_workbook

import os

outlook = win32.Dispatch('outlook.application')
class Mails_management():
    def __init__(self,folder,readfile,readsheet,column1,column2,writefile,sheetwriter):
        #self.folder=folder
        self.folder=folder
        self.readfile=readfile
        self.readsheet=readsheet
        self.column1=column1
        self.column2=column2
        self.writefile=writefile
        self.sheetwriter=sheetwriter
    def send_emails(itemSelection,attachment):
        #os.chdir(folder)
        #print(folder)
        shoutcoun_name="Eng.Mario","DEAR.aLL"
        shoutcount_to='mario.sameh@lge.com'
        shoutcount_cc='Mohammed.Shawky@insutech-eg.com'

        shoutcount_subject='weekly report for shout count'
        shoutcount_topic='<h2>dear %s<br>good day<br> you can find your interested report in attached  <br></h2>'

        qc_molds_name="DEAR.aLL"
        
        qc_molds_to=['hussein.rashad@insutech-eg.com','mohamed.abdallah@insutech-eg.com','mohamed.farid@insutech-eg.com','Mahmoud.AbdElFatah@cg-eg.com']
        
        qc_molds_cc=['omar.jelany@insutech-eg.com','abdallah.hassan@insutech-eg.com','Mohammed.Shawky@insutech-eg.com','ahmed.aly@cg-eg.com','mostafa.abdelaziz@insutech-eg.com','ahmed.khayry@insutech-eg.com','ahmed.elsayed@insutech-eg.com']
        qc_molds_subject='تقرير الجودة اليومي'

        qc_molds_topic=['<h2>السادة الكرام <br>بعد التحية<br> مرفق تقرير الجودة لمنتجات حقن الفوم ، ولوحظ بعض حالات عدم المطابقة برجاء الرد عليها في المخلص التالي:  <br></h2>']
        
        LIST_NAME=[shoutcoun_name,qc_molds_name]
        EMAIL_TO=[shoutcount_to,qc_molds_to]
        EMAIL_CC=[shoutcount_cc,qc_molds_cc]
        LIST_SUBJECT=[shoutcount_subject,qc_molds_subject]
        LIST_TOPIC=[shoutcount_topic,qc_molds_topic]
        
        '''
        mafdy_mail='mafdy.khalil@cg-eg.com'
        ihab='ehab.adel@cg-eg.com'
        xps_maintenace='mohamed.abdelmajed@cg-eg.com'
        spare_parts_insutec='SP.Insutech@cg-eg.com'
        ahmed_nagdy='ahmed.nagdy@insutech-eg.com'
        ahmed_elsayde='ahmed.elsayed@insutech-eg.com'
        
        mafdy_report='<h2>dear Eng. mafdy<br>good day<br> kindly send your montly report as following  <br> صرف قطع الغيار  -summary-تقرير الاعطال-تقرير قطع الغيار</h2>'
        finance_mail='<h2>dear mr. ihab<br>good day<br> kindly send your montly report as following  <br>sales report'
        mafdy_report='<h2>dear Eng. mafdy<br>good day<br> kindly send your montly report as following  <br> صرف قطع الغيار -تقرير قطع الغيار</h2>'
        hmedNgdy_report='<h2>dear Mr. ahmed <br>good day<br> kindly send your montly report as following  <br>   -summary-تقرير الاعطال- <br> OEE , <br></h2>'
        ahmed_elsayed_report='<h2>dear Mr. Ahmed<br>good day<br> kindly send your montly report as following  <br>   -تسوية الخامة والكسر - <br> متابعه  خطه مبيعات وانتاج مصانع الفوم , <br></h2>'
        '''

        item_name=LIST_NAME[itemSelection]
        item_to=EMAIL_TO[itemSelection]
        item_cc=EMAIL_CC[itemSelection]
        item_subject=LIST_SUBJECT[itemSelection]#%item_name
        item_tobic=LIST_TOPIC[itemSelection]
        personal_mail=item_name
        subject_mail=item_subject
        
        mail = outlook.CreateItem(0)
        mail.To = item_to
        mail.Cc = item_cc
        mail.Subject = subject_mail
        mail.Body = 'Message body'
        mail.HTMLBody = item_tobic

        # To attach a file to the email (optional):
        print ("mail was send to with attachmed ",attachment,"located in ",itemSelection)

        #attachment  = folder+"v129molds_shoutcount.xlsx"
        print(attachment)
        mail.Attachments.Add(attachment)
        mail.Send()
        
    import win32com.client


    def extract(count):
        """Get emails from outlook."""
        items = []
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)  # "6" refers to the inbox
        messages = inbox.Items
        message = messages.GetFirst()
        i = 0
        while message:
            try:
                message = dict()
                message["Subject"] = getattr(message, "Subject", "<UNKNOWN>")
                message["SentOn"] = getattr(message, "SentOn", "<UNKNOWN>")
                message["EntryID"] = getattr(message, "EntryID", "<UNKNOWN>")
                message["Sender"] = getattr(message, "Sender", "<UNKNOWN>")
                message["Size"] = getattr(message, "Size", "<UNKNOWN>")
                message["Body"] = getattr(message, "Body", "<UNKNOWN>")
                items.append(message)
            except Exception as ex:
                print("Error processing mail", ex)
            i += 1
            if i < count:
                message = messages.GetNext()
            else:
                return items

        return items


    def show_message(items):
        """Show the messages."""
        items.sort(key=lambda tup: tup["SentOn"])
        for i in items:
            print(i["SentOn"], i["Subject"])


    #def main():
     #   """Fetch and display top message."""
      #  items = extract(5)
       # show_message(items)


    #if __name__ == "__main__":
     #   main()
