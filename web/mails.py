
from csv import list_dialects
import win32com.client as win32
import pandas as pd
import openpyxl as xl
from openpyxl import load_workbook
#from analysis.collect import Select
import os
from server.config.settings_cross import *
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
    def send_emails(year,month,day,to_day,itemSelection,attachment,conn_db=True):
        #os.chdir(folder)
        #print(folder)
        fllowup_topic='''
                Dear all<br>
                Good day<br>
                Kindly find the point is open to solving many quality issues<br>
                 , kindly reply by last situation for your point after handling it<br>
                السادة الكرام<br>
                مرفق قائمة المتابعة الخاصة بموضوعات المتعلقة بحل مشكلات تؤثر علي جودة المنتجات <br>
                ، برجاء مراجعة القائمة المرفقة التي توضح القضية والمطلوب والمسئول<br>
                ، واغلاق المطلوب من كل فرد من السادة الذين تم اضافتهم في الايميل<br>
                    '''

        
        shoutcoun_name="Eng.Mario","DEAR.aLL"
        shoutcount_to='mario.sameh@lge.com'
        shoutcount_cc='Mohammed.Shawky@insutech-eg.com'
        shoutcount_subject='weekly report for shout count'
        shoutcount_topic='<h2>dear eng.mario<br>good day<br> you can find your interested report in attached  <br></h2>'

        qc_molds_name="DEAR.aLL"
        qc_molds_to=['hussein.rashad@insutech-eg.com','mohamed.abdallah@insutech-eg.com','mohamed.farid@insutech-eg.com','Mahmoud.AbdElFatah@cg-eg.com']
        qc_molds_cc=['omar.jelany@insutech-eg.com','abdallah.hassan@insutech-eg.com','Mohammed.Shawky@insutech-eg.com','ahmed.aly@cg-eg.com','mostafa.abdelaziz@insutech-eg.com','ahmed.khayry@insutech-eg.com','ahmed.elsayed@insutech-eg.com']
        qc_molds_subject='تقرير الجودة اليومي'
        qc_molds_topic='<h2>السادة الكرام <br>بعد التحية<br> مرفق تقرير الجودة لمنتجات حقن الفوم ، ولوحظ بعض حالات عدم المطابقة برجاء الرد عليها في المخلص التالي:  <br></h2>'
        
        test_name="Eng.Mario","DEAR.aLL"
        test_to='youssri.ahmed@insutech-eg.com'
        test_cc='youssri.ahmed@insutech-eg.com'
        test_subject='تجربة'
        test_topic='رسالة تجريبية'

        fllowup_purchasing_to='mohamed.hamza@insutech-eg.com;ramy.ali@lge.com;mohamed.khater@cg-eg.com;Ismail.Mammon@insutech-eg.com'
        fllowup_purchasing_cc='Mohammed.Shawky@insutech-eg.com;ahmed.Elmetwaly@cg-eg.com;manal.elsayed@insutech-eg.com'
        fllowup_purchasing_subject='قائمة متابعة -ادارة المشتريات'
        fllowup_purchasing_topic=fllowup_topic

        fllowup_maintenance_to='ahmed.abozaid@insutech-eg.com;ahmed.sherif@cg-eg.com;ahmed.sabah@cg-eg.com'
        fllowup_maintenance_cc='mostafa.abdelaziz@insutech-eg.com;Mohammed.Shawky@insutech-eg.com;mohamed.hegazy@cg-eg.com'
        fllowup_maintenance_subject='قائمة متابعة -ادارة الصيانة'
        fllowup_maintenance_topic=fllowup_topic

        fllowup_production_to='omar.jelany@insutech-eg.com;AbdElrahman.Zakria@insutech-eg.com;mohamed.abdallah@insutech-eg.com'
        fllowup_production_cc='mostafa.abdelaziz@insutech-eg.com;Mohammed.Shawky@insutech-eg.com'
        fllowup_production_subject='قائمة متابعة -ادارة الانتاج'
        fllowup_production_topic=fllowup_topic

        fllowup_quality_to='Mohammed.Shawky@insutech-eg.com;ahmed.aly@cg-eg.com>'
        fllowup_quality_cc=''
        fllowup_quality_subject='قائمة متابعة -ادارة الجودة'
        fllowup_quality_topic=fllowup_topic

        fllowup_warehouse_to='elhosaini.mohamed@insutech-eg.com;Block.RM@insutech-eg.com; Block.SP@insutech-eg.com'
        fllowup_warehouse_cc='Mohammed.Shawky@insutech-eg.com; mostafa.abdelaziz@insutech-eg.com;hamada.elnaggar@insutech-eg.com'
        fllowup_warehouse_subject='قائمة متابعة -ادارة المخازن'
        fllowup_warehouse_topic=fllowup_topic

        fllowup_october_to='hamada.shawkey@insutech-eg.com;mohamed.abdallah@insutech-eg.com; ahmed.nagdy@insutech-eg.com'
        fllowup_october_cc='Mohammed.Shawky@insutech-eg.com;mafdy.khalil@insutech-eg.com'
        fllowup_october_subject='قائمة متابعة  مصنع 6 اكتوبر'
        fllowup_october_topic=fllowup_topic

        fllowup_safety_to='magdy.sleem@insutech-eg.com'
        fllowup_safety_cc='Mohammed.Shawky@insutech-eg.com;ahmed.aboshady@insutech-eg.com'
        fllowup_safety_subject='قائمة متابعة  السلامة والصحة المهنية'
        fllowup_safety_topic=fllowup_topic

        fllowup_hr_to='doaa.abdelhamid@insutech-eg.com;Belal.Saad@insutech-eg.com;mohamed.elsayed@insutech-eg.com'
        fllowup_hr_cc='Mohammed.Shawky@insutech-eg.com;ahmed.aboshady@insutech-eg.com'
        fllowup_hr_subject='قائمة متابع الموارد البشرية'
        fllowup_hr_topic=fllowup_topic

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

        #for data from Database
        
        if conn_db:
            from ..analysis.collect import Select,Data_db
            git_database=Select(format_path,"formatQC_report_monthly_v3.xlsx","output",year,month,'QC_molds_monthly_v2.xlsx',"Sheet1")
            fuNgetDailyReport=git_database.monthly_molds(dailyReportName,year,month,day,to_day,monthly=False,daily=True)
            fuNgetFollowUp=Data_db.f22followup()
            
        else:
            fuNgetDailyReport=[]
            funShoutCount=[]
            funTest=[]
            fuNgetFollowUp=[]
        #_____list data by run functions____________
        
        
        
        
        functions_getdata=[funShoutCount,fuNgetDailyReport,funTest,fuNgetFollowUp]
        list_reports=functions_getdata[itemSelection]
        
        #_____list email data by manual____________
        LIST_NAME=[shoutcoun_name,qc_molds_name,test_name,]
        EMAIL_TO=[shoutcount_to,qc_molds_to,test_to,fllowup_purchasing_to,fllowup_maintenance_to,
        fllowup_production_to,fllowup_quality_to,fllowup_warehouse_to,fllowup_october_to,
        fllowup_safety_to,fllowup_hr_to]
        EMAIL_CC=[shoutcount_cc,qc_molds_cc,test_cc,fllowup_purchasing_cc,fllowup_maintenance_cc,
        fllowup_production_cc,fllowup_quality_cc,fllowup_warehouse_cc,fllowup_october_cc,
        fllowup_safety_cc,fllowup_hr_cc]
        LIST_SUBJECT=[shoutcount_subject,qc_molds_subject,test_subject,fllowup_purchasing_subject,fllowup_maintenance_subject,
        fllowup_production_subject,fllowup_quality_subject,fllowup_warehouse_subject,fllowup_october_subject,
        fllowup_safety_subject,fllowup_hr_subject]
        LIST_TOPIC=[shoutcount_topic,qc_molds_topic,list_reports,fllowup_purchasing_topic,fllowup_maintenance_topic,
        fllowup_production_topic,fllowup_quality_topic,fllowup_warehouse_topic,fllowup_october_topic,
        fllowup_safety_topic,fllowup_hr_topic]
                
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
        print("_______attachments____________",attachment)

        #mail.Attachments.Add(attachment)
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
