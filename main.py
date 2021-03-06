__author__ = 'youssri Ahmed Hamdy <estratigy@yahoo.com>'
__copyright__ = 'Copyright (c) 2021'
__version__ = '1.0.0'

import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore
from interface import Ui_MainWindow
from Lib.TabBarStyle import TabBarStyle

import time
import os
from apps import Group
from apps import Block
from apps import Unique,Select
from apps import Connection


class Stream(QtCore.QObject):
    '''
    to print console
    '''
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

#from test_main.py import TestAnalyss

class AppWindow(Ui_MainWindow,QMainWindow):
    def __init__(self,parent=None):
        super(AppWindow,self).__init__(parent)
        #self.Ui_MainWindow = Ui_MainWindow()
        self.setupUi(self)
        self.signals_control()
        self.show()
        #self.listWebFilterLGItems.clearSelection()
        self.deepLearning()
        
    def signals_control(self):        
        #switchers tabs
        self.button_AI_leader.clicked.connect(self.conntectTabs0)
        self.buttonKnowledge.clicked.connect(self.conntectTabs1)
        self.button_analysis.clicked.connect(self.conntectTabs2)
        self.buttonFiles.clicked.connect(self.conntectTabs3)
        self.buttonWeb.clicked.connect(self.conntectTabs4)
        self.button_reporting.clicked.connect(self.conntectTabs5)
        #switchers contrlo panel
        self.butRestart.clicked.connect(self.restart)
        #switchers main_AI_leader tabs
        self.butSubLeader.clicked.connect(self.connSubLeader_items)
        self.butSubLeader_adjusting.clicked.connect(self.connSubLeader_adjusting)
        #switchers main_properties tabs
        self.butSubPropFilter.clicked.connect(self.connSubPropFilter)
        self.butSubPropResults.clicked.connect(self.connSubPropResults)
        # tabs_Leaders:        
        self.pBut_tabSubLeader_adjust_thinking.clicked.connect(self.deepLearning)
        #switcher subtabs _analysis

        self.ButWebFilterRefresh.clicked.connect(self.clickedList)
        
        self.but_analysis_SubAdres_reports.clicked.connect(self.connSubanalysis_reports)
        self.but_analysis_SubAdres_database.clicked.connect(self.connSubAnalysis_DB)

        self.ButtonAnalysisDownload.clicked.connect(self.connect_shareDb)
        self.ButtonAnalysisTester.clicked.connect(self.test)
        self.But_analysis_prepareDB.clicked.connect(self.database_management)
    
        
        siteName=self.interTheWebSiteLineEdit.text()
        
        self.ButWebFilterOpensites.clicked.connect(lambda: Connection.site_connection(self,siteName))
        
        self.listWebFilterLGItems.currentItemChanged.connect(self.clickedList)
        #sqlite database
        self.ButWebFilterOpensites_4.clicked.connect(self.dataIntry)
        #file controle___________________________________________
        self.But_FileControl_execute.clicked.connect(self.files_control)
        #switcher control panel
        #from memory import Sqlite_db
        #self.controlBanel_createDb.clicked.connect(Sqlite_db)
        #mail control_____________
        self.but_web_filler.clicked.connect(self.connSubWeb_filler)
        self.but_web_mail.clicked.connect(self.connSubWeb_mail)
        self.but_web_next.clicked.connect(self.connSubWeb_next)

        self.ButWebMailSend.clicked.connect(self.mailControl)
    #__________________________control panel
    def restart(self):        
        if __name__ == "__main__":
            import sys
            app = QApplication(sys.argv)
            #app.setStyle(TabBarStyle())
            ex = AppWindow()
            sys.exit(app.exec_())
            while True:
                #ex = Main()
                ex.setFont(QFont("Consolas", 10))
                ex.setStyleSheet(blue)
                #welcome = Welcome(ex)
                ex.showMaximized()
                current_exit_code = app.exec()
                if current_exit_code == -123456789:
                    break
    #___________________________automated web control section_____________________________#
    def clickedList(self):
        from apps import AutomatedFilling
        print("___________________test interface______________")
        switcher = {
        "LG43UJ63":0,
        "LG49UJ63":1,
        "LG55UK630":2,
        "LGLG32LM55":3,
        "LGLG43LM63":4,
        "FRONT 43LM63":5,
        "FRONT 43LM55":6,
        "LG65UM73up&down":7,
        "LG65UM73LR":8,
        "LG43UP77":9,
        "LG65UP775Front":10,
        "LG65UP77set":11,
        "LG65UP81set":12,
        "LG65UP81Side":13,
        "LG75UP77FRONT":14,
        "LG75UP77":15,
        "LG43UP81":16,
        "LgWasherCover":17,
        "LgWasherAngels":18,
        "LgWasherBase":19
        }
        #self.ButWebFilterFIllNames.clicked.disconnect()
        
        item = self.listWebFilterLGItems.currentItem()

        if item is None:
            print("kindly select the item form the items list")
        #if item is not None:
        else:
            
            x=switcher.get(item.text(), "Invalid items")
            print("now is printing","item:",item.text(),"code:",x,"its type:",type(x))

            self.ButWebFilterFIllNames.clicked.connect(lambda:AutomatedFilling.pastNames(x))
            self.ButWebFilterFIllData.clicked.connect(lambda:AutomatedFilling.past_form(x,standard_spec=False,vertically=False))
            
            #print(map(x,switcher))   
            #self.close()
    
    def conntectTabs(self):
        self.tabWidget_left.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(1)    
    def conntectTabs0(self):
        self.tabWidget_left.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(1)
    def conntectTabs1(self):
        self.tabWidget_left.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def conntectTabs2(self):
        self.tabWidget_left.setCurrentIndex(2)
        self.tabMaps.setCurrentIndex(0)
    def conntectTabs3(self):
        self.tabWidget_left.setCurrentIndex(3)
        self.tabMaps.setCurrentIndex(0)
    def conntectTabs4(self):
        self.tabWidget_left.setCurrentIndex(4)
        self.tabMaps.setCurrentIndex(0)
    def conntectTabs5(self):
        self.tabWidget_left.setCurrentIndex(5)
        self.tabMaps.setCurrentIndex(0)
    def connSubLeader_adjusting(self):
        self.tabSubLeader.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(1)
    def connSubLeader_items(self):
        self.tabSubLeader.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(2)
    def connSubPropFilter(self):
        self.tabSubProperties.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(1)
    def connSubPropResults(self):
        self.tabSubProperties.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def connSubanalysis_reports(self):
        self.tabSubAnalysis.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(0)
    def connSubAnalysis_DB(self):
        self.tabSubAnalysis.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def connSubWeb_filler(self):
        self.but_web_controler.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def connSubWeb_mail(self):
        self.but_web_controler.setCurrentIndex(2)
        self.tabMaps.setCurrentIndex(1)
    def connSubWeb_next(self):
        self.but_web_controler.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(1)
    def forward(self):
        self.setCurrentIndex(self.currentIndex() + 1)

    def backward(self):
        self.setCurrentIndex(self.currentIndex() - 1)
    
    def conntectTabs(self):
        if  self.button_planning.clicked:        
                self.tabWidget_left.setCurrentIndex(0)
                self.tabMaps.setCurrentIndex(1)    
        if  self.buttonKnowledge.clicked:
                self.tabWidget_left.setCurrentIndex(1)
                self.tabMaps.setCurrentIndex(0)
        if  self.button_analysis.clicked:
                self.tabWidget_left.setCurrentIndex(2)
                self.tabMaps.setCurrentIndex(0)
        if  self.buttonFiles.clicked:
                self.tabWidget_left.setCurrentIndex(3)
                self.tabMaps.setCurrentIndex(0)
        if  self.buttonWeb.clicked:
                self.tabWidget_left.setCurrentIndex(4)
                self.tabMaps.setCurrentIndex(0)
        if  self.Button_reporting.clicked:
                self.tabWidget_left.setCurrentIndex(5)
                self.tabMaps.setCurrentIndex(0)
    
    
    def reconnect(self,signal, newhandler=None, oldhandler=None):   
        self.listWebFilterLGItems.clearSelection()
        #self.listWebFilterLGItems.currentItemChanged.disconnect()

        #self.ButWebFilterFIllNames.clicked.disconnect()
        #self.ButWebFilterFIllData.clicked.disconnect()        
        while True:
            try:
                if oldhandler is not None:
                    signal.disconnect(oldhandler)
                else:
                    signal.disconnect()
            except TypeError:
                break
        if newhandler is not None:
            signal.connect(newhandler)
