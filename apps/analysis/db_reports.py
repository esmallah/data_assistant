from .database_postgrsql import cursor,conn


SQL_quality_records="""
				year,
				month,
				day,
				machine_id,
				item_id,
				number_day_use,
				mold_id,
				product_parts,
				shift1_wet_weight1,
				shift1_wet_weight2,
				shift1_wet_weight3,
				shift1_wet_weight4,
				shift1_wet_weight5,
				shift1_dry_weight1,
				shift1_dry_weight2,
				shift1_dry_weight3,
				shift1_dry_weight4,
				shift1_dry_weight5,
				shift1_c_t1,
				shift1_c_t2,
				shift2_wet_weight1,
				shift2_wet_weight2,
				shift2_wet_weight3,
				shift2_wet_weight4,
				shift2_wet_weight5,
				shift2_dry_weight1,
				shift2_dry_weight2,
				shift2_dry_weight3,
				shift2_dry_weight4,
				shift2_dry_weight5,
				shift2_c_t1,
				shift2_c_t2,
				average_dry_weight,
				average_wet_weight,
				rat_actually,
				rat_validation,
				c_t_actually,
				shift1_production_cards,
				shift1_prod_page,
				shift1_proper_production,
				shift1_scrabe_shortage,
				shift1_scrabe_roll,
				shift1_scrabe_broken,
				shift1_scrabe_curve,
				shift1_scrabe_shrinkage,
				shift1_scrabe_dimentions,
				shift1_scrabe_weight,
				shift1_scrabe_dirty,
				shift1_scrabe_cloration,
				shift1_scrabe_No_parts,
				shift1_scrabe_no_item,
				shift1_all_production,
				shift2_production_cards,
				shift2_prod_page,
				shift2_proper_production,
				shift2_scrabe_shortage,
				shift2_scrabe_roll,
				shift2_scrabe_broken,
				shift2_scrabe_curve,
				shift2_scrabe_shrinkage,
				shift2_scrabe_dimentions,
				shift2_scrabe_weight,
				shift2_scrabe_dirty,
				shift2_scrabe_cloration,
				shift2_scrabe_No_parts,
				shift2_scrabe_no_item,
				shift2_all_production,
				sum_scrabe_shortage_bySet,
				sum_scrabe_roll_bySet,
				sum_scrabe_broken_bySet,
				sum_scrabe_curve_bySet,
				sum_scrabe_shrinkage_bySet,
				sum_scrabe_dimentions_bySet,
				sum_scrabe_weight_bySet,
				sum_scrabe_dirty_bySet,
				sum_scrabe_cloration_bySet,
				sum_scrabe_No_parts,
				number_scrab_by_item,
				gross_production,
				scrap_percent_by_item,
				part_id,
				factory,
				scrab_ncr_reason,
				ct_ncr_reason,
				weight_ncr_reason,
				id_DayPartUnique,
				parts_patchsNumbers,
				Items_patchsNumbers,
				bachStartDate,
				date_day,
				bachEndDate
				"""
sql_quality_reporty_yearly_item='''
								year , mold_id,item_id,product_name
								,product_code
								,standard_dry_weight
								,standard_dry_weight_from
								,standard_dry_weight_to
								,round(avg(average_wet_weight),1)as average_wet_weight
								,round(avg(average_dry_weight),1)as average_dry_weight
								,round(avg(average_wet_weight)-avg(standard_dry_weight)/avg(standard_dry_weight),1) as wet_average_percent
								,standard_rate_hour as standard_rate_hour
								,c_t_standard_per_second c_t_standard_per_second
								,round(avg(rat_actually),0)as rat_actually
								,round(avg(c_t_actually),0)as c_t_actually
								,round(sum(sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
								round(sum(sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
								round(sum(sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet,
								round(sum(sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
								round(sum(sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
								round(sum(sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
								round(sum(sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
								round(sum(sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
								round(sum(sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
								scrabe_standard as scrabe_standard,
								
								round(sum(number_scrab_by_item),0)as number_scrab_by_item,
								
								round(sum(gross_production),0)as gross_production,
								round(sum(standard_scrap_weight_kg),1)as standard_scrap_weight_kg,
								round(sum(standard_production_weight_kg),1)as standard_production_weight_kg,
								round(sum(scrap_weight_kg),1)as scrap_weight_kg,
								round(sum(production_weight_kg),1)as production_weight_kg,
								round(count(number_day_use),0)as number_day_use,
								round(sum(number_scrab_by_item)/avg(rat_actually),1) as HoursScrap,
								round(avg(mold_avalibility),2)as "mold_avalibility",
								customer_name
								
'''
sql_quality_reporty_yearly_mold='''year, mold_id,mold_name

					,c_t_standard_per_second,
							round(avg(rat_actually),0)as rat_actually,

							round(avg(c_t_actually),0)as c_t_actually,
							
							round(sum(sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
							round(sum(sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
							round(sum(sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
							round(sum(sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
							round(sum(sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
							round(sum(sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
							round(sum(sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
							round(sum(sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
							round(sum(sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
							scrabe_standard,
							
							round(sum(number_scrab_by_item),0)as number_scrab_by_item,
							
							round(sum(gross_production),0)as gross_production,
							round(sum(standard_scrap_weight_kg),1)as standard_scrap_weight_kg,
							round(sum(standard_production_weight_kg),1)as standard_production_weight_kg,
							round(sum(scrap_weight_kg),1) as scrap_weight_kg,
							round(sum(production_weight_kg),1)as production_weight_kg,
							round(count(number_day_use),0)as number_day_use,
							round(sum(number_scrab_by_item)/avg(rat_actually),1) as HoursScrap,
							round(avg(mold_avalibility),2)as "mold_avalibility"
							
					'''
sql_quality_water_content='''
				year,
				month,
				day,
				item_id,
				mold_id
				,product_name,
				product_code
				machine_id,
				standard_dry_weight
				,standard_dry_weight_from
				,standard_dry_weight_to
				,round(avg(average_wet_weight),1)as average_wet_weight
				,round(avg(average_dry_weight),1)as average_dry_weight
				
				
					'''
sql_material_daily='''
				date_day,
				shift,
				silo_number,
				line_number,
				material
				,density,
				standard_denisty_from,
				standard_denisty_to,
				actually_denisty_1,
				actually_denisty_2
				,actually_denisty_3
				,midian_actually_denisty
				,min_actually_denisty
				,max_actually_denisty
					'''
