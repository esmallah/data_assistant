'''this module for the data was emported from database analysis'''
import csv
import pandas as pd
import openpyxl as xl
from openpyxl import load_workbook

import os
import numpy as np
import glob

from memory import Block,Material,cursor
#import database_postgrsql as database


from random import randint,seed

#master data
    #for columns from ite_ master for molds ( the one product from one moldes)
columns_machines=['id','scrabe_standard','machine_type','place' ,'low_size','high_size']

columns_molds=['mold_id','ORG_CODE','ORG_NAME','Ctegory','UOM','machie_size','No_on_Set',
'set',"sub_category",'mold_name','status','c_t_standard_per_second','c_t_standard_per_second_from',
'c_t_standard_per_second_to',"view_molds",
'gap_mm','injekors_numbers','drummers_number','customer_id','playback','gap_tolerance',
'gap_mm_from','gap_mm_to','machine_parameter_id','mold_start_date','mold_expire_date',"customer_name","company_of_customer",
"customer_proberty_name","customer_proberty_sequence","customer_asset_code","Customer_Product_Group"]
 
#for columns to more than one products form the same mold
columns_parts=['part_id','product_code','product_name_by_parts','Weight_kg','standard_rate_hour','highlite',
    'standard_dry_weight','standard_dry_weight_from','standard_dry_weight_to','positive_weight','negative_weight',
    'sub_category','mold_id','product_parts','item_id','product_name','item_name_customers','item_code_customers','item_classification_customers'
    ,"view_items","view_molds",
    'view_parts','density','row_material_typeA','row_material_typeB',
    'tall_mm','tall_positive_tolerance','tall_negative_tolerance','width_mm','width_positive_tolerance','width_negative_tolerance',
    'sicness_mm','sicness_positive_tolerance','sicness_negative_tolerance','id_printed_specification','spec_folder_no',
    'page_volum_x','page_volum_y','page_volum_z','volume','sitotb_color','sitotb_set','silotib_meter_reels',
    'silotib_outside_meter','package_page','number_bacage','page_size_x','page_size_y','page_colore','pages_kgm_set','pages_kgm',
    'kg_after_add12percent','kg_after_add8_5percent','id_modification','notes','silotib_inside_meter']

#prepare data entering tables
    #3collecting tables ct,weight and scrap(yt_quality)
columns_quality=['year',
    'month',
    'day',
    'machine_id',
    'item_id',
    'number_day_use',
    'mold_id',
    'product_parts'
    ,'shift1_wet_weight1',
    'shift1_wet_weight2',
    'shift1_wet_weight3',
    'shift1_wet_weight4',
    'shift1_wet_weight5'
    ,'shift1_dry_weight1','shift1_dry_weight2','shift1_dry_weight3','shift1_dry_weight4','shift1_dry_weight5',
    'shift1_c_t1','shift1_c_t2',
    'shift2_wet_weight1','shift2_wet_weight2','shift2_wet_weight3','shift2_wet_weight4','shift2_wet_weight5',
    'shift2_dry_weight1','shift2_dry_weight2','shift2_dry_weight3','shift2_dry_weight4','shift2_dry_weight5',
    'shift2_c_t1','shift2_c_t2'

    ,'average_dry_weight','average_wet_weight','rat_actually','rat_validation','c_t_actually','shift1_production_cards'
    ,'shift1_prod_page','shift1_proper_production','shift1_scrabe_shortage','shift1_scrabe_roll','shift1_scrabe_broken',
    'shift1_scrabe_curve','shift1_scrabe_shrinkage','shift1_scrabe_dimentions','shift1_scrabe_weight','shift1_scrabe_dirty'
    ,'shift1_scrabe_cloration','shift1_scrabe_no_parts','shift1_scrabe_no_item','shift1_all_production'
    ,'shift2_production_cards','shift2_prod_page','shift2_proper_production','shift2_scrabe_shortage',
    'shift2_scrabe_roll','shift2_scrabe_broken','shift2_scrabe_curve','shift2_scrabe_shrinkage','shift2_scrabe_dimentions'
    ,'shift2_scrabe_weight','shift2_scrabe_dirty','shift2_scrabe_cloration','shift2_scrabe_no_parts','shift2_scrabe_no_item'
    ,'shift2_all_production'
    ,'sum_scrabe_shortage_bySet','sum_scrabe_roll_bySet','sum_scrabe_broken_bySet'
    ,'sum_scrabe_curve_bySet','sum_scrabe_shrinkage_bySet','sum_scrabe_dimentions_bySet','sum_scrabe_weight_bySet','sum_scrabe_dirty_bySet',
    'sum_scrabe_cloration_bySet','sum_scrabe_no_parts','number_scrab_by_item',
    'gross_production','scrap_percent_by_item','part_id','factory','scrab_ncr_reason'
    ,'ct_ncr_reason','weight_ncr_reason','id_DayPartUnique','parts_patchsNumbers','Items_patchsNumbers','bachStartDate',
    'date_day','bachEndDate']
    
    #the previous columns separate to 
        #1 cycle time table
