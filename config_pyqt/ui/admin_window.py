__author__ = 'youssri Ahmed Hamdy <estratigy@yahoo.com>'
__copyright__ = 'Copyright (c) 2021'
__version__ = '1.0.0'


from config_pyqt.setting import *

#from ui import Login

from config_pyqt.interface import Ui_MainWindow

data_path=r'D:\ProgramData\assistantApplcation'
class AppWindow(Ui_MainWindow,QMainWindow):  
    switch_window = QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(AppWindow,self).__init__(parent)
        self.setWindowTitle('Main Window')
        #self.Ui_MainWindow = Ui_MainWindow()
        self.setupUi(self)
        self.signals_control()
        self.show()
        self.deepLearning()
        
    def switch(self):
        self.switch_window.emit(self.line_edit.text())

    def signals_control(self):        
        from web.web import Connection
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
        self.butSubknowledge_tables.clicked.connect(self.connSubknowledge_tables)
        self.butSubknowledge_query.clicked.connect(self.connSubknowledge_query)
        self.butSubknowledge_data.clicked.connect(self.connSubknowledge_data)
        self.butSubknowledge_dataFlow.clicked.connect(self.connSubknowledge_dataFlow)
        self.butSubknowledge_tools.clicked.connect(self.connSubknowledge_formDesign)
        self.butSubknowledge_dataEntry.clicked.connect(self.connSubknowledge_dataEntry)

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
        self.listWebEmailSelect.currentItemChanged.connect(self.mailControl)
        self.butSubImportEmailSend.clicked.connect(self.connect_shareDb)
        self.ButWebMailBrowser.clicked.connect(self.getfiles)
    def mailControl(self,list):

        '''for contorl to operating system and its contents from files and sub filess'''
        from web.mails import Mails_management
        
        switcher_mail = {
        "shou_count_report":0,
        "quality_repot_report":1,
        "5s_followup":2,
        "followUp_Issues":3,
        "test:4":4,
        "followup-purchasing":5,
        "followup-production":6,
        "followup-wharehouse":7,
        "followup-quality":8,
        "followup-6october":9,
        "followup-safety":10,
        "followup-hr":11,
        }

        #self.ButWebFilterFIllNames.clicked.disconnect()
        
        Email_type = self.listWebEmailSelect.currentItem()

        if Email_type is None:
            print("kindly select the item form the items list")
        #if item is not None:
        else:
        
            x=switcher_mail.get(Email_type.text(), "Invalid items")
            print("now is printing","item:",Email_type.text(),"code:",x,"its type:",type(x))
            direction=self.ButWebFilter_fillingDirection.currentText()
        #______________
            attachment_name=self.WebSiteLineEdit_mail_address.text()
            
            #if self.ButWebEmail_sendDbReport.isChecked():
            #else:

            self.ButWebMailSend.clicked.connect(lambda:Mails_management.send_emails(x,attachment_name,))#year,month,day,to_day))
    #__________________________control panel
    def restart(self):        
        if __name__ == "__main__":
            
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
    #@QtCore.pyqtSlot()    
    
    def clickedList(self):
        from web import AutomatedFilling
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
        "LG75UP77Set":15,
        "LG75UP77Side":16,
        "LG43UP81":17,
        "LGNano80set":18,
        "LGNano80side":19,
        "LGOLED65A26LA_set":20,
        "OLED65A26LAside":21,
        "lg70UQ980updown":22,
        "lg70UQ980sides":23,

        "lg_OLED65CS_set":24,
        "lg_OLED65CS_sides":25,
        "OLED55CS_set":26,
        "OLED55CS_side":27,

        "LgWasherCover":28,
        "LgWasherAngels":29,
        "LgWasherBase":30,
        "LgWasherBase_VIVACHE":31,

        "lg_slides_50UQ75":32
        }

        #self.ButWebFilterFIllNames.clicked.disconnect()
        
        item = self.listWebFilterLGItems.currentItem()

        if item is None:
            print("kindly select the item form the items list")
        #if item is not None:
        else:
        
            x=switcher.get(item.text(), "Invalid items")
            print("now is printing","item:",item.text(),"code:",x,"its type:",type(x))
            direction=self.ButWebFilter_fillingDirection.currentText()
            self.ButWebFilterFIllNames.clicked.connect(lambda:AutomatedFilling.past_form(x,fill_data=False,insert_name=True,vertically=False,))
            if direction=="vertically":
                self.ButWebFilterFIllData.clicked.connect(lambda:AutomatedFilling.past_form(x,fill_data=True,standard_spec=False,vertically=False,))
            elif direction=="horizontal":
                self.ButWebFilterFIllData.clicked.connect(lambda:AutomatedFilling.past_form(x,fill_data=True,standard_spec=False,vertically=True,))
            elif direction=="standards":
                self.ButWebFilterFIllData.clicked.connect(lambda:AutomatedFilling.past_form(x,fill_data=True,standard_spec=True,vertically=True,))
            self.listWebFilterLGItems.clearSelection()
            #print(map(x,switcher))   
            #self.close()
    


    def getfiles(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath() ,)# '*.xlsx')
        self.WebSiteLineEdit_mail_address.setText(fileName)

    def conntectTabs(self):
        self.tabWidget_left.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(1)    
    def conntectTabs0(self):
        self.tabWidget_left.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(1)
    def conntectTabs1(self):#knowledge
        self.tabWidget_left.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
        #from pyqt_sqlite import MainWindow
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
    def connSubknowledge_tables(self):
        self.gridTabWidget.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(1)
    def connSubPropResults(self):
        self.gridTabWidget.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def connSubknowledge_tables(self):
        self.gridTabWidget.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(0)
    def connSubknowledge_query(self):
        self.gridTabWidget.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def connSubknowledge_data(self):
        self.gridTabWidget.setCurrentIndex(2)
        self.tabMaps.setCurrentIndex(0)
    def connSubknowledge_dataFlow(self):
        self.gridTabWidget.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def connSubknowledge_formDesign(self):
        self.gridTabWidget.setCurrentIndex(3)
        self.tabMaps.setCurrentIndex(0)
    def connSubknowledge_dataEntry(self):
        self.gridTabWidget.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def connSubanalysis_reports(self):
        self.tabSubAnalysis.setCurrentIndex(0)
        self.tabMaps.setCurrentIndex(0)
    def connSubAnalysis_DB(self):
        self.tabSubAnalysis.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def connSubWeb_filler(self):
        self.but_web_controler_2.setCurrentIndex(1)
        self.tabMaps.setCurrentIndex(0)
    def connSubWeb_mail(self):
        self.but_web_controler_2.setCurrentIndex(2)
        self.tabMaps.setCurrentIndex(1)
    def connSubWeb_next(self):
        self.but_web_controler_2.setCurrentIndex(0)
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
    
    #___________________________analysis section_____________________________#
    def deepLearning(self):
        from leader import Ai_thinking
        
        
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
        from Lib import ModifyTableDialog

    def database_management(self):
        from analysis import Block,PgAccess,MoldsQuality
        
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
        
            #uninstall data entry
        if self.checkBox_analysis_db_uninstall_report_dataentry_views.isChecked():
            MoldsQuality.uninstall_dataentry_reports(self)
        if self.checkBox_analysis_db_uninstall_report_dataentry_records.isChecked():
            MoldsQuality.uninstall_dataentry_views(self)
        
        if self.checkBox_analysis_DB_deleteRows.isChecked():
            if str(self.comboBox_analysisDb_deleteType.currentText())=="day" : #for chose any type of files
                PgAccess.delete_rows(self,"t10quality_inpsection",year,month,day,monthly=False)
            if str(self.comboBox_analysisDb_deleteType.currentText())=="month" : #for chose any type of files
                PgAccess.delete_rows(self,"t10quality_inpsection",year,month,monthly=True)
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
            Block.install_calculation_viws("")
            Block.install_befor_reports_molds("")
            Block.install_befor_reports_parts("")
            Block.install_befor_reports_item_master("")
            
            Block.install_befor_reports_material("")
            
            Block.install_reports("")
            
        if self.checkBox_analysis_DB_instal_report_dataentry_records.isChecked():
            MoldsQuality.install_tables_machine_loaded(self)
        if self.checkBox_analysis_DB_instal_report_dataentry_views.isChecked():
            MoldsQuality.install_views_machine_loaded(self)

    #_______________tables Operation_________________________
        old_column=str(self.analsyisDb_columnName.text())
        new_column=str(self.analsyisDb_columnNew.text())
        category=str(self.analsyisDb_tableName.text())
        
        if str(self.analysisDb_combo_object.currentText())=="table" : #for chose any type of files
            if str(self.analysisDb_combo_altertables.currentText())=="select" : #for chose any type of files
                PgAccess.select_tables(self,category,old_column)
        if str(self.analysisDb_combo_object.currentText())=="column" : #for chose any type of files
            if str(self.analysisDb_combo_altertables.currentText())=="add" : #for chose any type of files
                PgAccess.add_columns(self,category,old_column,new_column)
        if str(self.analysisDb_combo_object.currentText())=="column" : #for chose any type of files
            if str(self.analysisDb_combo_altertables.currentText())=="delete" : #for chose any type of files
                PgAccess.drop_columns(self,category,old_column)
        
        if str(self.analysisDb_combo_object.currentText())=="column" : #for chose any type of files
            if str(self.analysisDb_combo_altertables.currentText())=="alter type" : #for chose any type of files
                PgAccess.alterTybe_columns(self,category,old_column,new_column)
        
        if str(self.analysisDb_combo_object.currentText())=="column" : #for chose any type of files
            if str(self.analysisDb_combo_altertables.currentText())=="alter name" : #for chose any type of files
                PgAccess.alterName_columns(self,category,old_column,new_column)

    def connect_shareDb(self):
        from analysis import Unique,Select,Group,Block
        
        #connect to database
        year=self.analysis_year.currentText()
        month=self.analysis_month.currentText()
        day=self.analysis_day.currentText()
        to_day=self.analysis_day_to.currentText()
        analysisInput=str(self.analsyisInputLineEdit.text())
        analysisOutput=str(self.analsyisIOutputLineEdit.text())
        data_uplaod_local_pc=str(self.analsyisLineEdit_analysisDb_server_address.text())
        DATAFOLDER_ON_NETWORK=r"\\AHMED-ALY\Users\Public\database"

        #select date                
        dailyReportName=str(year)+"-"+str(month)+"QC_molds_daily_archive_v3.xlsx"
        monthlyReportName=str(year)+"-"+str(month)+"QC_molds_monthly_v3.xlsx"
        yearlyReportName=str(year)+"QC_molds_yearly_v3.xlsx"
        format_path = os.path.join(BASE_DIR, os.path.normpath(r".\analysis\formats"))
        #______________________________________________________________________________________
        #to send emails from db to outlook
       #______________________________________________________________________________________ 
        
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        #to cahnge folder uploading data
        if str(self.comboBox_analysisDb_server_select.currentText())=="network" : #for select netowrk server in close site
            data_store=DATAFOLDER_ON_NETWORK
        elif str(self.comboBox_analysisDb_server_select.currentText())=="network test" : #for select netowrk server in close site
            data_store=DATAFOLDER_ON_NETWORK
        else :
            data_store=data_uplaod_local_pc
        
        #format_path = os.path.join(BASE_DIR, os.path.normpath(__file__))
        upload_database=Block(data_store,"")
        print ("format path",format_path)
        #format_path = os.path.join(format_path2, )
        
        git_database=Select(format_path,"formatQC_report_monthly_v3.xlsx","output",year,month,'QC_molds_monthly_v2.xlsx',"Sheet1")
        
                    #import data
        #import database on share
        quality1=Select(data_store,"QC_daily_v2 - Copy.xlsx","input",year,month,"","")
        quality2=Select(data_store,"input_to_csv.xlsx","Sheet1",year,month,"input_to_database.csv","Sheet1")
        if self.checkBox_analysis_toCSV.isChecked()==True:
            if str(self.comboBox_analysisDb_convertCsv.currentText())=="quality_daily" : #for chose any type of files
                quality1.select_data(year,month,day,day=True,masterData=False)   #true for select alst day , false for select all month
                quality1.convert_csv(quality_records=True,masterData=False,material=False)
                print("convert csv quality for day:",day," month:",month," year:",year)
            if str(self.comboBox_analysisDb_convertCsv.currentText())=="quality_monthly" : #for chose any type of files
                quality1.select_data(year,month,day,day=False,monthly=True,masterData=False)
                quality1.convert_csv(quality_records=True,masterData=False,material=False)
                print("convert csv quality for month:",month," year:",year)
            if str(self.comboBox_analysisDb_convertCsv.currentText())=="quality_yearly" : #for chose any type of files
                quality1.select_data(year,month,day,day=False,monthly=False,yearly=True,masterData=False)
                quality1.convert_csv(quality_records=True,masterData=False,material=False)
                print("convert csv quality for month:",month," year:",year)
            if str(self.comboBox_analysisDb_convertCsv.currentText())=="quality_all" : #for chose any type of files
                quality1.select_data(year,month,day,day=False,monthly=False,yearly=True,masterData=False)
                quality1.convert_csv(quality_records=True,masterData=False,material=False)
            if str(self.comboBox_analysisDb_convertCsv.currentText())=="material":
                quality1.convert_csv(material=True,masterData=False)
            if str(self.comboBox_analysisDb_convertCsv.currentText())=="masterData":
                quality1.select_data(year,month,day,masterData=True,quality_records=False)   #true for select alst day , false for select all month
                quality1.convert_csv(masterData=True,quality_records=False,material=False)

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
#if self.checkBox_analsys_monthlyreport.isChecked():
        if self.checkEmailSendDbReport.isChecked():   #to send this email via report
            list=git_database.monthly_molds(dailyReportName,year,month,day,to_day,monthly=False,daily=True)
            print ("checkBox_analysis_summaryReport start",analysisInput)
            self.mailControl(list)
        if self.checkBox_analysis_summaryReport.isChecked():
            pass
            #git_database.monthly_molds(dailyReportName,year,month,day,to_day,monthly=False,daily=True)
            
            #qc_daily.daily_molds(year,month,day)#____________________________________daily report______________________________
        if self.checkBox_analysis_spc.isChecked():
            item_id=int(self.comboBox_analysisDb_analysis_spc.currentText())    
            if self.comboBox_analysisDb_analysis_spc_move.currentText()=="new_workbook":
                qc_daily.spc_molds(int(year),int(month),item_id,create_workbook=True)
            if self.comboBox_analysisDb_analysis_spc_move.currentText()=="add_sheet":
                qc_daily.spc_molds(int(year),int(month),item_id,create_workbook=False)
            print("item_id,item_id","type",type(item_id))
    
        if self.checkBox_analysis_DB_daily.isChecked():
        
        #for daily report
            print("year",type(year),"month",type(month),"day",type(day))
            git_database.monthly_molds(dailyReportName,year,month,day,to_day,monthly=False,daily=True)
            print("the daily report has downloaded for day ",day," , month:",month,"and year:",year)

        if self.checkBox_analysis_DB_monthlyReport.isChecked():
        
        #for monthly report
            git_database.monthly_molds(monthlyReportName,year,month,day,to_day,monthly=True,daily=False) #add output_batches for calculate items group by its continusliy production by RNN to learn brevious to get values
            print("the monthly report has downloaded for month:",month,"and year:",year)

        if self.checkBox_analysis_DB_yearlyInput.isChecked():
            #git_database.export_report_daily_yearly(year,month,day,to_day)
            git_database.monthly_molds(yearlyReportName,year,month,day,to_day,monthly=False,daily=False)
            print("the yearly report has downloaded for year:",year)

        if self.checkBox_analysis_DB_weekly.isChecked()==True:
            if str(self.comboBox_analysisDb_weeklyChoices.currentText())=="quweekly production" : #for chose any type of files
                git_database.export_report_daily_yearly(self,year,month,day,to_day)
                print("download production report from day:",day,"to day :",to_day," month:",month," year:",year)
            if str(self.comboBox_analysisDb_weeklyChoices.currentText())=="weekly defect" : 
                git_database.export_report_daily_yearly(year,day,to_day)
                print("download defects report from day:",day,"to day :",to_day," month:",month," year:",year)
            if str(self.comboBox_analysisDb_weeklyChoices.currentText())=="shout_count" : 
                git_database.monthly_molds(dailyReportName,year,month,day,to_day,monthly=False,daily=False,weekly=True)
                
                print("download shout count report from day:",day,"to day :",to_day," month:",month," year:",year)
        #____________________________________________________________________________________________
                            ##generate_data
        #capabilty study
        new_molds=Select(r".\data\capabilty_study","capabilty_study.xlsx","eye",year,month,"capabilty_study.xlsx","عين-")
        
        #______________________________________________asistance operation______________________________
        #unique list for mold statistics or fix dublicat (folder,readfile,readsheet,column1,column2,writefile,sheetwriter)
        molds=Unique(self,analysisInput,"input","mold_name","machine_id","analyis_monthly.xls",4)
               
        sales_quality=Unique(analysisOutput,"qc_return - daily2.xlsx","input_return","","","QC_returns.xlsx","sheet1")
        print ("analysis Output",analysisOutput)
    
        if self.checkBox_analysis_returnReport.isChecked():           
            if str(self.comboBox_analysisDb_returnReportChoices.currentText())=="monthly" : #from database
                Block.returnProducts(self,year,month)
                print("download return report from  month:",month," year:",year)
            if str(self.comboBox_analysisDb_returnReportChoices.currentText())=="yearly" : #from excel sheets
            #sales_quality.returns_report()
                sales_quality.return_crosstab(year)

        #append multy sheets in same workbooks
        if self.checkBox_analysis_yearlyReport.isChecked():
            sceab_yearly.multi_workbook()
            item_master_all=Select(r"E:\work\programing\2data_analysis\files\master_data","warehouse2018.xlsx",None,year,month,"items_all.xlsx","sheet1")
            qc_yearly.multi_sheet()
    #___________________________________reports_from_PC_______________________________________
        #query_output=Group(r'E:\work\contact_group\QHSE_activation\QC quality control\qc_molds\database','database_output.xlsx',"output",2020,2,"qc_analysis_monthly.xlsx","Sheet1")
        #yearly_molds=Group(analysisInput,'QC_daily_v2.xlsx',"input",2020,2,"qc_analysis_yearly.xlsx","Sheet1")
        #yearly_molds_sheet_from_database=Group(r'E:\work\contact_group\QHSE_activation\QC quality control\qc_molds','QC_molds_monthly_v2.xlsx',"output_monthly",2019,8,"qc_analysis_yearly.xlsx","Sheet1")
        #yearly_molds18=Group(r'E:\work\contact_group\QHSE_activation\QC quality control\qc_molds2018','2018QC_molds_daily.xls',"input",2019,12,"qc_analysis_yearly2018_custom.xlsx","Sheet1")
        #mothly_molds=Group(analysisInput,"QC_daily_v2.xlsx","input",2020,2,31,31)
        #mold_data=Group(analysisInput,"drywtmonthly_sorce.xlsm","input",2019,1,"drywtmonthly_v2.xlsx","input")
        qc_daily=Select(analysisInput,"QC_daily_v2.xlsx","input","253","254",1,31)
        
    def test(self):
        import test_main
        year=self.analysis_year.currentText()
        month=self.analysis_month.currentText()
        day=self.analysis_day.currentText()
        to_day=self.analysis_day_to.currentText()
        test_scrab_input_baches=test_main.Apply_testAnalysis(int(year),int(month))
        test_scrab_input_baches.test_analysis_scrap()
    def files_control(self):
        '''for contorl to operating system and its contents from files and sub filess'''
        from files import Files_control
        #path=r"E:\work\contact_group\QHSE\block"
        #outputpath=r"E:\work\contact_group\QHSE_activation\QES general\document control"
        path=self.FileLocationInputLineEdit.text()
        outputpath=self.FileLocationOutputLineEdit.text()
        if self.checkBox_FileControl_getfilesNames.isChecked():
            if str(self.comboBox_FileControl_output_type.currentText())=="folders and sub files" : #for chose any type of files
                Files_control.get_folders_list(path,outputpath)
            else:
                Files_control.get_Files_names(path,outputpath)
        #______________________for convert files to pdf
        from files import Convert
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
        if self.checkBox_FileControl_deletFiles.isChecked():
            documentation.delete_files()
        #_________warning________________
        #warning this order will be delet files , so you must be have a backup first( don't try without backup files)
        #
        #documentation.delete_files()
        #_______________________for rename excel sheets inside workbook
        from files import Names 

        qc_names=Names(r'D:\2work\programing\2data_analysis\files\master_data','master_names.xlsx','sheets','new_names.xlsx','sheet1')
        #______________________for  merge tow files 
        from files import Merge
        import os
        #for vlookup to connect tow sheets by one variable
        scrab=Merge(r"D:\2work\programing\data_analysis\files\yearly_report","id_specification",'item_specifications_v1.xlsx',"items_spec",'2018QC_molds_yearly_input2.xlsx',"scrap_input",'scrap_2018_2.xlsx','scrap_input')

        c_t=Merge(r"D:\2work\programing\data_analysis\files\yearly_report","id_specification",'item_specifications_v1.xlsx',"items_spec",'2018QC_molds_yearly_input2.xlsx',"ct_input",'ct_2018_2.xlsx','ct_input')

        dry_weight=Merge(r"D:\2work\programing\data_analysis\files\yearly_report","id_specification",'item_specifications_v1.xlsx',"items_spec",'2018QC_molds_yearly_input2.xlsx',"weights_input",'weights_2018_2.xlsx','weights_input')

        yearly2018=Merge(r"D:\2work\programing\data_analysis\files\master_data","product_name",'master_items.xlsx',"items_spec",'names_for_fix.xlsx',"sheet1",'molds_name_fixed.xlsx','Sheet1')

        items_master=Merge(r"D:\work\contact_group\Contact records\QC quality control\Foam\returns","return_reason",'qc_return - daily2.xlsx',"sheet1",'QC_returns.xlsx',"sheet1",'qc_return2.xlsx','Sheet1')
        if self.checkBox_FileControl_getUniqe.isChecked():
            

            #activate
            #molds_master.vlookup()

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


    universe_1 = [0 for i in range(512)]

        #____for translation