class Block():
	'''
		this class for manage data base on sahrenetowrk or cpanel to mold categories in foam industries
		
	'''		
	def __init__(self,folder,table):
		self.folder=folder
		self.table=table
		
	def server_pc_qa(self,year,month,day):
		#for get last year and month and day form loaded database
		SQL1='''select * from  yt_quality where year=%s'''%year
		SQL2=SQL1+'and month=%s'%month
		SQL3=SQL2+'and day=%s'%day
		cursor.execute(SQL3)
		
		#last_monthDb=last_yearDb["month"].max()
		#mold_daysDb=last_monthDb["day"].max()
		# fro test the connection
		rows = cursor.fetchall()
		#rows = cursor.fetchone()
		array_length= len(rows)
		rows=pd.DataFrame()
		
		for row in rows:
		#	print("__test1___")
		#	print(row)
			rows=rows.append(row)
			
			#rows["year"]=rows["year"].astype(int)#Last convert values to ints:

			#return rows
		print("array_length:",array_length)
		#print("__test		# 2___",rows)
		last_year=rows.iloc[:,2]
		print("year",last_year)
		lastMonth=rows.iloc[0][3]
		lastDay=rows.iloc[0][4]
		print("year:",last_year,", month:",lastMonth," and day:",lastDay)
	def server_pc_qa_test(self,year,month):
		#select by varible
		table_name="yt_quality"
					
		SQL1 = 'SELECT * FROM %s' %table_name
		SQL2 = SQL1+' where year=2019 and month =(%s);'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	

		#source code
		#SQL1 = 'SELECT * FROM %s' %table_name
		#SQL2 = SQL1+' WHERE created_on < date (%s);'
		#cursor.execute(SQL2, (time_from, ))
		#https://stackoverflow.com/questions/31760183/psycopg2-cursor-execute-pass-in-variable-table-names-and-items
		# fro test the connection
		
		rows = cursor.fetchall()
		
		for row in rows:
			print(row)

	def uninstall_database(self):
		#uninstall report first steps to uninistall database structures
			drop_yv_database=	'''drop database Block_QC'''
			cursor.execute(drop_yv_database)
			
			conn.commit()	# for change the data base on postgrsql
	def uninstall_reports(self):
		#uninstall report first steps to uninistall database structures'''
			
			drop_yv_items_molds_report=	'''drop view yv_items_molds_report'''
			cursor.execute(drop_yv_items_molds_report)
			
			drop_yv_molds_report_daily=	'''drop view yv_molds_report_daily'''
			cursor.execute(drop_yv_molds_report_daily)

			drop_yv_molds_report=	'''drop view yv_molds_report'''
			cursor.execute(drop_yv_molds_report)

			drop_yv_material_product_daily='''drop view yv_material_product_daily '''
			cursor.execute(drop_yv_material_product_daily)

			drop_yv_material_daily_used='''drop view yv_material_daily_used '''
			cursor.execute(drop_yv_material_daily_used)

			drop_Yv_quality_inspection_items=		'''drop view Yv_quality_inspection_items'''
			cursor.execute(drop_Yv_quality_inspection_items)
			
			
			drop_Yv_quality_inspection_molds=		'''drop view Yv_quality_inspection_molds'''
			cursor.execute(drop_Yv_quality_inspection_molds)

			drop_Yv_quality_inspection_parts='''drop view Yv_quality_inspection_parts '''
			cursor.execute(drop_Yv_quality_inspection_parts)
			
			conn.commit()	
			print("complete uninistall reports")
	def uninstall_records(self):
			#for uninstall records tables
			drop_yt_quality=	'''drop table yt_quality''' 
			cursor.execute(drop_yt_quality)
			conn.commit()
			print("complete uninistall quality records")
	def uninstall_maretial(self):
			#for uninstall records tables
			drop_yt_material=	'''drop table yt_material''' 
			cursor.execute(drop_yt_material)
			conn.commit()
			print("complete uninistall material record")
					

	def uninstall_masterdata(self):
			drop_yv_items_master='''drop view yv_items_master'''
			cursor.execute(drop_yv_items_master)

			drop_yv_item_specifications='''drop view yv_item_specifications'''
			cursor.execute(drop_yv_item_specifications)
			
			drop_yv_item_specifications='''drop view yv_molds_list'''#new
			cursor.execute(drop_yv_item_specifications)
					
			drop_Yt_parts_list='''drop table Yt_parts_list'''
			cursor.execute(drop_Yt_parts_list)
			
			drop_Yt_molds_list='''drop table Yt_molds_list'''
			cursor.execute(drop_Yt_molds_list)
			conn.commit()
			print("complete uninistall master data")
	def uninstall_infrastrucure(self):
			drop_yt_machine_list='''drop table yt_machine_list'''
			cursor.execute(drop_yt_machine_list)
			conn.commit()
			print("complete uninistall infastructure")
	def install_database(self):
		#uninstall report first steps to uninistall database structures
			drop_yv_database=	'''create database Block_QC'''
			cursor.execute(drop_yv_database)
			
			conn.commit()	
	def install_machinelearn(self):
			#table for unity sheet names
			create_table_master_names='''
				create table Yt_master_names (
				id serial primary key, name varchar(100) , name_en varchar(100)null , name_ar varchar(100) null,first_source varchar(100) null ,main_category varchar(100) null);
				'''
			cursor.execute(create_table_master_names)
			#for enter new of names connection between Yt_master_names
			create_table_master_name_traindata='''create table Yt_master_name_traindata (id serial primary key,name varchar(50),main_category varchar(50),id_master_names);'''
			cursor.execute(create_table_master_name_traindata)
			conn.commit()
			
	def install_infrastrucure(self):
			create_table_machine_list='''create table yt_machine_list (id int primary key,scrabe_standard numeric , machine_type varchar(50),place varchar(50),low_size varchar(50) null,high_size varchar(50));'''
			cursor.execute(create_table_machine_list)
			conn.commit()
			print("complete inistall infrastructure data")
	def install_master_data(self):
			create_table_molds_list='''create table Yt_molds_list (
				mold_id int primary key,
				ORG_CODE varchar(50),
				ORG_NAME varchar(50),
				Ctegory varchar(50),
				UOM varchar(50),
				machie_size varchar(50),
				No_on_Set int null,
				set numeric null,
				sub_category varchar(50) null,
				mold_name varchar(300),
				status varchar(50)/*mold wrkind or mold not working*/,
				c_t_standard_per_second int,
				c_t_standard_per_second_from int,
				c_t_standard_per_second_to int,
				view_molds boolean,
				gap_mm int null,
				injekors_numbers int null,
				drummers_number int null,
				customer_id varchar(50) null,
				playback varchar(50) null,
				gap_tolerance int null,
				gap_mm_from int null,
				gap_mm_to int null,
				machine_parameter_id int null ,
				mold_start_date date null,
				mold_expire_date date null,
				customer_name varchar(100) null,
				company_of_customer varchar(200) null,
				customer_proberty_name varchar(200) null,
				customer_proberty_sequence varchar(200) null,
				customer_asset_code varchar(200) null,
				Customer_Product_Group varchar(200) null			
				)
				'''
			cursor.execute(create_table_molds_list)
			
			create_table_parts_list='''CREATE TABLE public.yt_parts_list
					(
					id_part varchar(50) primary key,
					product_code character varying(100) COLLATE pg_catalog."default",
					product_name_by_parts character varying(300) COLLATE pg_catalog."default",
					weight_kg numeric,
				standard_rate_hour int,
				highlite varchar(50) null,
				standard_dry_weight numeric,
				standard_dry_weight_from numeric,
				standard_dry_weight_to numeric,
				positive_weight numeric,
				negative_weight numeric,
				
				sub_category varchar(50),
				mold_id integer,
				product_parts varchar(50),
				item_id integer,
				product_name character varying(300) COLLATE pg_catalog."default",
				item_name_customers varchar(100) null,
				item_code_customers varchar(50) null,
				item_classification_customers varchar(120) null,
				view_items boolean,
				view_parts boolean,
				view_molds boolean,
				density numeric,
				row_material_typea character varying(50) COLLATE pg_catalog."default",
				row_material_typeb character varying(50) COLLATE pg_catalog."default",
				tall_mm numeric,
				tall_positive_tolerance numeric,
				tall_negative_tolerance numeric,
				width_mm numeric,
				width_positive_tolerance numeric,
				width_negative_tolerance numeric,
				sicness_mm numeric,
				sicness_positive_tolerance numeric,
				sicness_negative_tolerance numeric,
				id_printed_specification integer null,
				spec_folder_no integer null,
				page_volum_x numeric null,
				page_volum_y numeric null,
				page_volum_z numeric null,
				volume numeric null,
				sitotb_color character varying(50) COLLATE pg_catalog."default",
				sitotb_set character varying(50) COLLATE pg_catalog."default",
				silotib_meter_reels character varying(50) COLLATE pg_catalog."default",
				silotib_outside_meter numeric,
				package_page character varying(50) COLLATE pg_catalog."default",
				number_bacage character varying(50) COLLATE pg_catalog."default",
				page_size_x numeric,
				page_size_y numeric,
				page_colore character varying(50) COLLATE pg_catalog."default",
				pages_kgm_set numeric,
				pages_kgm numeric,
				kg_after_add12percent numeric,
				kg_after_add8_5percent numeric(50,0),
				id_modification int null,
				notes varchar(300) null,
				silotib_inside_meter numeric
				)
'''
			cursor.execute(create_table_parts_list)

			create_view_molds_list='''/* list molds by all informatio for molds only (not any parts) */create view yv_molds_list as (select M.*,p.standard_rate_hour
								from yt_parts_list p
							left join Yt_molds_list M
							on p.mold_id=M.mold_id
							where p.view_molds is not null)
							'''
			cursor.execute(create_view_molds_list)

			create_view_item_specification='''create view yv_item_specifications as (select p.* ,M.machie_size 
									,No_on_Set  ,M.set  ,M.mold_name ,
									M.customer_id ,M.c_t_standard_per_second ,	M.c_t_standard_per_second_from ,
								M.c_t_standard_per_second_to
								from yt_parts_list p
							left join Yt_molds_list M
							on p.mold_id=M.mold_id)'''
			cursor.execute(create_view_item_specification)
			
			create_view_item_master='''create view yv_items_master as (select p.* ,M.machie_size 
									,No_on_Set  ,M.set  ,M.mold_name ,M.UOM ,
									M.customer_id  ,M.c_t_standard_per_second ,	M.c_t_standard_per_second_from ,
								M.c_t_standard_per_second_to ,customer_name,company_of_customer
								from yt_parts_list p
							left join Yt_molds_list M
							on p.mold_id=M.mold_id
							where p.view_items=true  )'''
			cursor.execute(create_view_item_master)
			conn.commit()
			print("complete install master data")
	def install_records(self):
			create_table_quality='''
				create table yt_quality (
				id serial primary key,
				year int,
				month int,
				day int,
				machine_id int,
				item_id int,
				number_day_use int null,
				mold_id int,
				product_parts varchar(50),
				shift1_wet_weight1 numeric null,
				shift1_wet_weight2 numeric null ,
				shift1_wet_weight3 numeric null ,
				shift1_wet_weight4 numeric null ,
				shift1_wet_weight5 numeric null ,
				shift1_dry_weight1 numeric null,
				shift1_dry_weight2 numeric null,
				shift1_dry_weight3 numeric null,
				shift1_dry_weight4 numeric null,
				shift1_dry_weight5 numeric null,
				shift1_c_t1 int null,
				shift1_c_t2 int null,
				shift2_wet_weight1 numeric null,
				shift2_wet_weight2 numeric null,
				shift2_wet_weight3 numeric null,
				shift2_wet_weight4 numeric null,
				shift2_wet_weight5 numeric null,
				shift2_dry_weight1 numeric null,
				shift2_dry_weight2 numeric null,
				shift2_dry_weight3 numeric null,
				shift2_dry_weight4 numeric null,
				shift2_dry_weight5 numeric null,
				shift2_c_t1 int null,
				shift2_c_t2 int null,
				average_wet_weight numeric,
				average_dry_weight numeric,
				rat_actually int,
				rat_validation int,
				c_t_actually int null,
				shift1_production_cards int null,
				shift1_prod_page numeric null,
				shift1_proper_production int null,
				shift1_scrabe_shortage int null,
				shift1_scrabe_roll int null,
				shift1_scrabe_broken int null,
				shift1_scrabe_curve int null,
				shift1_scrabe_shrinkage int null,
				shift1_scrabe_dimentions int null,
				shift1_scrabe_weight int null,
				shift1_scrabe_dirty int null,
				shift1_scrabe_cloration int null,
				shift1_scrabe_No_parts int null,
				shift1_scrabe_no_item int null,
				
				shift1_all_production int null,
				
				shift2_production_cards int null,
				shift2_prod_page int null,
				shift2_proper_production int null,
				shift2_scrabe_shortage int null,
				shift2_scrabe_roll int null,
				shift2_scrabe_broken int null,
				shift2_scrabe_curve int null,
				shift2_scrabe_shrinkage int null,
				shift2_scrabe_dimentions int null,
				shift2_scrabe_weight int null,
				shift2_scrabe_dirty int null,
				shift2_scrabe_cloration int null,
				shift2_scrabe_No_parts int null,
				shift2_scrabe_no_item int null,
				shift2_all_production int null,
				sum_scrabe_shortage_bySet int null,
				sum_scrabe_roll_bySet int null,
				sum_scrabe_broken_bySet int null,
				sum_scrabe_curve_bySet int null,
				sum_scrabe_shrinkage_bySet int null,
				sum_scrabe_dimentions_bySet int null,
				sum_scrabe_weight_bySet int null,
				sum_scrabe_dirty_bySet int null,
				sum_scrabe_cloration_bySet int null,
				sum_scrabe_No_parts int null,
				number_scrab_by_item int null,			
				gross_production int,
				scrap_percent_by_item numeric ,
				part_id  varchar(50),
				factory  varchar(50),
				scrab_ncr_reason varchar(100),
				ct_ncr_reason varchar(100),
				weight_ncr_reason varchar(100),
				id_DayPartUnique varchar(50) UNIQUE /*for validate not upload any duplicate rows*/,
				parts_patchsNumbers varchar(50),
				Items_patchsNumbers varchar(50),
				bachStartDate date null,
				bachEndDate date null,
				date_day date);'''
			cursor.execute(create_table_quality)
			conn.commit()
			print("complete install quality records")
	def install_records_material(self):
			create_table_material='''
				create table yt_material (
				id serial primary key,
				year int,
				month int,
				day int,
				date_day date,
				shift int,
				machine_id int,
				silo_number int,
				line_number int,
				ingoing_date date,
				material varchar(50)/*mateiral by density*/,
				density int,
				row_material_name varchar(50),
				standard_denisty_from numeric,
				standard_denisty_to numeric,
				actually_denisty_1 numeric,
				actually_denisty_2 numeric,
				actually_denisty_3 numeric,
				min_actually_denisty numeric,
				midian_actually_denisty numeric,
				max_actually_denisty numeric,
				quantity numeric null,
				id_DayUnique varchar(50) UNIQUE /*for validate not upload any duplicate rows*/


				 );'''
			cursor.execute(create_table_material)
			conn.commit()
			print("complete install material records")
	def install_record_delivery(self):
		create_table_delivery='''
				create table delivery_to_customers (
							year int,
							month int,
							permission_number int,
							product_code varchar(50),
							product_name varchar(50),
							unit varchar(50),,
							warehouse_type varchar(50),
							gross_quantity int,
							customer_code int,
							customer_name varchar(50),,
							sale_order int,
							invoice_numbers int,
							driver_name varchar(50),,
							freighter varchar(50),,
							deliverad_place varchar(50),,
							planned_date date,
							date_date date
							date_part('week', date_date::date) AS weeksNumbers
							)
							
							'''
		cursor.execute(create_table_delivery)
		conn.commit()
	def install_befor_reports_molds(self):	#for prepair data to get reports as mold list
			create_view_qulaity_inspection_as_molds_list='''/* for collect quality_inspection as yv_parts_items  */
				create view Yv_quality_inspection_molds as (select 
									q.year, q.month ,q.date_day as day ,q.mold_id,q.machine_id,
									round(sum(q.shift1_wet_weight1),1)as shift1_wet_weight1,
									round(sum(q.shift1_wet_weight2),1)as shift1_wet_weight2,
									round(sum(q.shift1_wet_weight3),1)as shift1_wet_weight3,
									round(sum(q.shift1_wet_weight4),1)as shift1_wet_weight4,
									round(sum(q.shift1_wet_weight5),1)as shift1_wet_weight5,
									round(sum(q.shift1_dry_weight1),1)as shift1_dry_weight1,
									round(sum(q.shift1_dry_weight2),1)as shift1_dry_weight2,
									round(sum(q.shift1_dry_weight3),1)as shift1_dry_weight3,
									round(sum(q.shift1_dry_weight4),1)as shift1_dry_weight4,
									round(sum(q.shift1_dry_weight5),1)as shift1_dry_weight5,
									round(avg(q.shift1_c_t1),0)as shift1_c_t1,
									round(avg(q.shift1_c_t2),0) as shift1_c_t2,

									round(sum(q.shift2_wet_weight1),1)as shift2_wet_weight1,
									round(sum(q.shift2_wet_weight2),1)as shift2_wet_weight2,
									round(sum(q.shift2_wet_weight3),1)as shift2_wet_weight3,
									round(sum(q.shift2_wet_weight4),1)as shift2_wet_weight4,
									round(sum(q.shift2_wet_weight5),1)as shift2_wet_weight5,				
									round(sum(q.shift2_dry_weight1),1)as shift2_dry_weight1,
									round(sum(q.shift2_dry_weight2),1)as shift2_dry_weight2,
									round(sum(q.shift2_dry_weight3),1)as shift2_dry_weight3,
									round(sum(q.shift2_dry_weight4),1)as shift2_dry_weight4,
									round(sum(q.shift2_dry_weight5),1)as shift2_dry_weight5,
									round(avg(q.shift2_c_t1),0)as shift2_c_t1,		
									round(avg(q.shift2_c_t2),0)as shift2_c_t2,
									round(sum(q.average_wet_weight ),1)as average_wet_weight ,
									round(sum(q.average_dry_weight),1)as average_dry_weight,
									
									round(avg(q.rat_actually),0)as rat_actually ,
									round(avg(q.rat_validation),0)as rat_validation,
									round(avg(q.c_t_actually),0)c_t_actually,				
									round(min(q.shift1_production_cards),0)as shift1_production_cards,
									round(min(q.shift1_prod_page),0)as shift1_prod_page,
									round(min(q.shift1_proper_production),0)as shift1_proper_production,
									round(min(q.shift1_scrabe_shortage),0)as shift1_scrabe_shortage,
									round(min(q.shift1_scrabe_roll),0)as shift1_scrabe_roll,
									round(min(q.shift1_scrabe_broken),0)as shift1_scrabe_broken,
									round(min(q.shift1_scrabe_curve),0)as shift1_scrabe_curve,
									round(min(q.shift1_scrabe_shrinkage),0)as shift1_scrabe_shrinkage,
									round(min(q.shift1_scrabe_dimentions),0)as shift1_scrabe_dimentions,
									round(min(q.shift1_scrabe_weight),0)as shift1_scrabe_weight,
									round(min(q.shift1_scrabe_dirty),0)as shift1_scrabe_dirty,
									round(min(q.shift1_scrabe_cloration),0)as shift1_scrabe_cloration,
									round(min(q.shift1_scrabe_No_parts),0)as shift1_scrabe_No_parts,
									round(min(q.shift1_scrabe_no_item),0)as shift1_scrabe_no_item,
									
									round(min(q.shift1_all_production),0)as shift1_all_production,
									round(min(q.shift2_production_cards),0)as shift2_production_cards,
									round(min(q.shift2_prod_page),0)as shift2_prod_page,
									round(min(q.shift2_proper_production),0)as shift2_proper_production,
									round(min(q.shift2_scrabe_shortage),0)as shift2_scrabe_shortage,
									round(min(q.shift2_scrabe_roll),0)as shift2_scrabe_roll,
									round(min(q.shift2_scrabe_broken),0)as shift2_scrabe_broken,
									round(min(q.shift2_scrabe_curve),0)as shift2_scrabe_curve,
									round(min(q.shift2_scrabe_shrinkage),0)as shift2_scrabe_shrinkage,
									round(min(q.shift2_scrabe_dimentions),0)as shift2_scrabe_dimentions,
									round(min(q.shift2_scrabe_weight),0)as shift2_scrabe_weight,
									round(min(q.shift2_scrabe_dirty),0)as shift2_scrabe_dirty,
									round(min(q.shift2_scrabe_cloration),0)as shift2_scrabe_cloration,
									round(min(q.shift2_scrabe_No_parts),0)as shift2_scrabe_No_parts,
									round(min(q.shift2_scrabe_no_item),0)as shift2_scrabe_no_item,
									
									round(min(q.shift2_all_production),0)as shift2_all_production,
									
									round(min(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
									round(min(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
									round(min(q.sum_scrabe_broken_bySet),0)as sum_scrabe_broken_bySet,
									round(min(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
									round(min(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
									round(min(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
									round(min(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
									round(min(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
									round(min(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
									
									round(min(q.number_scrab_by_item),0)as number_scrab_by_item,/*select one item only in mold________*/
									round(min(q.gross_production),0)as gross_production,/*select one item only in mold________*/

									round(sum(q.number_scrab_by_item)/avg(s.standard_dry_weight),3)as standard_scrap_weight_kg ,
									round(sum(q.gross_production)/avg(s.standard_dry_weight),3)as standard_production_weight_kg,
									round(sum(q.number_scrab_by_item)/avg(q.average_dry_weight),3)as scrap_weight_kg,
									round(sum(q.gross_production)/avg(q.average_dry_weight),3)as production_weight_kg,

									round(avg(q.number_day_use),0)as number_day_use   /*average not sum for not dublicate the same molds*/,
									
									round(sum(number_scrab_by_item)/avg(rat_actually),3)as HoursScrap /*number hourse of scrap*/,
									
									round((sum(q.gross_production)/sum(q.number_day_use))/(22*avg(s.standard_rate_hour)),3)as mold_avalibility /*avalibility bercent in 22 work hours */,
									s.density,
									q.date_day
									from yt_quality q
									left join yv_item_specifications s
									on q.mold_id=s.mold_id
									group by q.year, q.month ,q.date_day,q.machine_id,q.mold_id,s.density
									
									order by q.year, q.month  ,q.date_day ,q.machine_id)
			'''
			cursor.execute(create_view_qulaity_inspection_as_molds_list)
			conn.commit()
			print("complete  install view befor_reports_molds")		
	
	def install_befor_reports_parts(self):		
			create_view_Yv_quality_inspection_parts='''/* for collect quality_inspection as parts  */
				create view Yv_quality_inspection_parts as (select 
									q.year, q.month ,q.date_day as day,q.mold_id,q.part_id,q.machine_id,Items_patchsNumbers,
		
									round(sum(q.shift1_wet_weight1),1)as shift1_wet_weight1,
									round(sum(q.shift1_wet_weight2),1)as shift1_wet_weight2,
									round(sum(q.shift1_wet_weight3),1)as shift1_wet_weight3,
									round(sum(q.shift1_wet_weight4),1)as shift1_wet_weight4,
									round(sum(q.shift1_wet_weight5),1)as shift1_wet_weight5,
									round(sum(q.shift1_dry_weight1),1)as shift1_dry_weight1,
									round(sum(q.shift1_dry_weight2),1)as shift1_dry_weight2,
									round(sum(q.shift1_dry_weight3),1)as shift1_dry_weight3,
									round(sum(q.shift1_dry_weight4),1)as shift1_dry_weight4,
									round(sum(q.shift1_dry_weight5),1)as shift1_dry_weight5,
									round(avg(q.shift1_c_t1),0)as shift1_c_t1,
									round(avg(q.shift1_c_t2),0) as shift1_c_t2,
													
									round(sum(q.shift2_wet_weight1),1)as shift2_wet_weight1,
									round(sum(q.shift2_wet_weight2),1)as shift2_wet_weight2,
									round(sum(q.shift2_wet_weight3),1)as shift2_wet_weight3,
									round(sum(q.shift2_wet_weight4),1)as shift2_wet_weight4,
									round(sum(q.shift2_wet_weight5),1)as shift2_wet_weight5,
									round(sum(q.shift2_dry_weight1),1)as shift2_dry_weight1,
									round(sum(q.shift2_dry_weight2),1)as shift2_dry_weight2,
									round(sum(q.shift2_dry_weight3),1)as shift2_dry_weight3,
									round(sum(q.shift2_dry_weight4),1)as shift2_dry_weight4,
									round(sum(q.shift2_dry_weight5),1)as shift2_dry_weight5,
									round(avg(q.shift2_c_t1),0)as shift2_c_t1,		
									round(avg(q.shift2_c_t2),0)as shift2_c_t2,
							
									round(sum(q.average_wet_weight ),1)as average_wet_weight ,
									round(sum(q.average_dry_weight),1)as average_dry_weight,
									

									round(avg(q.rat_actually),0)as rat_actually ,
									round(avg(q.rat_validation),0)as rat_validation,
									round(avg(q.c_t_actually),0)c_t_actually,				
									round(sum(q.shift1_production_cards),0)as shift1_production_cards,
									round(sum(q.shift1_prod_page),0)as shift1_prod_page,
									round(sum(q.shift1_proper_production),0)as shift1_proper_production,
									round(sum(q.shift1_scrabe_shortage),0)as shift1_scrabe_shortage,
									round(sum(q.shift1_scrabe_roll),0)as shift1_scrabe_roll,
									round(sum(q.shift1_scrabe_broken),0)as shift1_scrabe_broken,
									round(sum(q.shift1_scrabe_curve),0)as shift1_scrabe_curve,
									round(sum(q.shift1_scrabe_shrinkage),0)as shift1_scrabe_shrinkage,
									round(sum(q.shift1_scrabe_dimentions),0)as shift1_scrabe_dimentions,
									round(sum(q.shift1_scrabe_weight),0)as shift1_scrabe_weight,
									round(sum(q.shift1_scrabe_dirty),0)as shift1_scrabe_dirty,
									round(sum(q.shift1_scrabe_cloration),0)as shift1_scrabe_cloration,
									round(sum(q.shift1_scrabe_No_parts),0)as shift1_scrabe_No_parts,
									round(sum(q.shift1_scrabe_no_item),0)as shift1_scrabe_no_item,
									
									round(sum(q.shift1_all_production),0)as shift1_all_production,
									round(sum(q.shift2_production_cards),0)as shift2_production_cards,
									round(sum(q.shift2_prod_page),0)as shift2_prod_page,
									round(sum(q.shift2_proper_production),0)as shift2_proper_production,
									round(sum(q.shift2_scrabe_shortage),0)as shift2_scrabe_shortage,
									round(sum(q.shift2_scrabe_roll),0)as shift2_scrabe_roll,
									round(sum(q.shift2_scrabe_broken),0)as shift2_scrabe_broken,
									round(sum(q.shift2_scrabe_curve),0)as shift2_scrabe_curve,
									round(sum(q.shift2_scrabe_shrinkage),0)as shift2_scrabe_shrinkage,
									round(sum(q.shift2_scrabe_dimentions),0)as shift2_scrabe_dimentions,
									round(sum(q.shift2_scrabe_weight),0)as shift2_scrabe_weight,
									round(sum(q.shift2_scrabe_dirty),0)as shift2_scrabe_dirty,
									round(sum(q.shift2_scrabe_cloration),0)as shift2_scrabe_cloration,
									round(sum(q.shift2_scrabe_No_parts),0)as shift2_scrabe_No_parts,
									
									round(sum(q.shift2_all_production),0)as shift2_all_production,
									
									round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
									round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
									round(sum(q.sum_scrabe_broken_bySet),0)as sum_scrabe_broken_bySet,
									round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
									round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
									round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
									round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
									round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
									round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
									round(sum(q.sum_scrabe_no_parts),0)as sum_scrabe_no_parts,
									round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
									
									round(sum(q.gross_production),0)as gross_production,

									round(sum(q.number_scrab_by_item)/avg(s.standard_dry_weight),3)as standard_scrap_weight_kg ,
									round(sum(q.gross_production)/avg(s.standard_dry_weight),3)as standard_production_weight_kg,
									round(sum(q.number_scrab_by_item)/avg(q.average_dry_weight),3)as scrap_weight_kg,
									round(sum(q.gross_production)/avg(q.average_dry_weight),3)as production_weight_kg,
									


									round(avg(q.number_day_use),0)as number_day_use   /*average not sum for not dublicate the same molds*/,
									round(sum(number_scrab_by_item)/avg(rat_actually),3)as HoursScrap /*number hourse of scrap*/,
									round((sum(q.gross_production)/sum(q.number_day_use))/(22*avg(s.standard_rate_hour)),3)as mold_avalibility /*avalibility bercent in 22 work hours */
									 ,s.density
									from yt_quality q
									left join yv_item_specifications s
									on q.part_id=s.id_part
								
									group by q.year, q.month ,Items_patchsNumbers,q.date_day,q.mold_id,q.part_id,q.machine_id,s.density
									
									order by q.year, q.month ,q.date_day ,q.machine_id)
			'''
			cursor.execute(create_view_Yv_quality_inspection_parts)
			conn.commit()		
			print("complete install view befor_reports_parts")		
	def install_befor_reports_item_master(self):		

			create_view_qulaity_inspection_as_items_master='''/* for collect quality_inspection as yv_items_master  */
								create view Yv_quality_inspection_items as (select 
								q.year, q.month ,q.date_day as day,q.mold_id,q.item_id,q.machine_id,q.factory,Items_patchsNumbers,
	
								round(sum(q.shift1_wet_weight1),1)as shift1_wet_weight1,
								round(sum(q.shift1_wet_weight2),1)as shift1_wet_weight2,
								round(sum(q.shift1_wet_weight3),1)as shift1_wet_weight3,
								round(sum(q.shift1_wet_weight4),1)as shift1_wet_weight4,
								round(sum(q.shift1_wet_weight5),1)as shift1_wet_weight5,
								round(sum(q.shift1_dry_weight1),1)as shift1_dry_weight1,
								round(sum(q.shift1_dry_weight2),1)as shift1_dry_weight2,
								round(sum(q.shift1_dry_weight3),1)as shift1_dry_weight3,
								round(sum(q.shift1_dry_weight4),1)as shift1_dry_weight4,
								round(sum(q.shift1_dry_weight5),1)as shift1_dry_weight5,
								round(avg(q.shift1_c_t1),0)as shift1_c_t1,
								round(avg(q.shift1_c_t2),0) as shift1_c_t2,
												
								round(sum(q.shift2_wet_weight1),1)as shift2_wet_weight1,
								round(sum(q.shift2_wet_weight2),1)as shift2_wet_weight2,
								round(sum(q.shift2_wet_weight3),1)as shift2_wet_weight3,
								round(sum(q.shift2_wet_weight4),1)as shift2_wet_weight4,
								round(sum(q.shift2_wet_weight5),1)as shift2_wet_weight5,
								round(sum(q.shift2_dry_weight1),1)as shift2_dry_weight1,
								round(sum(q.shift2_dry_weight2),1)as shift2_dry_weight2,
								round(sum(q.shift2_dry_weight3),1)as shift2_dry_weight3,
								round(sum(q.shift2_dry_weight4),1)as shift2_dry_weight4,
								round(sum(q.shift2_dry_weight5),1)as shift2_dry_weight5,
								round(avg(q.shift2_c_t1),0)as shift2_c_t1,		
								round(avg(q.shift2_c_t2),0)as shift2_c_t2,
						
								round(sum(q.average_wet_weight ),1)as average_wet_weight ,
								round(sum(q.average_dry_weight),1)as average_dry_weight,
								
								round(avg(q.rat_actually),0)as rat_actually ,
								round(avg(q.rat_validation),0)as rat_validation,
								round(avg(q.c_t_actually),0)c_t_actually,				
								round(sum(q.shift1_production_cards),0)as shift1_production_cards,
								round(sum(q.shift1_prod_page),0)as shift1_prod_page,
								round(sum(q.shift1_proper_production),0)as shift1_proper_production,
								round(sum(q.shift1_scrabe_shortage),0)as shift1_scrabe_shortage,
								round(sum(q.shift1_scrabe_roll),0)as shift1_scrabe_roll,
								round(sum(q.shift1_scrabe_broken),0)as shift1_scrabe_broken,
								round(sum(q.shift1_scrabe_curve),0)as shift1_scrabe_curve,
								round(sum(q.shift1_scrabe_shrinkage),0)as shift1_scrabe_shrinkage,
								round(sum(q.shift1_scrabe_dimentions),0)as shift1_scrabe_dimentions,
								round(sum(q.shift1_scrabe_weight),0)as shift1_scrabe_weight,
								round(sum(q.shift1_scrabe_dirty),0)as shift1_scrabe_dirty,
								round(sum(q.shift1_scrabe_cloration),0)as shift1_scrabe_cloration,
								round(sum(q.shift1_scrabe_No_parts),0)as shift1_scrabe_No_parts,
								round(sum(q.shift1_scrabe_no_item),0)as shift1_scrabe_no_item,
								
								round(sum(q.shift1_all_production),0)as shift1_all_production,
								
								round(sum(q.shift2_production_cards),0)as shift2_production_cards,
								round(sum(q.shift2_prod_page),0)as shift2_prod_page,
								round(sum(q.shift2_proper_production),0)as shift2_proper_production,
								round(sum(q.shift2_scrabe_shortage),0)as shift2_scrabe_shortage,
								round(sum(q.shift2_scrabe_roll),0)as shift2_scrabe_roll,
								round(sum(q.shift2_scrabe_broken),0)as shift2_scrabe_broken,
								round(sum(q.shift2_scrabe_curve),0)as shift2_scrabe_curve,
								round(sum(q.shift2_scrabe_shrinkage),0)as shift2_scrabe_shrinkage,
								round(sum(q.shift2_scrabe_dimentions),0)as shift2_scrabe_dimentions,
								round(sum(q.shift2_scrabe_weight),0)as shift2_scrabe_weight,
								round(sum(q.shift2_scrabe_dirty),0)as shift2_scrabe_dirty,
								round(sum(q.shift2_scrabe_cloration),0)as shift2_scrabe_cloration,
								round(sum(q.shift2_scrabe_No_parts),0)as shift2_scrabe_No_parts,
								round(sum(q.shift2_scrabe_no_item),0)as shift2_scrabe_no_item,
								
								round(sum(q.shift2_all_production),0)as shift2_all_production,
								
								round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
								round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
								round(sum(q.sum_scrabe_broken_bySet),0)as sum_scrabe_broken_bySet,
								round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
								round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
								round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
								round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
								round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
								round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
								round(sum(q.sum_scrabe_no_parts),0)as sum_scrabe_no_parts,
								round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
								
								round(sum(q.gross_production),0)as gross_production,

								round(sum(q.number_scrab_by_item)/avg(s.standard_dry_weight),3)as standard_scrap_weight_kg ,
									round(sum(q.gross_production)/avg(s.standard_dry_weight),3)as standard_production_weight_kg,
									round(sum(q.number_scrab_by_item)/avg(q.average_dry_weight),3)as scrap_weight_kg,
									round(sum(q.gross_production)/avg(q.average_dry_weight),3)as production_weight_kg,

								round(avg(q.number_day_use),0)as number_day_use    /*average not sum for not dublicate the same molds*/,
								
								round(sum(number_scrab_by_item)/avg(rat_actually),3)as HoursScrap /*number hourse of scrap*/,
								round((sum(q.gross_production)/sum(q.number_day_use))/(22*avg(s.standard_rate_hour)),3)as mold_avalibility /*avalibility bercent in 22 work hours */
								,s.density
								from yt_quality q
								left join yv_items_master s
								on q.item_id=s.item_id
						
								group by q.factory,q.year, q.month ,Items_patchsNumbers,q.date_day ,q.mold_id,q.item_id,q.machine_id,s.density
								
								order by q.year, q.month ,q.machine_id
										
										)'''
			cursor.execute(create_view_qulaity_inspection_as_items_master)
			
			conn.commit()		
			print("complete install view befor_reports_Items")	
	def install_befor_reports_material(self):		

			create_view_qulaity_inspection_as_items_master='''/* for collect material unique used ber day as yv_material_daily_used  */
								create view yv_material_daily_used as (select year ,month ,day ,date_day ,material ,sum(quantity) ,density 
								
								from yt_material q
								
								group by year, month ,day,date_day ,density,material
								
								order by year, month , day ,date_day)'''
			cursor.execute(create_view_qulaity_inspection_as_items_master)
			
			conn.commit()		
			print("complete install view befor_reports_Items")	
	
	def install_reports(self):
		create_view_quality_daily='''create view yv_molds_report_daily as(select q.year, q.month ,q.day,q.mold_id,q.item_id,q.machine_id,
								
								p.product_name,p.product_code
								,p.machie_size,p.set,p.no_on_set
								,p.standard_dry_weight,p.standard_dry_weight_from,p.standard_dry_weight_to,
								
								/*weight and ct record*/									
								round(avg(q.shift1_wet_weight1),0)as shift1_wet_weight1,
								round(avg(q.shift1_wet_weight2),0)as shift1_wet_weight2,
								round(avg(q.shift1_wet_weight3),0)as shift1_wet_weight3,
								round(avg(q.shift1_wet_weight4),0)as shift1_wet_weight4,
								round(avg(q.shift1_wet_weight5),0)as shift1_wet_weight5,
								round(avg(q.shift1_dry_weight1),0)as shift1_dry_weight1,
								round(avg(q.shift1_dry_weight2),0)as shift1_dry_weight2,
								round(avg(q.shift1_dry_weight3),0)as shift1_dry_weight3,
								round(avg(q.shift1_dry_weight4),0)as shift1_dry_weight4,
								round(avg(q.shift1_dry_weight5),0)as shift1_dry_weight5,
								round(avg(q.shift1_c_t1),0)as shift1_c_t1,
								round(avg(q.shift1_c_t2),0)as shift1_c_t2,
								round(avg(q.shift2_wet_weight1),0)as shift2_wet_weight1,
								round(avg(q.shift2_wet_weight2),0)as shift2_wet_weight2,
								round(avg(q.shift2_wet_weight3),0)as shift2_wet_weight3,
								round(avg(q.shift2_wet_weight4),0)as shift2_wet_weight4,
								round(avg(q.shift2_wet_weight5),0)as shift2_wet_weight5,
								round(avg(q.shift2_dry_weight1),0)as shift2_dry_weight1,
								round(avg(q.shift2_dry_weight2),0)as shift2_dry_weight2,
								round(avg(q.shift2_dry_weight3),0)as shift2_dry_weight3,
								round(avg(q.shift2_dry_weight4),0)as shift2_dry_weight4,
								round(avg(q.shift2_dry_weight5),0)as shift2_dry_weight5,
								round(avg(q.shift2_c_t1),0)as shift2_c_t1,
								round(avg(q.shift2_c_t2),0)as shift2_c_t2,
								round(avg(q.average_wet_weight),1)as average_wet_weight,
								round(avg(q.average_dry_weight),1)as average_dry_weight,
								round((avg(average_wet_weight)-p.standard_dry_weight)/avg(p.standard_dry_weight),1) as wet_average_percent,
								p.standard_rate_hour,
								p.c_t_standard_per_second,								
								round(avg(q.rat_actually),0)as rat_actually,
								round(avg(q.c_t_actually),0)as c_t_actually,
								/*scrap record*/									
								
								round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
								round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
								round(sum(q.sum_scrabe_broken_bySet),0)as sum_scrabe_broken_bySet,
								round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
								round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
								round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
								round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
								round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
								round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
						
								round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
								round(sum(q.gross_production),0)as gross_production,
								m.scrabe_standard,
								round((sum(q.number_scrab_by_item))/(sum(q.gross_production)),3)as scrap_percent_by_item,
								
								case
									WHEN round((sum(q.number_scrab_by_item))/(sum(q.gross_production)),3) <= m.scrabe_standard THEN 1 
								end as scrab_validation,
								
								
								round(sum(standard_scrap_weight_kg),1)as standard_scrap_weight_kg,
								round(sum(standard_production_weight_kg),1)as standard_production_weight_kg,
								round((sum(q.number_scrab_by_item))*(avg(q.average_dry_weight))/1000,1) as scrap_weight_kg,
								round((sum(q.gross_production))*(avg(q.average_dry_weight))/1000,1) as production_weight_kg,
								p.customer_name,p.company_of_customer,p.item_code_customers,p.item_classification_customers,
								date_part('week', q.day::date) AS weeksNumbers
								
								
								
				from Yv_quality_inspection_items q
							
							left join yv_items_master p
							on q.item_id=p.item_id
							left join yt_machine_list m
							on m.id=q.machine_id
							
								group by q.factory,q.year, q.month ,q.day,q.mold_id,p.mold_name,
								q.machine_id,p.machie_size,m.machine_type,m.scrabe_standard,q.item_id,p.product_name,p.product_code,
								p.product_name_by_parts,p.product_parts,p.UOM,p.set,p.no_on_set,p.standard_dry_weight
								,p.standard_dry_weight_from,p.standard_dry_weight_to,p.standard_rate_hour
								,p.c_t_standard_per_second,p.customer_name,p.company_of_customer,p.item_code_customers,p.item_classification_customers
								
							order by q.year, q.month,q.day,q.machine_id
			)'''
		cursor.execute(create_view_quality_daily)
		create_monthly_report_view='''create view yv_molds_report as (select 
							q.year, q.month ,q.mold_id,s.mold_name
							,s.c_t_standard_per_second,
							round(avg(q.c_t_actually),0)as c_t_actually,
							round(avg(q.rat_actually),0)as rat_actually,
							round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
							round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
							round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
							round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
							round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
							round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
							round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
							round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
							round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
							m.scrabe_standard,
							
							round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
							
							round(sum(q.gross_production),0)as gross_production,
							round(sum(standard_scrap_weight_kg),1)as standard_scrap_weight_kg,
							round(sum(standard_production_weight_kg),1)as standard_production_weight_kg,
							round(sum(scrap_weight_kg),1) as scrap_weight_kg,
							round(sum(production_weight_kg),1)as production_weight_kg,
							round(count(q.number_day_use),0)as number_day_use,
							round(sum(number_scrab_by_item)/avg(rat_actually),1) as HoursScrap,
							round((sum(q.gross_production)/sum(q.number_day_use))/(22*avg(s.standard_rate_hour)),3)as mold_avalibility /*avalibility bercent in 22 work hours */
							from Yv_quality_inspection_molds q
							left join yv_molds_list s
							on q.mold_id=s.mold_id
						left join yt_machine_list m
						on m.id=q.machine_id
						
							group by q.year, q.month ,m.scrabe_standard,q.mold_id,s.mold_name
							,s.c_t_standard_per_second
							
						order by q.year, q.month )'''
		cursor.execute(create_monthly_report_view)
				

		create_item_report_view='''create view yv_items_molds_report as (select 
								q.year ,q.month, q.mold_id,q.item_id,p.product_name
								,p.product_code
								,p.standard_dry_weight
								,p.standard_dry_weight_from
								,p.standard_dry_weight_to
								,round(avg(q.average_wet_weight),1)as average_wet_weight
								,round(avg(q.average_dry_weight),1)as average_dry_weight
								,round((avg(average_wet_weight)-avg(p.standard_dry_weight))/avg(p.standard_dry_weight),1) as wet_average_percent
								,p.standard_rate_hour as standard_rate_hour
								,p.c_t_standard_per_second c_t_standard_per_second
								,round(avg(q.rat_actually),0)as rat_actually
								,round(avg(q.c_t_actually),0)as c_t_actually
								,round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
								round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
								round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet,
								round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
								round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
								round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
								round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
								round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
								round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
								m.scrabe_standard as scrabe_standard,
								
								round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
								
								round(sum(q.gross_production),0)as gross_production,
								round(sum(standard_scrap_weight_kg),1)as standard_scrap_weight_kg,
								round(sum(standard_production_weight_kg),1)as standard_production_weight_kg,
								round(sum(scrap_weight_kg),1)as scrap_weight_kg,
								round(sum(production_weight_kg),1)as production_weight_kg,
								round(count(q.number_day_use),0)as number_day_use,
								round(sum(number_scrab_by_item)/avg(rat_actually),1) as HoursScrap,
								round(avg(q.mold_avalibility),2)as "mold_avalibility",
								p.customer_name,
								p.item_name_customers,
								p.item_code_customers
								from Yv_quality_inspection_items q
							left join yv_items_master p
							on q.item_id=p.item_id 
							left join yt_machine_list m
							on m.id=q.machine_id
							
								group by q.year,q.month,p.customer_name, q.mold_id,q.item_id,p.product_name,p.item_name_customers,
								p.item_code_customers,p.product_code,p.standard_dry_weight
								,p.standard_dry_weight_from,p.standard_dry_weight_to,p.standard_rate_hour
								,p.c_t_standard_per_second,m.scrabe_standard
								
							order by q.year)'''
		cursor.execute(create_item_report_view)
		conn.commit()
		create_item_report_view='''create view yv_material_product_daily as(select
							q.year, q.month ,q.day,t2.material,q.item_id,p.Product_name,p.product_code
							,p.standard_dry_weight_from,p.standard_dry_weight_to
							,round(avg(q.average_dry_weight),1)as average_dry_weight,p.standard_rate_hour,
							p.c_t_standard_per_second,
							
							round(avg(q.rat_actually),0)as rat_actually,
							round(avg(q.c_t_actually),0)as c_t_actually,
							
							round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
							round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
							round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
							round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
							round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
							round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
							round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
							round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
							round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
							
							round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
							
							round(sum(q.gross_production),0)as gross_production,
							m.scrabe_standard,

							round(count(Items_patchsNumbers),1)as BachesTimesForItem,
							
				 			q.density
							
							from Yv_quality_inspection_items q
							left join yv_items_master p
								on q.item_id=p.item_id
								
				 				left join yt_machine_list m
								on m.id=q.machine_id
							
							left join yv_material_daily_used t2
							on q.density = t2.density and q.day = t2.date_day
							group by q.year, q.month,q.day,t2.material,m.scrabe_standard,q.item_id,p.product_name,p.product_code,p.standard_dry_weight_from,p.standard_dry_weight_to
							,p.standard_rate_hour,p.c_t_standard_per_second,q.density	
							order by q.year,q.month,t2.material,p.product_name)'''
		cursor.execute(create_item_report_view)
		conn.commit()
		print("complete install reports")		

	def import_infrastructure(self):	
		print("_______test_________")
		print(self.folder)
		import_yt_machine_list ='''copy yt_machine_list (id,scrabe_standard,machine_type,place ,low_size,high_size)
		FROM '%s\machines.csv' (FORMAT csv, HEADER, DELIMITER ',');'''%self.folder
		
		cursor.execute(import_yt_machine_list)
		
		conn.commit()
		print("import infrastructure data for day")
	def import_masterdata_molds(self):
		import_yt_molds_list='''copy Yt_molds_list (
			mold_id ,
			ORG_CODE ,
			ORG_NAME ,
			Ctegory ,
			UOM ,
			machie_size ,
			no_on_Set  ,
			set  ,
			sub_category,	
			mold_name ,
			status ,
			c_t_standard_per_second,
			c_t_standard_per_second_from,
			c_t_standard_per_second_to,
			view_molds ,
			gap_mm  ,
			injekors_numbers  ,
			drummers_number  ,
			customer_id  ,
			playback  ,
			gap_tolerance,
			gap_mm_from,
			gap_mm_to,
			machine_parameter_id,
			mold_start_date,
			mold_expire_date,
			customer_name,
			company_of_customer,
			customer_proberty_name,
			customer_proberty_sequence,
			customer_asset_code,
			Customer_Product_Group
			)
			FROM '%s\molds_list.csv' (FORMAT csv, HEADER, DELIMITER ',');'''%self.folder
						
		cursor.execute(import_yt_molds_list)
		conn.commit()
		print("import molds data for day")

	def import_masterdata_parts(self):
		import_ty_parts_list='''
					copy Yt_parts_list (
					id_part,
					product_code,
					product_name_by_parts,
					Weight_kg,
					standard_rate_hour,
					highlite,
					standard_dry_weight,
					standard_dry_weight_from,
					standard_dry_weight_to,
					positive_weight,
					negative_weight,
					sub_category,
					mold_id,
					product_parts,
					item_id,
					product_name,
					item_name_customers,
					item_code_customers,
					item_classification_customers,
					view_items,
					view_molds,
					view_parts,
					density,
					row_material_typeA,
					row_material_typeB,
					tall_mm,
					tall_positive_tolerance,
					tall_negative_tolerance,
					width_mm,
					width_positive_tolerance,
					width_negative_tolerance,
					sicness_mm,
					sicness_positive_tolerance,
					sicness_negative_tolerance,
					id_printed_specification,
					spec_folder_no,
					page_volum_x,
					page_volum_y,
					page_volum_z,
					volume,
					sitotb_color,
					sitotb_set,
					silotib_meter_reels,
					silotib_outside_meter,
					package_page,
					number_bacage,
					page_size_x,
					page_size_y,
					page_colore,
					pages_kgm_set,
					pages_kgm,
					kg_after_add12percent,
					kg_after_add8_5percent,
					id_modification,
					notes,
					silotib_inside_meter
				
					)
					FROM '%s\parts_list.csv' (FORMAT csv, HEADER, DELIMITER ',');
					'''%self.folder

		cursor.execute(import_ty_parts_list)
		conn.commit()
		print("import items data")
	def import_quality_records(self):
		SQL1="copy yt_quality (%s)" %SQL_quality_records
		SQL2=SQL1+" FROM '%s\quality_records.csv' (FORMAT csv, HEADER, DELIMITER ',');"%self.folder
		
		cursor.execute(SQL2)

		conn.commit()
	def import_material_records(self):
		SQL1='''copy yt_material(
			year,
			month,
			day,
			date_day,
			shift,
			machine_id,
			silo_number,
			line_number,
			material,
			ingoing_date,
			density/*density starndards*/,
			standard_denisty_from,
			standard_denisty_to,
			actually_denisty_1,
			actually_denisty_2,
			actually_denisty_3,
			min_actually_denisty,
			midian_actually_denisty,
			max_actually_denisty,
			quantity,
			id_DayUnique,
			row_material_name
			
			)
			'''
		SQL2=SQL1+" FROM '%s\materials.csv' (FORMAT csv, HEADER, DELIMITER ',');"%self.folder
		
		cursor.execute(SQL2)

		conn.commit()
		print("import material records")

	def import_delivery_records(self):
			SQL1='''copy yt_delivery(
					year,
					month,
					weeksNumbers,
					permission_number,
					product_code,
					product_name,
					unit,
					warehouse_type,
					gross_quantity,
					customer_code,
					customer_name,
					sale_order,
					invoice_numbers,
					driver_name,
					freighter,
					deliverad_place,
					planned_date,
					date_date
					)
				'''
			SQL2=SQL1+" FROM '%s\delivery.csv' (FORMAT csv, HEADER, DELIMITER ',');"%self.folder
			
			cursor.execute(SQL2)

			conn.commit()
			print("import delivery records")

							
	#__________________________________________	___________________________________________________#
	#show monthly reports	
	def show_monthly_report_ar(self,year,month,day,to_day):
		SQL1='select * from yv_items_molds_report where year = (%s) '%year
		
		SQL2 = SQL1+' and month=(%s);'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	

	def show_yearly_report_itemsByMonths(self,year,month):
			SQL1='select * from yv_items_molds_report where year = (%s) '%year
			cursor.execute(SQL1)

	def show_monthly_report_view_month(self,year,month):

		SQL1='''with quary_molds_report as (select 
								q.year, q.month ,
								round(avg(q.average_dry_weight),1)as average_dry_weight,
								round(avg(q.rat_actually),0)as rat_actually,
								round(avg(q.c_t_actually),0)as c_t_actually,
								
								round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
								round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
								round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
								round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
								round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
								round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
								round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
								round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
								round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
								
								round(sum(q.sum_scrabe_no_parts),0)as sum_scrabe_no_parts,
								round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
								
								round(sum(q.gross_production),0)as gross_production																
					
				from Yv_quality_inspection_items q
							
							
							left join yv_items_master p
							on q.item_id=p.item_id
							left join yt_machine_list m
							on m.id=q.machine_id
							
								group by q.year, q.month 
								
							order by q.year, q.month 
									)
							select * from quary_molds_report
							where year =(%s)'''%year
		SQL2 = SQL1+' and month = (%s);'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	

	def show_machine_monthly_report(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year, q.month ,q.machine_id,m.scrabe_standard,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually,
									
									round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
									round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
									round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
									round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
									round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
									round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
									round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
									round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
									round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
									
									
									round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
									
									round(sum(q.gross_production),0)as gross_production,
									round(sum(q.gross_production),1)as standard_scrap_weight_kg,
									round(sum(standard_production_weight_kg),1)as standard_production_weight_kg,
									round(sum(scrap_weight_kg),1) as scrap_weight_kg,
									round(sum(production_weight_kg),1)as production_weight_kg ,
									round(sum(HoursScrap),3)as HoursScrap ,
									round(avg(q.mold_avalibility),2)as "mold_avalibility"
									
					from Yv_quality_inspection_items q
								
								left join yv_items_master p
								on q.item_id=p.item_id 
								left join yt_machine_list m
								on m.id=q.machine_id
								
									group by q.year, q.month ,q.machine_id,m.scrabe_standard
								order by q.year, q.month ,q.machine_id
										)
								select * from quary_molds_report
								where year =(%s)'''%year
		#cursor.execute(show_machine_monthly_report)
		SQL2 = SQL1+' and month =(%s);'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	def show_scrap_monthly_report_type_machines(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year, q.month ,q.day,m.scrabe_standard,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually,
									
									round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
									round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
									round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
									round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
									round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
									round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
									round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
									round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
									round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
									
									
									round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
									
									round(sum(q.gross_production),0)as gross_production,
									round(sum(standard_scrap_weight_kg),1)as standard_scrap_weight_kg,
									round(sum(standard_production_weight_kg),1)as standard_production_weight_kg,
									round(sum(scrap_weight_kg),1) as scrap_weight_kg,
									round(sum(production_weight_kg),1)as production_weight_kg ,
									round(sum(HoursScrap),3)as HoursScrap 					
						
					from Yv_quality_inspection_items q
								
								
								left join yv_items_master p
								on q.item_id=p.item_id 
								left join yt_machine_list m
								on m.id=q.machine_id
								
									group by q.year, q.month ,q.day,m.scrabe_standard
									
								order by q.year, q.month ,q.day
										)
								select * from quary_molds_report
								where year =(%s) '''%year
		

		SQL2 = SQL1+' and month = (%s);'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	

	def show_scrap_monthly_report_by_days(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year, q.month ,q.day,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually,
									
									round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
									round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
									round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
									round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
									round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
									round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
									round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
									round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
									round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
									
									round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
									
									round(sum(q.gross_production),0)as gross_production,
									round(sum(standard_scrap_weight_kg),1)as standard_scrap_weight_kg,
									round(sum(standard_production_weight_kg),1)as standard_production_weight_kg,
									round(sum(scrap_weight_kg),1) as scrap_weight_kg,
									round(sum(production_weight_kg),1)as production_weight_kg,
									round(sum(HoursScrap),3)as HoursScrap 						
						
					from Yv_quality_inspection_items q
								
								
								left join yv_items_master p
								on q.item_id=p.item_id 
								left join yt_machine_list m
								on m.id=q.machine_id
								
									group by q.year, q.month ,q.day
									
								order by q.year, q.month ,q.day
										)
								select * from quary_molds_report
								where year =(%s)'''%year
		SQL2 = SQL1+' and month = (%s);'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	def show_machine_yearly_report(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year ,q.machine_id,m.scrabe_standard,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually,
									
									round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
									round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
									round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
									round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
									round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
									round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
									round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
									round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
									round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
									
									
									round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
									
									round(sum(q.gross_production),0)as gross_production,
									round(sum(standard_scrap_weight_kg),1)as standard_scrap_weight_kg,
									round(sum(standard_production_weight_kg),1)as standard_production_weight_kg,
									round(sum(scrap_weight_kg),1) as scrap_weight_kg,
									round(sum(production_weight_kg),1)as production_weight_kg ,
									round(sum(HoursScrap),3)as HoursScrap 
					from Yv_quality_inspection_items q
								
								left join yv_items_master p
								on q.item_id=p.item_id 
								left join yt_machine_list m
								on m.id=q.machine_id
								
									group by q.year ,q.machine_id,m.scrabe_standard
								order by q.year ,q.machine_id
										)
								select * from quary_molds_report
								where year =(%s);'''%year

		cursor.execute(SQL1,)

	def monthly_report_ncr_weight_low(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year, q.month ,q.mold_id,q.item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									
									
									round(count(q.number_day_use),0)as number_day_use,
									m.machine_type,
									round(avg(q.average_dry_weight-p.standard_dry_weight),0)as Weight_deviation,
									round(max(q.average_dry_weight),0)as max_WeightAtmonth,
									round(min(q.average_dry_weight),0)as min_WeightAtMonth,
									round(stddev(q.average_dry_weight),0)as standardWeightDeviationAtMonth
					
						
					from Yv_quality_inspection_items q
								
								
								left join yv_items_master p
								on q.item_id=p.item_id 
								left join yt_machine_list m
								on m.id=q.machine_id
									group by q.year, q.month ,m.machine_type,q.mold_id,q.item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to
									
								order by q.year, q.month 
										)
								select * from quary_molds_report
								where year =(%s)'''%year
		SQL2 = SQL1+'  and month = (%s) and average_dry_weight<standard_dry_weight_from;'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	def monthly_report_ncr_weight_hight(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year, q.month ,q.mold_id,q.item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									
									
									round(count(q.number_day_use),0)as number_day_use,
									m.machine_type,
									round(avg(q.average_dry_weight-p.standard_dry_weight),0)as Weight_deviation,
									round(max(q.average_dry_weight),0)as max_WeightAtmonth,
									round(min(q.average_dry_weight),0)as min_WeightAtMonth,
									round(stddev(q.average_dry_weight),0)as standardWeightDeviationAtMonth
												
						
					from Yv_quality_inspection_items q
								
								
								left join yv_items_master p
								on q.item_id=p.item_id
								left join yt_machine_list m
								on m.id=q.machine_id
									group by q.year, q.month ,m.machine_type,q.mold_id,q.item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to
								order by q.year, q.month 
										)
								select * from quary_molds_report
								where year =(%s) '''%year
		SQL2 = SQL1+'  and month = (%s) and average_dry_weight>standard_dry_weight_to;'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	def monthly_report_ncr_ct(self,year,month):
		SQL1='''with quary_molds_report as (select q.year, q.month ,q.mold_id,p.mold_name,p.standard_rate_hour
									,p.c_t_standard_per_second,
									
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually,
									
									round(count(q.number_day_use),0)as number_day_use,
									m.machine_type ,
									round(avg(q.c_t_actually-p.c_t_standard_per_second),0)as c_t_deviation,
									round(max(q.c_t_actually),0)as max_ctAtmonth,
									round(min(q.c_t_actually),0)as min_ctAtMonth,
									round(stddev(q.c_t_actually),0)as standardCtDeviationAtMonth,
									round(sum(q.gross_production),0)as gross_production,
									round((avg(q.c_t_actually-p.c_t_standard_per_second)*sum(gross_production)/(60*60)),0) as HoursProductionLost,
									round(avg(q.mold_avalibility),2)as mold_avalibility
								from Yv_quality_inspection_molds q
								
							
								left join yv_molds_list p
								on q.mold_id=p.mold_id
								left join yt_machine_list m
								on m.id=q.machine_id						
									group by q.year, q.month ,m.machine_type,q.mold_id,p.mold_name,p.standard_rate_hour
									,p.c_t_standard_per_second
								order by q.year, q.month 
										)
								select * from quary_molds_report
								where year =(%s)'''%year
		
		SQL2 = SQL1+' and month = (%s) and 	c_t_actually>c_t_standard_per_second*1.05'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	def monthly_report_ncr_scrap(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year, q.month ,q.mold_id,q.item_id,p.product_name,p.product_code,m.scrabe_standard,					
									round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,

									round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
									round(sum(q.sum_scrabe_broken_bySet),0)as sum_scrabe_broken_bySet,
									round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
									round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
									round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
									round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
									round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
									round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,

									round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
									
									round(sum(q.gross_production),0)as gross_production,
									round(count(q.number_day_use),0)as number_day_use,
									round((sum(q.number_scrab_by_item))/(sum(q.gross_production)),3)as percentage
																		
								from Yv_quality_inspection_items q
								left join yv_items_master p
								on q.item_id=p.item_id 
								left join yt_machine_list m
								on m.id=q.machine_id
								
									group by q.year, q.month ,q.mold_id,q.item_id,p.product_name,p.product_code,m.scrabe_standard
									
								order by q.year, q.month 
										)
								select * from quary_molds_report			
								where year =(%s)'''%year
		SQL2 = SQL1+' and month = (%s) and percentage>scrabe_standard'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	
	def yearly_report_ncr_weight(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year,q.mold_id,q.item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									
									round(count(q.number_day_use),0)as number_day_use,
									m.machine_type,
									round(avg(q.average_dry_weight-p.standard_dry_weight),0)as Weight_deviation,
									round(max(q.average_dry_weight),0)as max_WeightAtmonth,
									round(min(q.average_dry_weight),0)as min_WeightAtMonth,
									round(stddev(q.average_dry_weight),0)as standardWeightDeviationAtMonth
					from Yv_quality_inspection_items q
								
								
								left join yv_items_master p
								on q.item_id=p.item_id
								left join yt_machine_list m
								on m.id=q.machine_id
									group by q.year,m.machine_type,q.mold_id,q.item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to
									
								order by q.year
										)
								select * from quary_molds_report
								where year =(%s) and (average_dry_weight>standard_dry_weight_to or average_dry_weight<standard_dry_weight_from)'''%year
		
		cursor.execute(SQL1)
	def yearly_report_ncr_ct(self,year,month):
		SQL1='''with quary_molds_report as (select q.year,q.mold_id,p.mold_name,p.standard_rate_hour
									,p.c_t_standard_per_second,
									
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually,
									
									round(count(q.number_day_use),0)as number_day_use,
									m.machine_type,
									round(avg(q.c_t_actually-p.c_t_standard_per_second),0)as c_t_deviation,
									round(max(q.c_t_actually),0)as max_ctAtmonth,
									round(min(q.c_t_actually),0)as min_ctAtMonth,
									round(stddev(q.c_t_actually),0)as standardCtDeviationAtMonth,
									round(sum(q.gross_production),0)as gross_production,
									round((avg(q.c_t_actually-p.c_t_standard_per_second)*sum(gross_production)/(60*60)),0) as HoursProductionLost,
									round(avg(q.mold_avalibility),2)as mold_avalibility


				
								from Yv_quality_inspection_molds q
								
							
								left join yv_molds_list p
								on q.mold_id=p.mold_id
								left join yt_machine_list m
								on m.id=q.machine_id
									group by q.year ,m.machine_type,q.mold_id,p.mold_name,p.standard_rate_hour
									,p.c_t_standard_per_second
								order by q.year 
										)
								select * from quary_molds_report
								where year =(%s) and c_t_actually>c_t_standard_per_second*1.05'''%year
		
		
		cursor.execute(SQL1)
	def yearly_report_ncr_scrap(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year ,q.mold_id,q.item_id,p.product_name,p.product_code,m.scrabe_standard,					
									
									round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
									
									round(sum(q.gross_production),0)as gross_production,
									round(count(q.number_day_use),0)as number_day_use,
									round((sum(q.number_scrab_by_item))/(sum(q.gross_production)),3)as percentage
																		
								from Yv_quality_inspection_items q
								left join yv_items_master p
								on q.item_id=p.item_id 
								left join yt_machine_list m
								on m.id=q.machine_id
								
									group by q.year ,q.mold_id,q.item_id,p.product_name,p.product_code,m.scrabe_standard
									
								order by q.year
										)
								select * from quary_molds_report			
								where year =(%s) and percentage>scrabe_standard'''%year
		
		cursor.execute(SQL1)
	def get_daily_dataentry_items(self,year,month,*args):
		SQL1='''with quary_molds_report as (select * from yv_molds_report_daily
								
									)
							select * from quary_molds_report where year=(%s)'''%year
		
		SQL2 = SQL1+' and month = (%s)'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
#		SQL3 = SQL1+' and mold_id = (%s)'
#		cursor.execute(SQL3, (args, ))
		
	def get_daily_dataentry_items_yearly(self,year,month,day,to_day):
		SQL1='''with quary_items_report as (select * from yv_molds_report_daily
									)
							select * from quary_items_report where year=(%s)'''%year
	
		cursor.execute(SQL1)	
	def yearly_report_molds_byWeeks(self,year,month,day,to_day):
		SQL1='''with quary_items_report_by_week as (select * from yv_molds_report_daily
									)
							select * from quary_items_report_by_week
							group by year,month,weeksNumbers
							where year=(%s)'''%year
		SQL2=SQL1+'''and month %s'''%month
		SQL3=SQL2+'''and day >= %s'''%day
		SQL4=SQL3+'''and day < %s'''%to_day
	
		cursor.execute(SQL4)	

	def show_machine_report_yearly(self,year,month):
		show_machine_report_yearly='''with quary_molds_report as (select 
									q.year, q.month,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually,
									
									round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
									round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
									round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
									round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
									round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
									round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
									round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
									round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
									round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
									
									round(sum(q.sum_scrabe_no_parts),0)as sum_scrabe_no_parts,
									round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
									round(sum(q.gross_production),0)as gross_production,
									round(count(q.number_day_use),0)as number_day_use,
								/*	round(count(unique(q.machine_id)),0)as machines_number, */
									round(min(q.machine_id),0)as machines_min_use,
									round(max(q.machine_id),0)as machines_max_use						
					from Yv_quality_inspection_items q
								
								
								left join yv_items_master p
								on q.item_id=p.item_id
								left join yt_machine_list m
								on m.id=q.machine_id
								
									group by q.year, q.month 
									
								order by q.year, q.month
										)
								select * from quary_molds_report
								where year =(%s)'''%year
		cursor.execute(show_machine_report_yearly)
	def items_report_arabic_custom_item(self,year,*args):
		

		SQL1='''select %s '''%sql_quality_reporty_yearly_item
		SQL2=SQL1+''' from yv_items_molds_report
		
			where year = (%s) '''%year
	

		SQL3=SQL2+''' group by year ,customer_name,scrabe_standard, mold_id,item_id,product_name
			,product_code,standard_dry_weight,standard_dry_weight_from,standard_dry_weight_to,standard_rate_hour,c_t_standard_per_second order by year;
			'''
		
		if type(args) == tuple:   
			cursor.execute(SQL3)
		else:  
			SQL_mold = SQL2+''' and item_id =(%s) group by year ,customer_name,scrabe_standard, mold_id,item_id,product_name
			,product_code,standard_dry_weight,standard_dry_weight_from,standard_dry_weight_to,standard_rate_hour,c_t_standard_per_second order by year;'''
			cursor.execute(SQL_mold, (args, ))


		
	def show_yearly_report_molds(self,year,month,*args):#report depend of mold structure
			SQL1='''select %s '''%sql_quality_reporty_yearly_mold
			SQL2=SQL1+''' from yv_molds_report 
			
			 where year = (%s) '''%year
		

			SQL3=SQL2+'''group by year ,scrabe_standard,mold_id,mold_name 
			,c_t_standard_per_second 
			order by year
			 '''
			
			if type(args) == tuple:   
				cursor.execute(SQL3)
			else:  
				SQL_mold = SQL2+''' and mold_id =(%s) group by year ,scrabe_standard,mold_id,mold_name 
			,c_t_standard_per_second order by year;'''
				cursor.execute(SQL_mold, (args, ))

	def show_mnthly_report_molds(self,year,month):#report depend of mold structure
			#report depend of mold structure
		SQL1='''
							with quary_molds_report as (select * from yv_molds_report)
						select * from quary_molds_report
						where year = (%s) '''%year
		SQL2 = SQL1+' and month =(%s);'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	def yearly_report_molds_byMonthes(self,year,*args):#report depend of mold structure
			#report depend of mold structure
		SQL1='''
							
							with quary_molds_report as(select * from yv_molds_report)
										
							select * from quary_molds_report	
							
						where year = (%s) '''%year
		#ALTER TABLE quary_molds_report DROP COLUMN month
		SQL2 = SQL1+' and mold_id =(%s);'
		if type(args) == tuple:   			#for filter for specific items
			cursor.execute(SQL1)
		else:
			cursor.execute(SQL2, (args, ))

	
	# for baches re
	
	def show_monthly_Baches(self,year,month):#report depend of mold structure
			#report depend of mold structure
		SQL1='''with monthly_baches_report as (select
							q.year, q.month ,q.Items_patchsNumbers,q.item_id,p.Product_name,p.product_code
							,p.standard_dry_weight_from,p.standard_dry_weight_to
							,round(avg(q.average_dry_weight),1)as average_dry_weight,p.standard_rate_hour,
							p.c_t_standard_per_second,
							
							round(avg(q.rat_actually),0)as rat_actually,
							round(avg(q.c_t_actually),0)as c_t_actually,
							
							round(sum(q.sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
							round(sum(q.sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
							round(sum(q.sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
							round(sum(q.sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
							round(sum(q.sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
							round(sum(q.sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
							round(sum(q.sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
							round(sum(q.sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
							round(sum(q.sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
							
							round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
							
							round(sum(q.gross_production),0)as gross_production,
							m.scrabe_standard,

							round(count(Items_patchsNumbers),1)as BachesTimesForItem,
							bachStartDate

							
							bachStartDate
							from Yt_quality q
							left join yv_items_master p
							on q.item_id=p.item_id
						left join yt_machine_list m
						on m.id=q.machine_id
						
							group by q.year, q.month,m.scrabe_standard,q.item_id,p.product_name,p.product_code,p.standard_dry_weight_from,p.standard_dry_weight_to
							,p.standard_rate_hour,p.c_t_standard_per_second,q.Items_patchsNumbers,bachStartDate		
							)
							select distinct t1.* ,t2.bachEndDate
							from monthly_baches_report t1
							left join 
								(select year, month ,Items_patchsNumbers ,bachEndDate
									from
									Yt_quality q 
									where bachEndDate is not null
									group by year, month ,Items_patchsNumbers,bachEndDate)t2
							on t1.Items_patchsNumbers=t2.Items_patchsNumbers
							
							
						where t1.year = (%s) 
							'''%year
		SQL2 = SQL1+' and t1.month =(%s) order by t1.year, t1.month ,t1.bachStartDate DESC;'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	
	def deliveryToCustomers_week(self,year):#report depend of mold structure
			#report depend of mold structure
		SQL1='''with material_product as (select
							
							year,
							month,
							weeksNumbers,
							permission_number,
							product_code,
							product_name,
							unit,
							warehouse_type,
							gross_quantity,
							customer_code,
							customer_name,
							sale_order,
							invoice_numbers,
							driver_name,
							freighter,
							deliverad_place,
							planned_date,
							date_date
							

				
							from delivery_to_customers
							
							group by year, month,material,scrabe_standard,item_id,product_name,product_code,standard_dry_weight_from,standard_dry_weight_to
							,standard_rate_hour,c_t_standard_per_second,density
							)
							select distinct t1.* 
							from material_product t1
							
							where year = (%s)
							order by year , month  , material,product_name'''%year
		
		if type(year) == tuple:   
			cursor.execute(SQL1, year)	
		else:
			cursor.execute(SQL1, (year,))	
	
	def show_water_content_daily(self,year,month,day,to_day):#report depend of mold structure
			SQL1='''select %s '''%sql_quality_water_content
			sql2=SQL1+''' from yv_molds_report_daily 
			
			 where year = %s  ''' %year 
			sql3=sql2+'''and month =%s 
						group by year ,month,day,machine_id,mold_id,item_id,product_code,
						product_name,standard_dry_weight,standard_dry_weight_from,
						standard_dry_weight_to order by day'''  %month

			if type(month) == tuple:   
				cursor.execute(sql3, month)	
			else:
				cursor.execute(sql3,(month,))

		#______________________________second section___________________________________________#
		#this install as dublicate data for 2nd way to analysis data by create separated tables then collect it
			#
class Material():
	def material_bySilo_daily(self,year,month,day,to_day):#report depend of mold structure
			#report depend of mold structure
		SQL0='''select %s  '''%sql_material_daily
		SQL1=SQL0+''' from yt_material q where year = (%s)'''%year
		SQL2=SQL1+'''and month= (%s) '''%month
		SQL3=SQL2+'''and day=(%s) order by date_day,shift,silo_number,material
				 '''%day
	
		cursor.execute(SQL3)	
	def materialToPorduct_daily(self,year):#report depend of mold structure
			#report depend of mold structure
		SQL1='''select * from yv_material_product_daily q
							
							
							where year = (%s)
							order by year , month  , material,product_name'''%year
		
		if type(year) == tuple:   
			cursor.execute(SQL1, year)	
		else:
			cursor.execute(SQL1, (year,))	
	def materialToPorduct(self,year):#report depend of mold structure
			#report depend of mold structure
		SQL1='''with material_product as (select
							year, month ,material,item_id,Product_name,product_code
							,standard_dry_weight_from,standard_dry_weight_to
							,round(avg(average_dry_weight),1)as average_dry_weight,standard_rate_hour,
							c_t_standard_per_second,
							
							round(avg(rat_actually),0)as rat_actually,
							round(avg(c_t_actually),0)as c_t_actually,
							
							round(sum(sum_scrabe_shortage_bySet),0)as sum_scrabe_shortage_bySet,
							round(sum(sum_scrabe_roll_bySet),0)as sum_scrabe_roll_bySet,
							round(sum(sum_scrabe_broken_bySet  ),0)as sum_scrabe_broken_bySet  ,
							round(sum(sum_scrabe_curve_bySet),0)as sum_scrabe_curve_bySet,
							round(sum(sum_scrabe_shrinkage_bySet),0)as sum_scrabe_shrinkage_bySet,
							round(sum(sum_scrabe_dimentions_bySet),0)as sum_scrabe_dimentions_bySet,
							round(sum(sum_scrabe_weight_bySet),0)as sum_scrabe_weight_bySet,
							round(sum(sum_scrabe_dirty_bySet),0)as sum_scrabe_dirty_bySet,
							round(sum(sum_scrabe_cloration_bySet),0)as sum_scrabe_cloration_bySet,
							
							round(sum(number_scrab_by_item),0)as number_scrab_by_item,
							
							round(sum(gross_production),0)as gross_production,
							scrabe_standard,

							round(count(Product_name),1)as number_use_day,
							
				 			density

				
							from yv_material_product_daily q
							
							group by year, month,material,scrabe_standard,item_id,product_name,product_code,standard_dry_weight_from,standard_dry_weight_to
							,standard_rate_hour,c_t_standard_per_second,density
							)
							select distinct t1.* 
							from material_product t1
							
							where year = (%s)
							order by year , month  , material,product_name'''%year
		
		if type(year) == tuple:   
			cursor.execute(SQL1, year)	
		else:
			cursor.execute(SQL1, (year,))	
class PgAccess():
	'''
		this class for manage data base structre
		
	'''		
	def __init__(self,folder,table):
		self.folder=folder
		self.table=table
	def head_show_monthly_Baches(self):
				#with psycopg2.connect(DSN) as connection:
			SQL1="select column_name from information_schema.columns where table_schema = 'public' and table_name='%s'"%table
			cursor.execute(SQL1)	
	def updateTable(self,table,column, day,item_id,newValue):
		
			print("Table Before updating record ")
			
			SQL1_column = """select %s """%column
			SQL2_table=SQL1_column+'from %s '%table
			SQL3_day=SQL2_table+'where year=2020 and month=2 and day =%s '%self.day
			SQL3_row=SQL3_day+'and item_id=%s;'
			cursor.execute(SQL3_row, (item_id, ))
			record = cursor.fetchone()
			#record = cursor.fetchall()
			print(record)
			
			# Update single record now
			updateSQL1_column = """Update %s """%table
			updateSQL2_table=SQL1_column+'set %s '%column
			updateSQL3_day=SQL2_table+'where year=2020 and month=2 and day =%s '%day
			updateSQL3_row=SQL3_day+'and item_id=%s;'
			cursor.execute(SQL3_row, (item_id, ))

			sql_update_query = """Update yt_quality set where year=2020 and month=2 and day =5 and item_id=%s"""
			
	def delete_rows(self,table,year,month,*args,monthly=True):
			
		SQL_table=' DELETE from %s '%table
		SQL_year=SQL_table+'where year=%s'%year
		SQL_month=SQL_year+' and month =%s '%month
				
		#SQL3_row=SQL3_day+'and item_id=%s;
		#if args == ():   			#for filter for specific items
		#	cursor.execute(SQL_month)
		if monthly:
			cursor.execute(SQL_month)
		else:
			#day=int(args)
			SQL_day=SQL_month+' and day =%s '%args

			cursor.execute(SQL_day)	
			
		conn.commit()
		print("deleting rows for day "+str(args) ,"in month: "+str(month),"in year:"+str(year))

	#manage tables
	def select_tables(self,table,column_name,*args):
		
		sql1=' select %s '%column_name
		sql2=sql1+'from %s'%table
		
		print (cursor.mogrify(sql2))
		cursor.execute(sql2)	
		conn.commit()
		
	def alterTybe_columns(self,table,column_name,datatype,*args):
			
		SQL_table=' alter table %s '%table
		SQL2=SQL_table+'ALTER COLUMN %s'%column_name
		SQL3=SQL2+' %s '%datatype
							
		cursor.execute(SQL3)	
		
		conn.commit()
		print("alter table "+str(table) ,"column "+str(column_name)," to data type"+str(datatype))

	def alterName_columns(self,table,column_name,newName,*args):
			
		SQL_table=' alter table %s '%table
		SQL2=SQL_table+'rename COLUMN %s'%column_name
		SQL3=SQL2+' to %s '%newName
							
		cursor.execute(SQL3)	
		
		conn.commit()
		print("alter table "+str(table) ,"column "+str(column_name),"to:"+str(newName))
	
	def add_columns(self,table,column_name,dataType,*args):
		SQL_table=' alter table %s '%table
		SQL2=SQL_table+'add COLUMN %s'%column_name
		SQL3=SQL2+' %s '%dataType
							
		cursor.execute(SQL3)	
		
		conn.commit()
		print("add column "+str(column_name) ,"in table name "+str(table),"table tybe "+str(dataType))
	def drop_columns(self,table,column_name):
		SQL_table=' alter table %s '%table
		SQL2=SQL_table+'drop COLUMN %s'%column_name
		cursor.execute(SQL2)	
		conn.commit()
		print("drop column "+str(column_name) ,"in table name "+str(table))