columns_cycle_time=['year','month','day','machine_id','rat_actually','rat_validation','c_t_deviation','shift1_c_t1','shift1_c_t2'
                ,'shift2_c_t1','shift2_c_t2','c_t_actually','mold_id','part_id','item_id','number_day_use','factory','ct_ncr_reason','id_DayPartUnique'
                ,'parts_patchsNumbers','Items_patchsNumbers','bachStartDate','bachEndDate']

        #2 quality inspections scrap and weights
columns_QCinspection=['year','month','day','machine_id','item_id','number_day_use','mold_id','product_parts',
    'shift1_wet_weight1','shift1_wet_weight2','shift1_wet_weight3','shift1_wet_weight4','shift1_wet_weight5',
    'shift1_dry_weight1',    'shift1_dry_weight2','shift1_dry_weight3','shift1_dry_weight4','shift1_dry_weight5','shift1_ct1','shift1_ct2',
    'shift2_wet_weight1','shift2_wet_weight2','shift2_wet_weight3','shift2_wet_weight4','shift2_wet_weight5',
    'shift2_dry_weight1','shift2_dry_weight2','shift2_dry_weight3','shift2_dry_weight4','shift2_dry_weight5',

    'shift2_ct1','shift2_ct2'

    ,'average_wet_weight','average_dry_weight','rat_actually','rat_validation','dryweight_deviation_validation','part_id','shift1_production_cards'
    ,'shift1_prod_page','shift1_proper_production','shift1_scrabe_shortage','shift1_scrabe_roll','shift1_scrabe_broken',
    'shift1_scrabe_curve','shift1_scrabe_shrinkage','shift1_scrabe_dimentions','shift1_scrabe_weight','shift1_scrabe_dirty'
    ,'shift1_scrabe_cloration','shift1_scrabe_no_parts','shift1_scrabe_no_item'
    ,'shift1_all_production'

    ,'shift2_production_cards','shift2_prod_page','shift2_proper_production','shift2_scrabe_shortage',
    'shift2_scrabe_roll','shift2_scrabe_broken','shift2_scrabe_curve','shift2_scrabe_shrinkage','shift2_scrabe_dimentions'
    ,'shift2_scrabe_weight','shift2_scrabe_dirty','shift2_scrabe_cloration','shift2_scrabe_no_parts','shift2_scrabe_no_item'
    ,'shift2_all_production'

    
    ,'bachStartDate'


    'sum_scrabe_shortage_bySet','sum_scrabe_roll','sum_scrabe_broken'
    ,'sum_scrabe_curve','sum_scrabe_shrinkage','sum_scrabe_dimentions','sum_scrabe_weight','sum_scrabe_dirty_bySet',
    'sum_scrabe_cloration','sum_scrabe_no_parts','number_scrab_by_item',
    'gross_production','scrap_percent_by_item','scrap_weight_kg','production_weight_kg','id_DayPartUnique','factory','scrab_ncr_reason'
    ,'weight_ncr_reason','parts_patchsNumbers','Items_patchsNumbers','bachStartDate','bachEndDate']

            #the previeuse table separate to
                    #1weights table
columns_weight=['year','month','day','machine_id','item_id','number_day_use','mold_id','product_parts',
'shift1_dry_weight1','shift1_dry_weight2','shift1_dry_weight3','shift1_dry_weight4'
,'shift1_dry_weight5','shift2_dry_weight1','shift2_dry_weight2','shift2_dry_weight3','shift2_dry_weight4',
'shift2_dry_weight5','average_wet_weight','average_dry_weight','dryweight_deviation_validation','part_id','id_DayPartUnique','factory'
,'weight_ncr_reason','parts_patchsNumbers','Items_patchsNumbers','bachStartDate','bachEndDate']

                    #2scrab table