#    if connected:
 #       reconnect(self.ButWebFilterFIllNames.clicked.clicked, clickedList)
  #  else:
   #     reconnect(self.ButWebFilterFIllNames.clicked, clickedList2)        
        #time.sleep(10)
    def mailControl():
        '''for contorl to operating system and its contents from files and sub filess'''
        from apps import Mails_management
        
        Mails_management.send_emails("") 

    #___________________________analysis section_____________________________#
    def deepLearning(self):
        from leader import Ai_thinking
        
        data_path=Ai_thinking(r'E:\ProgramData\assistantApplcation','trainData.xlsx',"train","names","id_inside_cagegory","defined_names.xlsx","Sheet1")
        if self.checkBox_Leader_adjust_input_data.isChecked():
            data_path.show_data()

        if self.checkBox_Leader_adjust_network.isChecked():
            pass
        if self.checkBox_Leader_adjust_outout.isChecked():
            pass
        if self.checkBox_Leader_adjust_save.isChecked():
            pass
        if self.checkBox_Leader_adjust_train.isChecked():
            pass
        if self.checkBox_Leader_adjust_upooad.isChecked():
            pass

    #tabs_analysis(self):                

    #connect to database
    def dataIntry(self):
        from connectors import ModifyTableDialog
        
        
    def database_management(self):
        year=str(self.analysis_DByear.currentText())
        month=str(self.analysis_DBmonth.currentText())
        day=str(self.analysis_DBday.currentText())
        
        #_______________data base operations_________________________
                #uninstall restructor data bases#
        #prepare to uninstall
        if self.checkBox_analysis_db_uninstall_report.isChecked()== True:
            Block.uninstall_reports("1")#already must be uninstall first        
        
        if self.checkBox_analysis_DBuninstallRecord.isChecked():
        
                #uninstall cecords
            Block.uninstall_records("1")#choice2  warning all data will be lost
        if self.checkBox_analysis_DBuninstMaterial.isChecked():
            Block.uninstall_maretial("1")#choice2  warning all data will be lost

        #uninstall master data
        if self.checkBox_analysisDB_unin_masterData.isChecked():
            Block.uninstall_masterdata("1")#choice1
        
        if self.checkBox_analysis_DB_uninstal_infrastructure.isChecked():
            #uninstall infrastructure
            Block.uninstall_infrastrucure("")#choice3
        
        if self.checkBox_analysis_DB_deleteRows.isChecked():
            if str(self.comboBox_analysisDb_deleteType.currentText())=="day" : #for chose any type of files
                Block.delete_rows(self,"yt_quality",year,month,day)
            if str(self.comboBox_analysisDb_deleteType.currentText())=="month" : #for chose any type of files
                Block.delete_rows(self,"yt_quality",year,month)
                    #create restructure
        #install infrastructure
        if self.checkBox_analysis_DB_instal_infrastrucure.isChecked():
            Block.install_infrastrucure("1")
        
            #install master data
        if self.checkBox_analysis_DB_instal_masterData.isChecked():
            Block.install_master_data("1")
            #install records
        if self.checkBox_analysis_DB_instal_records.isChecked():
            Block.install_records("1")
                #finishng instalations
        if self.checkBox_analysis_DB_instalMateial.isChecked():
            Block.install_records_material("1")
        
        if self.checkBox_analysis_DB_instal_report.isChecked():
            Block.install_befor_reports_molds("")
            Block.install_befor_reports_parts("")
            Block.install_befor_reports_item_master("")
            Block.install_befor_reports_material("")
            Block.install_reports("")
    
    def connect_shareDb(self):
        #connect to database
        year=self.analysis_year.currentText()
        month=self.analysis_month.currentText()
        day=self.analysis_day.currentText()
        analysisInput=str(self.analsyisInputLineEdit.text())
        analysisOutput=str(self.analsyisInputLineEdit.text())

        
        #select date
                
        dailyReportName=str(year)+"-"+str(month)+"QC_molds_daily_archive_v3.xlsx"
        monthlyReportName=str(year)+"-"+str(month)+"QC_molds_monthly_v2.xlsx"

        upload_database=Block(r"\\AHMED-RASHAD\Users\Public\database","")

        #format_path2 = os.path.dirname(os.path.abspath(__file__))
        #format_path = os.path.join(format_path2, r".\apps\analysis\formats")
        format_path = os.path.normpath(r".\apps\analysis\formats")
        print ("format path",format_path)
        #format_path = os.path.join(format_path2, )

        git_database=Select(format_path,"formatQC_molds_monthly_v9.xlsx","output",year,month,'QC_molds_monthly_v2.xlsx',"Sheet1")
        
                    #import data
        #import database on share
        quality1=Select(r"\\AHMED-RASHAD\Users\Public\database","QC_daily_v2 - Copy.xlsx","input",year,month,"","")
        quality2=Select(r"\\AHMED-RASHAD\Users\Public\database","input_to_csv.xlsx","Sheet1",year,month,"input_to_database.csv","Sheet1")
        if self.checkBox_analysis_toCSV.isChecked()==True:
            if str(self.comboBox_analysisDb_convertCsv.currentText())=="quality_daily" : #for chose any type of files
                quality1.select_data(year,month,day,day=True,masterData=False)   #true for select alst day , false for select all month
                quality1.convert_csv(quality_records=True,masterData=False)
                print("convert csv quality for day:",day," month:",month," year:",year)
            if str(self.comboBox_analysisDb_convertCsv.currentText())=="quality_monthly" : #for chose any type of files
                quality1.select_data(year,month,day,day=False,masterData=False)
                quality1.convert_csv(quality_records=True,masterData=False)
                print("convert csv quality for month:",month," year:",year)

            if str(self.comboBox_analysisDb_convertCsv.currentText())=="material":
                quality1.convert_csv(material=True)
            if str(self.comboBox_analysisDb_convertCsv.currentText())=="masterData":
                quality1.select_data(year,month,day,masterData=True,quality_records=False)   #true for select alst day , false for select all month
                quality1.convert_csv(masterData=True,quality_records=False)

            self.comboBox_analysisDb_convertCsv#for swich on between monthly or day selection
        if self.checkBox_analysis_upload.isChecked():
            if str(self.comboBox_analysisDb_upload.currentText())=="quality_records":
                upload_database.import_quality_records()
                print("import quality records for day:",day," month:",month," year:",year)

            if str(self.comboBox_analysisDb_upload.currentText())=="material":
                upload_database.import_material_records()
            if str(self.comboBox_analysisDb_upload.currentText())=="infrastructure":
                upload_database.import_infrastructure()
                #iport master data
            if str(self.comboBox_analysisDb_upload.currentText())=="masterData_molds":#for swich on between recores or master data
                upload_database.import_masterdata_molds()
            if str(self.comboBox_analysisDb_upload.currentText())=="masterData_parts":#for swich on between recores or master data
                upload_database.import_masterdata_parts()

        ##erorr###### how close upload if there wr
        # 
        
                    #data basse export data
        #_______developer stage________________________________current_________====================


        
        if self.checkBox_analysis_DB_daily.isChecked():
        
        #for daily report
            print("year",type(year),"month",type(month),"day",type(day))
            git_database.export_report_mothly(dailyReportName,year,month,monthly=False)
            print("the daily report has downloaded for day ",day," , month:",month,"and year:",year)

        if self.checkBox_analysis_DB_monthlyReport.isChecked():
        
        #for monthly report
            git_database.export_report_mothly(monthlyReportName,year,month,monthly=True) #add output_batches for calculate items group by its continusliy production by RNN to learn brevious to get values
            print("the monthly report has downloaded for month:",month,"and year:",year)

        if self.checkBox_analysis_DB_yearlyInput.isChecked():
            git_database.export_report_daily_yearly(year)
            print("the yearly input report has downloaded for day ",day," , month:",month,"and year:",year)
        #git_database.export_report_daily_yearly()
        #upload_database.updateTable('yt_quality','shift1_production_cards',5,254,0)


        #____________________________________________________________________________________________
                            ##generate_data
        #capabilty study
        new_molds=Select(r".\data\capabilty_study","capabilty_study.xlsx","eye",year,month,"capabilty_study.xlsx","عين-")
        #(self,folder,readfile1,sheet1,writefile,writesheet):
        #new_molds_capabilty_study(394,102,117,3,"FMMINI30000042","كولدير ميلو -زوايا خلفي","11/04/2019")#(mold,lower weight, upper weight,eye_numbers,,code,name,date)

        #______________________________________________asistance operation______________________________
        #unique list for mold statistics or fix dublicat (folder,readfile,readsheet,column1,column2,writefile,sheetwriter)
        molds=Unique(self,analysisInput,"input","mold_name","machine_id","analyis_monthly.xls",4)
        #list_id.unique_list()
        #report_analysis()
        #database_output.convert_excel()
        #____append rows to another excel shet

        #add_lastday.copy_excel()
        yeary_append=Select(r"E:\work\programing\2data_analysis\files\yearly_report\molds\ct2018","9.xlsx","analysis",year,month,"2018.xlsx","c_t")
        #yeary_append.copy_workbooks()
        #append multy sheets in sperated workbooks
        sales_quality=Unique(r"E:\work\contact_group\QHSE_activation\QC quality control\returns","qc_return - daily2.xlsx","input_return","","","QC_returns.xlsx","sheet1")
        sceab_yearly=Select(r"E:\work\programing\data_analysis\files\yearly_report\molds","xlsx","scrap_input",year,month,"scrap_2018.xlsx","scrap_input")
        weights_yearly=Select(r"E:\work\programing\data_analysis\files\yearly_report\molds","xlsx","weights_input",year,month,"weights_2018.xlsx","weights_input")
        c_t_yearly=Select(r"E:\work\programing\data_analysis\files\yearly_report\molds","xlsx","c_t_input",year,month,"ct_2018.xlsx","c_t_input")
        sceab_10=Select(r"E:\work\programing\data_analysis\files\yearly_report\molds","xlsx","scrap_input",year,month,"scrap_2018.xlsx","scrap_input")
            
        if self.checkBox_analysis_returnReport.isChecked():           
            #sales_quality.returns_report()
            sales_quality.return_crosstab(year)
        #append multy sheets in same workbooks
        if self.checkBox_analysis_yearlyReport.isChecked():
            
            sceab_yearly.multi_workbook()
        #    def __init__(self,folder,readfile,readsheet,column1,column2,writefile,sheetwriter):
            
        
            item_master_all=Select(r"E:\work\programing\2data_analysis\files\master_data","warehouse2018.xlsx",None,year,month,"items_all.xlsx","sheet1")
            qc_yearly.multi_sheet()
    #___________________________________reports_from_PC_______________________________________
        query_output=Group(r'E:\work\contact_group\QHSE_activation\QC quality control\qc_molds\database','database_output.xlsx',"output",2020,2,"qc_analysis_monthly.xlsx","Sheet1")
        yearly_molds=Group(analysisInput,'QC_daily_v2.xlsx',"input",2020,2,"qc_analysis_yearly.xlsx","Sheet1")
        yearly_molds_sheet_from_database=Group(r'E:\work\contact_group\QHSE_activation\QC quality control\qc_molds','QC_molds_monthly_v2.xlsx',"output_monthly",2019,8,"qc_analysis_yearly.xlsx","Sheet1")
        yearly_molds18=Group(r'E:\work\contact_group\QHSE_activation\QC quality control\qc_molds2018','2018QC_molds_daily.xls',"input",2019,12,"qc_analysis_yearly2018_custom.xlsx","Sheet1")
        mothly_molds=Group(analysisInput,"QC_daily_v2.xlsx","input",2020,2,31,31)
        mold_data=Group(analysisInput,"drywtmonthly_sorce.xlsm","input",2019,1,"drywtmonthly_v2.xlsx","input")
        qc_daily=Group(analysisInput,"QC_daily_v2.xlsx","input","253","254",1,31)
        #if self.checkBox_analsys_monthlyreport.isChecked():
        if self.checkBox_analysis_summaryReport.isChecked():
            print ("checkBox_analysis_summaryReport",analysisInput)
            qc_daily.daily_molds(year,month,day)#____________________________________daily report______________________________
        if self.checkBox_analysis_spc.isChecked():
            item_id=int(self.comboBox_analysisDb_analysis_spc.currentText())    
            if self.comboBox_analysisDb_analysis_spc_move.currentText()=="new_workbook":
                qc_daily.spc_molds(int(year),int(month),item_id,create_workbook=True)
            if self.comboBox_analysisDb_analysis_spc_move.currentText()=="add_sheet":
                qc_daily.spc_molds(int(year),int(month),item_id,create_workbook=False)
            print("item_id,item_id","type",type(item_id))
        #____________________________________to upload data from pc______________________________
        query_output=Group(r'.\data\qc_molds\database','database_output.xlsx',"output",2020,2,"qc_analysis_monthly.xlsx","Sheet1")
        yearly_molds=Group(r'.\data\qc_molds','QC_daily_v2.xlsx',"input",2020,2,"qc_analysis_yearly.xlsx","Sheet1")
        yearly_molds_sheet_from_database=Group(r'.\data\qc_molds','QC_molds_monthly_v2.xlsx',"output_monthly",2019,8,"qc_analysis_yearly.xlsx","Sheet1")
        yearly_molds18=Group(r'.\data\qc_molds2018','2018QC_molds_daily.xls',"input",2019,12,"qc_analysis_yearly2018_custom.xlsx","Sheet1")
        mothly_molds=Group(r".\data\qc_molds","QC_daily_v2.xlsx","input",2020,2,31,31)

        quality1=Select(r".\data\qc_molds\database","QC_daily_v2 - Copy.xlsx",year,month,"input",2020,3)
        quality2=Select(r".\data\qc_molds\database","input_to_csv.xlsx",year,month,"Sheet1","input_to_database.csv","Sheet1")
        upload_database=Block(r".\data\qc_molds\database","QC_daily - Copy.xls")
        #group(folder,readfile,readsheet,column1,column2,writefile,writesheet)
        #quality1.select_data()
        #quality1.convert_csv()
    def test(self):
        import test_main
        year=self.analysis_year.currentText()
        month=self.analysis_month.currentText()
        day=self.analysis_day.currentText()
        test_scrab_input_baches=test_main.Apply_testAnalysis(int(year),int(month))
        test_scrab_input_baches.test_analysis_scrap()
    def files_control(self):
        '''for contorl to operating system and its contents from files and sub filess'''
        from apps import Files_control
        path=r"E:\work\contact_group\QHSE\block"
        outputpath=r"E:\work\contact_group\QHSE_activation\QES general\document control"
        if self.checkBox_FileControl_getfilesNames.isChecked():
            #Files_control.get_folders_list(path)
            Files_control.get_Files_names(path,outputpath)
        #______________________for convert files to pdf
        from apps import Convert
        #_________________________________pdf convertor_____________
        #_________________________warning___________________________
        #you must be copy your file to backup file becase any mistack you can't reback your files
        documentation=Convert(self.FileLocationInputLineEdit.text(),self.FileLocationOutputLineEdit.text())
        png=Convert(self.FileLocationInputLineEdit.text(),self.FileLocationOutputLineEdit.text())
        if self.checkBox_FileControl_Topdf.isChecked():
            documentation.convert_excel()
            documentation.convert_word()
            #specification.move_pdf()
            #png.convert_pdf_to_png()

        #_________warning________________
        #warning this order will be delet files , so you must be have a backup first( don't try without backup files)
        #
        #documentation.delete_files()
        #_______________________for rename excel sheets inside workbook
        from apps import Names 

        qc_names=Names(r'D:\2work\programing\2data_analysis\files\master_data','master_names.xlsx','sheets','new_names.xlsx','sheet1')
        #______________________for  merge tow files 
        from apps import Merge
        import os
        #for vlookup to connect tow sheets by one variable
        scrab=Merge(r"D:\2work\programing\data_analysis\files\yearly_report","id_specification",'item_specifications_v1.xlsx',"items_spec",'2018QC_molds_yearly_input2.xlsx',"scrap_input",'scrap_2018_2.xlsx','scrap_input')

        c_t=Merge(r"D:\2work\programing\data_analysis\files\yearly_report","id_specification",'item_specifications_v1.xlsx',"items_spec",'2018QC_molds_yearly_input2.xlsx',"ct_input",'ct_2018_2.xlsx','ct_input')

        dry_weight=Merge(r"D:\2work\programing\data_analysis\files\yearly_report","id_specification",'item_specifications_v1.xlsx',"items_spec",'2018QC_molds_yearly_input2.xlsx',"weights_input",'weights_2018_2.xlsx','weights_input')

        yearly2018=Merge(r"D:\2work\programing\data_analysis\files\master_data","product_name",'master_items.xlsx',"items_spec",'names_for_fix.xlsx',"sheet1",'molds_name_fixed.xlsx','Sheet1')

        #for unity tow sheets by tow variable ( not work until now)
        dryweight_scrab=Union(r"D:\programing\data_analysis\files\yearly_report","ID","day",'2018_dry_weight_connector.xls',"Sheet1",'2018_scrap_connector.xls',"Sheet1",'2018_input.xlsx','Sheet1')

        dryweight_ct=Union(r"D:\programing\data_analysis\files\yearly_report","ID","day",'2018-1_scrap_connector.csv',"Sheet1",'2018-1_c_t_connector.csv',"Sheet1",'2018_input.xlsx','Sheet1')


        items_master=Merge(r"D:\work\contact_group\Contact records\QC quality control\Foam\returns","return_reason",'qc_return - daily2.xlsx',"sheet1",'QC_returns.xlsx',"sheet1",'qc_return2.xlsx','Sheet1')
        if self.checkBox_FileControl_getUniqe.isChecked():


            #activate
            molds_master.vlookup()

            #scrab.vlookup()
        #______________________for copy files

        from apps import Direcories
        image_reports=copy.Direcories(r"H:\DCIM\Camera",r"D:\2work\contact_group\Contact records\08-QC quality control\Foam\qc_molds\2019\4",4,14)
        
        if self.secheckBox_FileControl_copyFiles.isChecked():

            image_reports.copy_files()

        #__________________resize Images
        if self.checkBox_FileControl_resizeImage.isChecked():       
            audit=r"C:\Backup\5s_photos\2020-10-5"
            audit.resize_image(audit)
from PyQt5.QtCore import pyqtSignal,QThread

universe_1 = [0 for i in range(512)]
if __name__ == "__main__":
        import sys
        
        app = QApplication(sys.argv)
        
        #app.setStyle(TabBarStyle())
        ex = AppWindow()
        
        sys.exit(app.exec_())