columns_scrap=['year','month','day','machine_id','item_id','mold_id','product_parts','part_id','shift1_production_cards'
,'shift1_prod_page','shift1_proper_production','shift1_scrabe_shortage','shift1_scrabe_roll','shift1_scrabe_broken',
'shift1_scrabe_curve','shift1_scrabe_shrinkage','shift1_scrabe_dimentions','shift1_scrabe_weight','shift1_scrabe_dirty'
,'shift1_scrabe_cloration','shift1_scrabe_no_parts','shift1_scrabe_no_item','shift1_all_production'
,'shift2_production_cards','shift2_prod_page','shift2_proper_production','shift2_scrabe_shortage',
'shift2_scrabe_roll','shift2_scrabe_broken','shift2_scrabe_curve','shift2_scrabe_shrinkage','shift2_scrabe_dimentions'
,'shift2_scrabe_weight','shift2_scrabe_dirty','shift2_scrabe_cloration','shift2_scrabe_no_parts','shift2_scrabe_no_item'
,'shift2_all_production','sum_scrabe_shortage_bySet','sum_scrabe_roll_bySet','sum_scrabe_broken_bySet'
,'sum_scrabe_curve_bySet','sum_scrabe_shrinkage_bySet','sum_scrabe_dimentions_bySet','sum_scrabe_weight_bySet','sum_scrabe_dirty_bySet',
'sum_scrabe_cloration_bySet','sum_scrabe_no_parts','number_scrab_by_item',
'gross_production','scrap_percent_by_item','factory','scrab_ncr_reason','id_DayPartUnique','Items_patchsNumbers'
,'parts_patchsNumbers','bachStartDate','bachEndDate']

#error __________________
#must be reduce column by ceate calculating columns

class Unique():
    def __init__(self,folder,readfile,readsheet,column1,column2,writefile,sheetwriter):
        #self.folder=folder
        self.folder=folder
        self.readfile=readfile
        self.readsheet=readsheet
        self.column1=column1
        self.column2=column2
        self.writefile=writefile
        self.sheetwriter=sheetwriter
    
    def unique_list(self):
        ''' to get unique data in any excel sheet'''
        os.chdir(self.folder)
        reader=pd.read_excel(self.readfile,self.readsheet)
        data=reader[[self.column1,self.column2]]
        
        unique_data=data.groupby(self.column1)[self.column2].count()
        writer = pd.ExcelWriter(self.writefile)
        
        unique_data.to_excel(writer,self.sheetwriter)
        writer.save()
    def item_master(self):
        '''for create item master from table item_master.exe'''
        os.chdir(self.folder)
        reader=pd.read_excel(self.readfile,self.readsheet)
        data=reader[columns_molds]
        unique_data=data.groupby(columns_molds)[self.column2].count()

        writer = pd.ExcelWriter(self.writefile)
        print(writer)
        unique_data.to_excel(writer,self.sheetwriter)
        writer.save()
    def report_analysis(self):
        os.chdir(self.folder)
        
        reader3=pd.read_excel(self.readfile,self.readsheet)
        last_year=reader3["year"].max()
        reader2_bool=reader3["year"]==last_year
        reader2=reader3[reader2_bool]
        last_month=reader2["month"].max()
        reader2_bool=reader2["month"]==self.sheetwriter
        reader=reader2[reader2_bool]
        unique_data=reader.groupby(self.column1)[self.column2].count()
        analysis_data=reader.groupby(self.column1)[self.column2].describe()
        
        #weights analsysis
        molds_weight_bool2=reader["average_dry_weight"]<reader["standard_dry_weight_from"]
        molds_weight3=reader[molds_weight_bool2]
        molds_weight_bool=molds_weight3["average_dry_weight"]>molds_weight3["standard_dry_weight_to"]
        molds_weight2=molds_weight3[molds_weight_bool]
        molds_weight_ncr=molds_weight2.groupby("mold_name")["average_dry_weight"].mean()

        #scrap analsysis
        reader["scrap_percent_by_set_all"]=reader['number_scrab_by_item']/reader['gross_production']
        molds_scrap_bool=reader["scrabe_standard"]<reader["scrap_percent_by_set_all"]
        molds_scrap2=reader[molds_scrap_bool]
        molds_scrap_ncr=molds_scrap2.groupby("mold_name")["gross_production","number_scrab_by_item","sum_scrabe_no_parts"].sum()

        #ct analsysis
        molds_ncr_rat_bool=reader["rat_actually"]<reader["standard_rate_hour"]
        molds_ncr_rat2=reader[molds_ncr_rat_bool]
        molds_ncr_rat=reader.groupby("mold_name")["rat_actually","c_t_actually"].mean()

        writer = pd.ExcelWriter(self.writefile)
        print(writer)
        unique_data.to_excel(writer,"Sheet1")
        analysis_data.to_excel(writer,"analysis")
        molds_ncr_rat.to_excel(writer,"molds_ncr_rat")
        molds_weight_ncr.to_excel(writer,"molds_weight_ncr")
        molds_scrap_ncr.to_excel(writer,"molds_scrap_ncr")
        writer.save()
    def returns_report(self):
        os.chdir(self.folder)
        reader=pd.read_excel(self.readfile,self.readsheet)
        return_day_bool=reader["month"]==self.column1
        return_day=reader[return_day_bool]
        unique_data=return_day.groupby(self.column2).sum()
        writer = pd.ExcelWriter(self.writefile)
        print(writer)
        unique_data.to_excel(writer,self.sheetwriter)
        writer.save()
    
    def return_crosstab(self,year,**customer):
        print("_____________return report________________")
        '''for get dtata form qc return'''
        os.chdir(self.folder)

        #for development this function in this erea>> git data from database for mix warehouse data with quality data
        reader_data=pd.read_excel(self.readfile,self.readsheet)
        last_year=reader_data["year"].max()
        reader2_bool=reader_data["year"]==last_year
        reader2=reader_data[reader2_bool]
        reader_filter_year=reader2[reader2["year"]==last_year]
        
        reader=reader_filter_year
        #reader=reader_filter_year[reader_filter_year["customer_name"]=="customer"]
        #reader=reader_filter_year[reader_filter_year["product_type"]=="xps"]
        
        df = pd.DataFrame(reader, columns = ['customer_name','customer_name_category', 'product_name', 'product_code', 'year',
         'month', 'date',"gross_quantity","return_quantity","scrap","return_reason",'inspection_results_proper','inspection_results_low_grade',
         'product_type','reason_category','lenth','width','denesity'])
        
        sheets=['customer_name', 'product_name','product_type']
        print("________________test_______________")
        print(df.reason_category)
        #for development this function in this erea>> git output by all delivers to customer and quantity return

        writer = pd.ExcelWriter(self.writefile)
        
        #to return quantity
        for f in sheets:
            reason_data=pd.crosstab([df[f],df.reason_category],[df.year,df.month],
            df.return_quantity,aggfunc='sum',margins=False)
            reason_data.to_excel(writer,f+"_reasons")        
            #to scrap sheet
            scrap=pd.crosstab([df[f],df.reason_category],[df.year,df.month],
            df.scrap,aggfunc='sum',margins=False)
        for f in sheets:
            unique_data=pd.crosstab([df[f]],[df.year,df.month],df.return_quantity,aggfunc='sum',margins=False)
            unique_data.to_excel(writer,f)     
        for f in sheets:
            scrap=pd.crosstab([df[f]],[df.year,df.month],df.scrap,aggfunc='sum',margins=False)
            scrap.to_excel(writer,f+"_scrap")     

        #to input quantity
        reader.to_excel(writer,"input")        
        writer.save()

class Select():
    
    """this class provide  work books and sheet names as input """
    def __init__(self,folder,readfile1,sheet1,year,month,writefile,writesheet):
        self.folder=folder
        
        self.readfile1=readfile1
        self.sheet1=sheet1

        self.year=year
        self.month=month
        self.writefile=writefile
        self.writesheet=writesheet

    def select_data(self,yearDb,monthDb,dayDb,day=True,monthly=True,yearly=True,masterData=True,quality_records=True):
        print("select data starts")  
        '''to convert excel file to csv for entering to database
        already day is true for select day by day
        day=False , its mean the selection for month
        '''
        os.chdir(self.folder)   # for work in the same folder

        #filter master data
        if masterData:
            master_data2=pd.read_excel(self.readfile1,"items_spec")  
            #        #upload  list without parts out of sevice

            #master_data=master_data2[master_data2["status"]==1]
            master_data=master_data2
            #upload moldss list 
            molds2=master_data[columns_molds]
            molds_bool=molds2["view_molds"].notnull()
            molds_list=molds2[molds_bool]
            #upload parts list 
            products_list=master_data[columns_parts]
            infr_data=pd.read_excel(self.readfile1,"machines_master")
        
        #filter inspection data
        daily_data3=pd.read_excel(self.readfile1,"input")
        material_data3=pd.read_excel(self.readfile1,"material")
        #filter the time
        last_year=daily_data3["year"].max()
        

        daily_data2=daily_data3[daily_data3["year"]==last_year]
        daily_data_material2=material_data3[material_data3["year"]==last_year]
        last_month=daily_data2["month"].max()

        daily_data1=daily_data2[daily_data2["month"]==int(monthDb)]
        daily_data_material1=daily_data_material2[daily_data_material2["month"]==int(monthDb)]
        last_day=daily_data1["day"].max()
        
        #to select periond of data
        if day:
            daily_analysis=daily_data1[daily_data1["day"]==int(dayDb)]
            daily_analysis_materia=daily_data_material1[daily_data_material1["day"]==int(dayDb)]
        elif monthly:
            daily_analysis=daily_data1
            daily_analysis_materia=daily_data_material1
        elif yearly:
            daily_analysis=daily_data2
            daily_analysis_materia=daily_data_material2
        else:    
            daily_analysis=daily_data3
            daily_analysis_materia=material_data3
        #daily_analysis_materia=material_data3      #for get all rows
        #filter master data
            #filter weights and scrap table
        productions_isnpection=daily_analysis[columns_quality]
         #filter ct tables
        molds_rate3=daily_analysis[columns_cycle_time]
        
        molds_rate_bool=molds_rate3["c_t_actually"].notnull()
        molds_rate2=molds_rate3[molds_rate_bool]
            #filter weight tables
        dry_weight3=daily_analysis[columns_weight]
        dry_weight2_bool=dry_weight3["average_dry_weight"].notnull()
        dry_weight2=dry_weight3[dry_weight2_bool]
            #filter scrab tables
        scrap3=daily_analysis[columns_scrap]
        scrap2_bool=scrap3["gross_production"].notnull()
        scrap2=scrap3[scrap2_bool]
        print("finishing the filtration and we will start to output now")  
        writer = pd.ExcelWriter("input_to_csv.xlsx")
        if masterData:
            molds_list.to_excel(writer,"molds_list", index=False)
            products_list.to_excel(writer,"parts_list", index=False)
            infr_data.to_excel(writer,"machines_list", index=False)
        else:
            productions_isnpection.to_excel(writer,"quality_records", index=False)        
            daily_analysis_materia.to_excel(writer,"materials", index=False)        
            dry_weight2.to_excel(writer,"weight_input", index=False)
            molds_rate2.to_excel(writer,"ct_input", index=False)        
            dry_weight2.to_excel(writer,"weight_input", index=False)
            scrap2.to_excel(writer,"scrap_input", index=False)
        writer.save()    

        print ("completed catch data  for ")
        print("year",daily_analysis["year"].unique())
        print("month",daily_analysis["month"].unique())
        print("for the days")
        print(daily_analysis["day"].unique())
        writer.save()
        
    def convert_csv(self,material=True,masterData=True,quality_records=True):
        os.chdir(self.folder)   # for work in the same folder
        '''to convert excel file to csv for entering to database'''
        
        #file_identifier = "*.XLS"
        #THIS_FOLDER = os.path.abspath(self.folder)
        df=pd.read_excel("input_to_csv.xlsx")
        if quality_records:
            pd.read_excel("input_to_csv.xlsx", "quality_records").to_csv("quality_records.csv", index=False)#input_to_database.csv
            pd.read_excel("input_to_csv.xlsx", "materials").to_csv("materials.csv", index=False)#input_to_database.csv

        if material:
            df=pd.read_excel("materials.xlsx")
            pd.read_excel("materials.xlsx", "Sheet1").to_csv("materials.csv", index=False)#input_to_database.csv
        if masterData:
            pd.read_excel("input_to_csv.xlsx", "machines_list").to_csv("machines.csv", index=False)#input_to_database.csv
            pd.read_excel("input_to_csv.xlsx", "molds_list").to_csv("molds_list.csv", index=False)#input_to_database.csv
            pd.read_excel("input_to_csv.xlsx", "parts_list").to_csv("parts_list.csv", index=False)#input_to_database.csv
        else:  
            pd.read_excel("input_to_csv.xlsx", "quality_records").to_csv("quality_records.csv", index=False)#input_to_database.csv
            pd.read_excel("input_to_csv.xlsx", "materials").to_csv("materials.csv", index=False)#input_to_database.csv
#_________________ to copy rang to another
    #File to be copied
        print("data is ready for upload to data base")
        #print(sheetname)
        
#_________________ to copy rang to another
    #File to be copied
    
        
    def import_database(self):
        os.chdir(self.folder)
        #from last funciton get csv files and upload to data base#_______#####        
        #filter inspection data
        daily_analysis=pd.read_csv("quality_records.csv")
        #filter the time
                     
        #filter master data
        
            #filter weights and scrap table
        productions_isnpection=daily_analysis[columns_quality]
        cur=database.cursor
        table="yt_quality"
        

        #not upload any duplicates database
        #1show data in yt_qulity
        database.Block.get_daily_dataentry_items(self)
        rows=database.cursor.fetchall()
        print(rows["month"])
        #2show data in csv file
        #3if comparison between 1 and 2
        #release

        #or
        # record importing and avoid second uploading


        f = open('D:\work\contact_group\Contact records\QC quality control\Foam\qc_molds\database\quality_records.csv')
        cur.copy_from(f, table, sep=',')
        f.close()
        #cur.copy_from(productions_isnpection,table, null='', sep=',', columns=(columns_molds))
        #sqlstr = "COPY yt_quality FROM STDIN DELIMITER ',' CSV"
        #with open('D:\work\contact_group\Contact records\QC quality control\Foam\qc_molds\database\quality_records.csv') as f:
        #    cur.copy_expert(sqlstr, f)
        conn.commit()

        #sorce code1
        #csv_file_name = '/home/user/some_file.csv'
        #sql = "COPY table_name FROM STDIN DELIMITER '|' CSV HEADER"
        #cursor.copy_expert(sql, open(csv_file_name, "r"))
        
        #source code2
        #f = open(r'C:\Users\n\Desktop\data.csv', 'r')
        #cur.copy_from(f, temp_unicommerce_status, sep=',')
        #f.close()

    def export_report_mothly(self,writerFile,year,month,day,to_day,*args,monthly=True):
        from memory import Block,cursor

        os.chdir(self.folder)
        inputPath=self.folder+r'\formats'
        outputPath=self.folder+r'\data\qc_molds'
        wb = xl.load_workbook(self.readfile1)
        #year=
        
        #daily input
    
        ws1=wb["input_daily"]
        Block.get_daily_dataentry_items(self,year,month,args)
        get_data=cursor.fetchall()
        #get_data.set_index("serial", inplace=True) #put index
        
        #get_data=pd.DataFrame(get_data["id"])
        rows=get_data
        #rows = get_data[columns_quality]
        
        r = 4  # start at fourd row
        c = 1 # column 'a'
        for row in rows:
            #print(row)
            for item in row:
                ws1.cell(row=r, column=c).value = item
                c += 1 # Column 'b'
            c = 1
            r += 1
        #material by silo
        
        ws_bach=wb["material_daily"]
        Material.material_bySilo_daily(self,year,month,day,to_day)
        get_data=cursor.fetchall()
        #get_data.set_index("serial", inplace=True) #put index
        
        #get_data=pd.DataFrame(get_data["id"])
        rows=get_data
        #rows = get_data[columns_quality]
        
        r = 4  # start at fourd row
        c = 1 # column 'a'
        for row in rows:
            #print(row)
            for item in row:
                ws_bach.cell(row=r, column=c).value = item
                c += 1 # Column 'b'
            c = 1
            r += 1
        #Bache input
        ws_bach=wb["batches"]
        Block.show_monthly_Baches(self,year,month)
        get_data=cursor.fetchall()
        #get_data.set_index("serial", inplace=True) #put index
        
        #get_data=pd.DataFrame(get_data["id"])
        rows=get_data
        #rows = get_data[columns_quality]
        
        r = 4  # start at fourd row
        c = 1 # column 'a'
        for row in rows:
            #print(row)
            for item in row:
                ws_bach.cell(row=r, column=c).value = item
                c += 1 # Column 'b'
            c = 1
            r += 1
        #monthly scrap report by day
        ws8=wb["scrap_type_machines"]
        Block.show_scrap_monthly_report_type_machines(self,year,month)
        rows = cursor.fetchall()
        r = 3  # start at 33th row
        c = 1 # column 'a'
        for row in rows:
            #print(row)
        
            for item in row:
                ws8.cell(row=r, column=c).value = item
                c += 1 # Column 'b'
            c = 1
            r += 1
            #monthly machine report
        ws8=wb["scrap_days"]
        Block.show_scrap_monthly_report_by_days(self,year,month)
        rows = cursor.fetchall()
        r = 3  # start at 33th row
        c = 1 # column 'a'
        for row in rows:
            #print(row)
        
            for item in row:
                ws8.cell(row=r, column=c).value = item
                c += 1 # Column 'b'
            c = 1
            r += 1    
        #water content report
        ws1=wb["moisture_daily"]
        Block.show_water_content_daily(self,year,month,day,to_day)
        get_data=cursor.fetchall()
        #get_data.set_index("serial", inplace=True) #put index
        
        #get_data=pd.DataFrame(get_data["id"])
        rows=get_data
        #rows = get_data[columns_quality]
        
        r = 4  # start at fourd row
        c = 1 # column 'a'
        for row in rows:
            #print(row)
            for item in row:
                ws1.cell(row=r, column=c).value = item
                c += 1 # Column 'b'
            c = 1
            r += 1
        #monthly output
        if monthly:
            ws2=wb["output"]
            Block.show_monthly_report_ar(self,year,month,day,to_day)
            rows = cursor.fetchall()
            r = 3  # start at third row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws2.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            #______yearly report
            #monthly mold report
            
            #filter on non conformity weights
                #part one low weight
            ws5=wb["wieght_report"]
            Block.monthly_report_ncr_weight_low(self,year,month)
            rows = cursor.fetchall()
            r = 12  # start at 12 row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws5.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
                #part tow hight weight
                ws5=wb["wieght_report"]
            Block.monthly_report_ncr_weight_hight(self,year,month)
            rows = cursor.fetchall()
            r = 33  # start at 33th row
            c = 1 # column 'a'
            for row in rows:
                
                for item in row:
                    ws5.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            #filter on non conformity ct
            ws6=wb["ct_report"]
            Block.monthly_report_ncr_ct(self,year,month)
            rows = cursor.fetchall()
            r = 11  # start at 11th row
            c = 1 # column 'a'
            for row in rows:
                
                for item in row:
                    ws6.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            #filter on on conformity scrap
            ws7=wb["scrap_report"]
            Block.monthly_report_ncr_scrap(self,year,month)
            rows= cursor.fetchall()
            r = 15  # start at 15th row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws7.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            #monthly machine report
            ws8=wb["scrap_machine"]
            Block.show_machine_monthly_report(self,year,month)
            rows = cursor.fetchall()
            r = 3  # start at 33th row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws8.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            
            
            #monthly machine report
            ws8=wb["scrap_machine_yearly"]
            Block.show_machine_yearly_report(self,year,month)
            rows = cursor.fetchall()
            r = 3  # start at 33th row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws8.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            
        
            ws2=wb["output_monthly"]
            Block.show_yearly_report_itemsByMonths(self,year,args)
            
            rows = cursor.fetchall()
            r = 3  # start at third row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws2.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            
            ws3=wb["year"]
            Block.show_machine_report_yearly(self,year,month)
            rows = cursor.fetchall()
            r = 3  # start at third row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws3.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            #scrap monthly
            ws3=wb["month"]
            Block.show_monthly_report_view_month(self,year,month)
            rows = cursor.fetchall()
            r = 3  # start at third row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws3.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            #yearly item report
            ws2=wb["output_yearly"]
            Block.items_report_arabic_custom_item(self,year,month,args)
            
            rows = cursor.fetchall()
            r = 3  # start at third row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws2.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            
            
            #monthly mold report by molds not items
            ws_output_molds=wb["output_molds"]
            Block.show_mnthly_report_molds(self,year,month)

            rows = cursor.fetchall()
            r = 3  # start at third row
            c = 1 # column 'a'
            for row in rows:
                #print(row)

                for item in row:
                    ws_output_molds.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1

            ws_output_molds_yearly=wb["output_mold_monthly"]
            Block.yearly_report_molds_byMonthes(self,year,args)

            rows = cursor.fetchall()
            r = 3  # start at third row
            c = 1 # column 'a'
            for row in rows:
                #print(row)

                for item in row:
                    ws_output_molds_yearly.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1

                #report for moldsy monthly
            
            ws_wieght_yearly=wb["output_molds_yearly"]
            Block.show_yearly_report_molds(self,year,month)
            rows = cursor.fetchall()
            r = 3  # start at 3th row
            c = 1 # column 'a'
            for row in rows:
                for item in row:
                    ws_wieght_yearly.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            
                #report of hight weight
            ws_wieght_yearly=wb["wieght_yearly"]
            Block.yearly_report_ncr_weight(self,year,month)
            rows = cursor.fetchall()
            r = 10  # start at 10th row
            c = 1 # column 'a'
            for row in rows:
                
                for item in row:
                    ws_wieght_yearly.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            #filter on non conformity ct
            ws_ct_yearly=wb["ct_yearly"]
            Block.yearly_report_ncr_ct(self,year,month)
            rows = cursor.fetchall()
            r = 11  # start at 11th row
            c = 1 # column 'a'
            for row in rows:
                
                for item in row:
                    ws_ct_yearly.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            #filter on on conformity scrap
            ws_scrap_yearly=wb["scrap_yearly"]
            Block.yearly_report_ncr_scrap(self,year,month)
            rows= cursor.fetchall()
            r = 15  # start at 15th row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
            
                for item in row:
                    ws_scrap_yearly.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1
            #for material
            ws1=wb["materials"]
            Material.materialToPorduct(self,year)
            get_data=cursor.fetchall()
            #get_data.set_index("serial", inplace=True) #put index
            
            #get_data=pd.DataFrame(get_data["id"])
            rows=get_data
            #rows = get_data[columns_quality]
            
            r = 4  # start at fourd row
            c = 1 # column 'a'
            for row in rows:
                #print(row)
                for item in row:
                    ws1.cell(row=r, column=c).value = item
                    c += 1 # Column 'b'
                c = 1
                r += 1

            

        wb.save(writerFile)
    def molds_capabilty_study(self,mold,LSL,USL,eye_numbers,code,name,date):
        os.chdir(self.folder)
        
        
        Block.show_items(self)
        get_data=cursor.fetchall()
        #get_data.set_index("serial", inplace=True) #put index
        get_data=pd.read_excel("QC_daily_v2 - Copy.xlsx","items_spec")
        #get_data=pd.DataFrame(get_data["id"])
        data2=get_data[get_data['mold_id']==mold]
        data=data2
        #data=data2.split(",")
        director=data["mold_id"]
        print("kindly weignt , the data is generating")
        
        wb = xl.load_workbook(self.readfile1)
        ws2= wb.get_sheet_by_name('eye')
        

        #rows = get_data[columns_quality]
#        for items in len(data):

        #part=data[items]
        #item=[data["part_id"]==part]
        
        #ws2['h2']=self.sheet1
        
        ws2['a2']=code
        ws2['b2']=date
        ws2['k2']=name
        ws2['i9']=USL
        ws2['i10']=LSL
        for n in range(eye_numbers):
            ws=wb.copy_worksheet(ws2)   #copy new sheet
            r = 6  # row number
            c = 2 # column 'a'
            values=[]
            for i in range(50):
                
                random_value = randint(LSL,USL)            
                values.append(random_value)
                
                for item in values:
                    item=str(random_value)
                    ws.cell(row=r, column=c).value = item
                c = 2
                r += 1
            ws.title=self.writesheet
        wb.save(self.writefile)
    
    def export_report_daily_yearly(self,year,month,day,to_day,*args):
        os.chdir(self.folder)
        #new sheet
        
        wb = xl.load_workbook(self.readfile1)
        #daily input
        ws1=wb["input_daily"]
        Block.get_daily_dataentry_items_yearly(self,year,month,day,to_day)
        get_data=cursor.fetchall()
        #get_data.set_index("serial", inplace=True) #put index
        
        #get_data=pd.DataFrame(get_data["id"])
        rows=get_data
        #rows = get_data[columns_quality]
        
        r = 4  # start at fourd row
        c = 1 # column 'a'
        for row in rows:
            #print(row)
            for item in row:
                ws1.cell(row=r, column=c).value = item
                c += 1 # Column 'b'
            c = 1
            r += 1
        #for week
        ws1=wb["input-week"]
        '''
        Block.yearly_report_molds_byWeeks(self,year,month,day,to_day)
        get_data=cursor.fetchall()
        #get_data.set_index("serial", inplace=True) #put index
        
        #get_data=pd.DataFrame(get_data["id"])
        rows=get_data
        #rows = get_data[columns_quality]
        
        r = 4  # start at fourd row
        c = 1 # column 'a'
        for row in rows:
            #print(row)
            for item in row:
                ws1.cell(row=r, column=c).value = item
                c += 1 # Column 'b'
            c = 1
            r += 1

        '''
        #for material
        ws1=wb["input_materials"]
        Material.materialToPorduct_daily(self,year)
        get_data=cursor.fetchall()
        #get_data.set_index("serial", inplace=True) #put index
        
        #get_data=pd.DataFrame(get_data["id"])
        rows=get_data
        #rows = get_data[columns_quality]
        
        r = 4  # start at fourd row
        c = 1 # column 'a'
        for row in rows:
            #print(row)
            for item in row:
                ws1.cell(row=r, column=c).value = item
                c += 1 # Column 'b'
            c = 1
            r += 1

        

        wb.save(year+"-QC_molds_daily_yearly_v3.xlsx")
    