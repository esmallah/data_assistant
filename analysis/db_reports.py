from config.memory.database_postgrs import cursor,conn
#from .database_sqlite import conn , cursor
#t22records_reports
SQL_quality_records="""
				year,
				month,
				day,
				f14machine_id,
				f11part_item_id,
				number_day_use,
				f12molds_id,
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
				
				f11part_id,
				factory,
				shift1_tall_mm,
				shift2_tall_mm,
				shift1_width_mm,
				shift2_width_mm,
				shift1_deepth_mm,
				shift2_deepth_mm,
				shift2_deepth_mm,
				shift1_denisty,
				shift2_denisty,

				id_DayPartUnique,
				parts_patchsNumbers,
				Items_patchsNumbers,
				bachStartDate,
				date_day,
				bachEndDate
				"""

create_calculation_trigger='''
			CREATE FUNCTION sum_scrabs() RETURNS trigger AS $sum_scrabs$
		BEGIN
			-- Check that scrap and production are given
			IF old.shift1_scrabe_no_parts IS NULL THEN
				NEW.shift1_scrabe_no_parts=old.shift1_scrabe_shortage+
				old.shift1_scrabe_roll +
				old.shift1_scrabe_broken +
				old.shift1_scrabe_curve +
				old.shift1_scrabe_shrinkage +
				old.shift1_scrabe_dimentions +
				old.shift1_scrabe_weight +
				old.shift1_scrabe_dirty +
				old.shift1_scrabe_cloration 
				;
			END IF;
			IF old.shift2_scrabe_no_parts IS NULL THEN
				NEW.shift2_scrabe_no_parts=old.shift2_scrabe_shortage+
				old.shift2_scrabe_roll +
				old.shift2_scrabe_broken +
				old.shift2_scrabe_curve +
				old.shift2_scrabe_shrinkage +
				old.shift2_scrabe_dimentions +
				old.shift2_scrabe_weight +
				old.shift2_scrabe_dirty +
				old.shift2_scrabe_cloration 
				;
			END IF;
			-- Who works for us when they must pay for it?
			IF old.sum_scrabe_no_parts IS NULL THEN
				new.sum_scrabe_no_parts=new.shift1_scrabe_no_parts+new.shift2_scrabe_no_parts
				;
			END IF;
			-- Remember who changed the payroll when
				RETURN NEW;
					END;
				$sum_scrabs$ LANGUAGE plpgsql;
				CREATE TRIGGER sum_scrabs AFTER INSERT OR UPDATE ON insutech.t10inventory
					FOR EACH ROW EXECUTE FUNCTION sum_scrabs();
		'''


sql_quality_reporty_yearly_item='''
								year , f12molds_id,f11part_item_id,product_name
								,product_code
								,standard_dry_weight
								,standard_dry_weight_from
								,standard_dry_weight_to
								,round(avg(average_wet_weight),1)as average_wet_weight
								,round(avg(average_dry_weight),1)as average_dry_weight
								,round(avg(average_wet_weight)-standard_dry_weight/avg(standard_dry_weight),1) as wet_average_percent
								,standard_rate_hour as standard_rate_hour
								,c_t_standard_per_second c_t_standard_per_second
								,round(avg(rat_actually),0)as rat_actually
								,round(avg(c_t_actually),0)as c_t_actually,
								
								customer_name,
								item_name_customers,
								item_code_customers
								
'''
sql_quality_reporty_yearly_mold='''year, f12molds_id,mold_name
					,c_t_standard_per_second,
							round(avg(rat_actually),0)as rat_actually,
							round(avg(c_t_actually),0)as c_t_actually
							
					'''
sql_quality_water_content='''
				year,
				month,
				day,
				f11part_item_id,
				f12molds_id
				,product_name,
				product_code
				f14machine_id,
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
veiw_quality_daily='''
				q.year,
				q.month,
				q.day,
				q.date_day,
				q.f14machine_id,
				q.f11part_item_id,
				q.number_day_use,
				q.f12molds_id,
				q.product_parts,
				q.shift1_wet_weight1,
				q.shift1_wet_weight2,
				q.shift1_wet_weight3,
				q.shift1_wet_weight4,
				q.shift1_wet_weight5,
				q.shift1_dry_weight1,
				q.shift1_dry_weight2,
				q.shift1_dry_weight3,
				q.shift1_dry_weight4,
				q.shift1_dry_weight5,
				q.shift1_c_t1,
				q.shift1_c_t2,
				q.shift2_wet_weight1,
				q.shift2_wet_weight2,
				q.shift2_wet_weight3,
				q.shift2_wet_weight4,
				q.shift2_wet_weight5,
				q.shift2_dry_weight1,
				q.shift2_dry_weight2,
				q.shift2_dry_weight3,
				q.shift2_dry_weight4,
				q.shift2_dry_weight5,
				q.shift2_c_t1,
				q.shift2_c_t2,
				q.shift1_production_cards,
				q.shift1_prod_page,
				q.shift1_proper_production,
				q.shift1_scrabe_shortage,
				q.shift1_scrabe_roll,
				q.shift1_scrabe_broken,
				q.shift1_scrabe_curve,
				q.shift1_scrabe_shrinkage,
				q.shift1_scrabe_dimentions,
				q.shift1_scrabe_weight,
				q.shift1_scrabe_dirty,
				q.shift1_scrabe_cloration,
				
				q.shift2_production_cards,
				q.shift2_prod_page,
				q.shift2_proper_production,
				q.shift2_scrabe_shortage,
				q.shift2_scrabe_roll,
				q.shift2_scrabe_broken,
				q.shift2_scrabe_curve,
				q.shift2_scrabe_shrinkage,
				q.shift2_scrabe_dimentions,
				q.shift2_scrabe_weight,
				q.shift2_scrabe_dirty,
				q.shift2_scrabe_cloration,
				
				q.f11part_id,
				q.factory,
				q.shift1_tall_mm,
				q.shift1_width_mm,
				q.shift1_deepth_mm,
				q.shift2_tall_mm,
				q.shift2_width_mm,
				q.shift2_deepth_mm,
				q.shift1_denisty,
				q.shift2_denisty
					'''
veiw_customer_complaints='''
				f112partners_id,
				date,
				attachment_name,
				f121risk_id,
				type,
				f5channel_id,
				f11part_item_id,
				date_request_in,
				receiver,
				verification_details,
				validation_details,
				cause_details,
				f74problems_id_layer0,
				f74problems_id_layer1,
				f74problems_id_layer2,
				f74problems_id,
				nondescovery_cause,
				field_stringlong,
				corrective_action_details,
				problem_summary,
				verification_result,
				date_request_out,
				status,
				date_closing,
				year,
				month,
				requester,
				'''
product_return_column='''
			t22.field_integer,
			q.f11part_item_id,
			t22.f112partners_id,
			t22.date,
			t22.year,
			t22.month,
			t22.f127means_id,
			t22.f121risk_id,
			t10.return_quantity,
			t10.number_delivery,
			t10.return_good,
			t10.return_downgrade,
			t10.return_scrap
			
				'''

class Block():
	'''this class for manage data base on sahrenetowrk or cpanel to mold categories in foam industries'''		
	def __init__(self,folder,table):
		self.folder=folder
		self.table=table	
	def server_pc_qa(self,year,month,day):
		#for get last year and month and day form loaded database
		SQL1='''select * from  insutech.t10inventory where year=%s'''%year
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
		table_name="insutech.t10inventory"
					
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
			
			drop_v100items_molds_report=	'''drop view v100items_molds_report'''
			cursor.execute(drop_v100items_molds_report)
			
			drop_v101molds_report_daily=	'''drop view v101molds_report_daily'''
			cursor.execute(drop_v101molds_report_daily)

			drop_v102molds_report=	'''drop view v102molds_report'''
			cursor.execute(drop_v102molds_report)

			drop_v103material_product_daily='''drop view v103material_product_daily '''
			cursor.execute(drop_v103material_product_daily)

			drop_v104material_daily_used='''drop view v104material_daily_used '''
			cursor.execute(drop_v104material_daily_used)

			drop_v105quality_inspection_items=		'''drop view v105quality_inspection_items'''
			cursor.execute(drop_v105quality_inspection_items)
			
			
			drop_v107quality_inspection_parts='''drop view v107quality_inspection_parts '''
			cursor.execute(drop_v107quality_inspection_parts)

			drop_v106quality_inspection_molds=		'''drop view v106quality_inspection_molds'''
			cursor.execute(drop_v106quality_inspection_molds)

			drop_quality_daily_calculator='''drop view v10quality_inpsection'''
			cursor.execute(drop_quality_daily_calculator)
			
			conn.commit()	
			print("complete uninistall reports")
	def uninstall_records(self):
			#for uninstall records tables
			drop_yt_quality=	'''drop table t10inventory''' 
#			cursor.execute(drop_yt_quality)
#			conn.commit()
			print("complete uninistall quality records")
	def uninstall_maretial(self):
			#for uninstall records tables
			drop_t13material_mixed=	'''drop table insutech.t13material_mixed''' 
#			cursor.execute(drop_t13material_mixed)
#			conn.commit()
			print("complete uninistall material record")
					

	def uninstall_masterdata(self):
			drop_v108items_master='''drop view v108items_master'''
			cursor.execute(drop_v108items_master)

			drop_v96item_specifications='''drop view v96item_specifications'''
			cursor.execute(drop_v96item_specifications)
			
			drop_v96item_specifications='''drop view v12molds_list'''#new
			cursor.execute(drop_v96item_specifications)
					
			
			conn.commit()
			print("complete uninistall master data")
	def uninstall_infrastrucure(self):
			drop_t14machine_list='''drop table t14machine'''
			cursor.execute(drop_t14machine_list)
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
			create_table_machine_list='''create table insutech.t14machine (id int primary key,name varchar(50),scrabe_standard numeric , machine_type varchar(50),place varchar(50),low_size varchar(50) null,high_size varchar(50) ,machineStatus boolean);'''
			cursor.execute(create_table_machine_list)
			conn.commit()
			print("complete inistall infrastructure data")
	
	def install_master_data(self):
			create_table_molds_list='''create table insutech.t12molds (
				mold_id int primary key,
				ORG_CODE varchar(50),
				ORG_NAME varchar(50),
				Ctegory varchar(50),
				UOM varchar(50),
				machine_size varchar(50),
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
#			cursor.execute(create_table_molds_list)
			
			create_table_parts_list='''
			CREATE TABLE IF NOT EXISTS insutech.t11parts
			(
			id_part character varying(50) COLLATE pg_catalog."default" NOT NULL,
			product_code character varying(100) COLLATE pg_catalog."default",
			product_name_by_parts character varying(300) COLLATE pg_catalog."default",
			weight_kg numeric,
			standard_rate_hour integer,
			highlite character varying(50) COLLATE pg_catalog."default",
			standard_dry_weight numeric,
			standard_dry_weight_from numeric,
			standard_dry_weight_to numeric,
			positive_weight numeric,
			negative_weight numeric,
			sub_category character varying(50) COLLATE pg_catalog."default",
			mold_id integer,
			product_parts character varying(50) COLLATE pg_catalog."default",
			item_id integer,
			product_name character varying(300) COLLATE pg_catalog."default",
			item_name_customers character varying(100) COLLATE pg_catalog."default",
			item_code_customers character varying(50) COLLATE pg_catalog."default",
			item_classification_customers character varying(120) COLLATE pg_catalog."default",
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
			id_printed_specification integer,
			spec_folder_no integer,
			page_volum_x numeric,
			page_volum_y numeric,
			page_volum_z numeric,
			volume numeric,
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
			id_modification integer,
			notes character varying(300) COLLATE pg_catalog."default",
			silotib_inside_meter numeric,
			mother_id integer,
			standard_wet_weight_from numeric,
			standard_wet_weight numeric,
			standard_wet_weight_to numeric,
			mold_numbers_to_same_item integer,
			no_duplication integer,
			dublication character varying COLLATE pg_catalog."default",
			note character varying COLLATE pg_catalog."default",
			weight_net_gm numeric,
			unit character varying COLLATE pg_catalog."default",
			id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
			describtion character varying(1024) COLLATE pg_catalog."default",
			category character varying(255) COLLATE pg_catalog."default",
			uom character varying(255) COLLATE pg_catalog."default",
			CONSTRAINT yt_parts_list_pkey PRIMARY KEY (id_part)
		)
		WITH (
			OIDS = FALSE
		)
		TABLESPACE pg_default;

		ALTER TABLE insutech.t11parts
			OWNER to postgres;

		GRANT ALL ON TABLE insutech.t11parts TO postgres;

		GRANT SELECT ON TABLE insutech.t11parts TO quality;

		'''
#			cursor.execute(create_table_parts_list)

			create_view_molds_list='''/* list molds by all informatio for molds only (not any parts) */create view v12molds_list as (select M.*,p.standard_rate_hour
								from insutech.t11parts p
							left join insutech.t12molds M
							on p.f12molds_id=M.mold_id
							where p.view_molds is not null)
							'''
			cursor.execute(create_view_molds_list)

			create_view_item_specification='''create view v96item_specifications as (select p.* ,M.machine_size 
									  ,M.set  ,M.mold_name ,m.density,
									M.f112partners_id_customer ,M.c_t_standard_per_second ,	M.c_t_standard_per_second_from ,
								M.c_t_standard_per_second_to
								from insutech.t11parts p
							left join insutech.t12molds M
							on p.f12molds_id=M.mold_id)'''
			cursor.execute(create_view_item_specification)
			
			create_view_item_master='''create view v108items_master as (select p.* ,M.machine_size 
									  ,M.set  ,M.mold_name ,m.density,
									M.f112partners_id_customer  ,M.c_t_standard_per_second ,	M.c_t_standard_per_second_from ,
								M.c_t_standard_per_second_to ,h.name as customer_name,h.formal_name as company_of_customer,h.partner_id as customer_id
								from insutech.t11parts p
							left join insutech.t12molds M
							on p.f12molds_id=M.mold_id
							left join insutech.t112partners h
							on h.partner_id=M.f112partners_id_customer
							where p.view_items=1)'''
			cursor.execute(create_view_item_master)
			conn.commit()
			print("complete install master data")
			
	def install_records(self):
			create_table_quality='''
		
		CREATE TABLE IF NOT EXISTS insutech.t10inventory
		(
			year integer NOT NULL,
			month integer NOT NULL,
			day integer NOT NULL,
			machine_id integer,
			item_id integer NOT NULL,
			number_day_use integer,
			mold_id integer,
			product_parts character varying(50) COLLATE pg_catalog."default",
			shift1_wet_weight1 numeric,
			shift1_wet_weight2 numeric,
			shift1_wet_weight3 numeric,
			shift1_wet_weight4 numeric,
			shift1_wet_weight5 numeric,
			shift1_dry_weight1 numeric,
			shift1_dry_weight2 numeric,
			shift1_dry_weight3 numeric,
			shift1_dry_weight4 numeric,
			shift1_dry_weight5 numeric,
			shift1_c_t1 integer,
			shift1_c_t2 integer,
			shift2_wet_weight1 numeric,
			shift2_wet_weight2 numeric,
			shift2_wet_weight3 numeric,
			shift2_wet_weight4 numeric,
			shift2_wet_weight5 numeric,
			shift2_dry_weight1 numeric,
			shift2_dry_weight2 numeric,
			shift2_dry_weight3 numeric,
			shift2_dry_weight4 numeric,
			shift2_dry_weight5 numeric,
			shift2_c_t1 integer,
			shift2_c_t2 integer,
			average_wet_weight numeric,
			average_dry_weight numeric,
			rat_actually integer,
			rat_validation integer,
			c_t_actually integer,
			shift1_production_cards integer,
			shift1_prod_page numeric,
			shift1_proper_production integer,
			shift1_scrabe_shortage integer,
			shift1_scrabe_roll integer,
			shift1_scrabe_broken integer,
			shift1_scrabe_curve integer,
			shift1_scrabe_shrinkage integer,
			shift1_scrabe_dimentions integer,
			shift1_scrabe_weight integer,
			shift1_scrabe_dirty integer,
			shift1_scrabe_cloration integer,
			shift1_scrabe_no_parts integer,
			shift1_scrabe_no_item integer,
			shift1_all_production integer,
			shift2_production_cards integer,
			shift2_prod_page integer,
			shift2_proper_production integer,
			shift2_scrabe_shortage integer,
			shift2_scrabe_roll integer,
			shift2_scrabe_broken integer,
			shift2_scrabe_curve integer,
			shift2_scrabe_shrinkage integer,
			shift2_scrabe_dimentions integer,
			shift2_scrabe_weight integer,
			shift2_scrabe_dirty integer,
			shift2_scrabe_cloration integer,
			shift2_scrabe_no_parts integer,
			shift2_scrabe_no_item integer,
			shift2_all_production integer,
			sum_scrabe_shortage_byset integer,
			sum_scrabe_roll_byset integer,
			sum_scrabe_broken_byset integer,
			sum_scrabe_curve_byset integer,
			sum_scrabe_shrinkage_byset integer,
			sum_scrabe_dimentions_byset integer,
			sum_scrabe_weight_byset integer,
			sum_scrabe_dirty_byset integer,
			sum_scrabe_cloration_byset integer,
			sum_scrabe_no_parts integer,
			number_scrab_by_item integer,
			gross_production integer,
			scrap_percent_by_item numeric,
			part_id character varying(50) COLLATE pg_catalog."default" NOT NULL,
			factory character varying(50) COLLATE pg_catalog."default",
			shift1_tall_mm character varying(100) COLLATE pg_catalog."default",
			shift2_tall_mm character varying(100) COLLATE pg_catalog."default",
			shift1_width_mm character varying(100) COLLATE pg_catalog."default",
			id_daypartunique character varying(50) COLLATE pg_catalog."default",
			parts_patchsnumbers character varying(50) COLLATE pg_catalog."default",
			items_patchsnumbers character varying(50) COLLATE pg_catalog."default",
			bachstartdate date,
			bachenddate date,
			date_day date,
			shift2_width_mm numeric,
			shift1_deepth_mm numeric,
			shift2_deepth_mm numeric,
			shift1_denisty numeric,
			shift2_denisty numeric,
			actuall_destiny_average numeric,
			actuall_tall_mm_average numeric,
			actuall_width_mm_average numeric,
			actuall_deep_mm_average numeric,
			product_code character varying COLLATE pg_catalog."default",
			weigh_net_gm numeric,
			visual_defect1 boolean,
			visual_defect2 boolean,
			visual_defect3 boolean,
			visual_defect4 boolean,
			visual_defect5 boolean,
			visual_defect6 boolean,
			visual_defect7 boolean,
			visual_defect8 boolean,
			visual_defect9 boolean,
			mother_id integer NOT NULL,
			attachment_id integer,
			"select" boolean,
			disable boolean,
			change_id integer,
			ncr_id integer,
			level_id integer,
			user_create character varying COLLATE pg_catalog."default",
			user_update character varying COLLATE pg_catalog."default",
			datecreate date,
			dateupdate date,
			shif1_tall2_mm numeric,
			shif1_width2_mm numeric,
			shift2_deepth2_mm numeric,
			shift1_deepth2_mm numeric,
			shif2_tall2_mm numeric,
			shif2_width2_mm numeric,
			id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 110419 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
			weight_kg1 numeric,
			weight_kg2 numeric,
			weight_kg3 numeric,
			weight_kg4 numeric,
			weight_kg5 numeric,
			weight_kg6 numeric,
			weight_kg7 numeric,
			weight_kg8 numeric,
			weight_kg9 numeric,
			weight_kg10 numeric,
			average_weight_kg numeric,
			weight_deviation_kg numeric,
			CONSTRAINT insutech.t10inventory_pkey PRIMARY KEY (id),
			CONSTRAINT yt_quality_id_daypartunique_key UNIQUE (id_daypartunique)
				)
				WITH (
					OIDS = FALSE
				)
				TABLESPACE pg_default;

				ALTER TABLE insutech.t10inventory
					OWNER to postgres;

				GRANT ALL ON TABLE insutech.t10inventory TO quality;

				GRANT ALL ON TABLE insutech.t10inventory TO postgres;

				COMMENT ON COLUMN insutech.t10inventory.weigh_net_gm
				IS 'between weight net weight and dry weight';
			'''
			cursor.execute(create_table_quality)
			conn.commit()
			print("complete install quality records")

	def install_records_material(self):
			create_table_material='''
				create table insutech.t13material_mixed (
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

	def install_calculation_viws(self):
		calculate_quality_daily='''create view v10quality_inpsection as
		 (select %s,
			(q.shift2_scrabe_shortage + q.shift1_scrabe_shortage) / s.no_on_set as sum_scrabe_shortage_byset ,
			(q.shift1_scrabe_roll + q.shift2_scrabe_roll ) / s.no_on_set as sum_scrabe_roll_byset ,
			(q.shift1_scrabe_broken + q.shift2_scrabe_broken ) / s.no_on_set as sum_scrabe_broken_byset ,
			(q.shift1_scrabe_curve + q.shift2_scrabe_curve  ) / s.no_on_set sum_scrabe_curve_byset ,
			(q.shift1_scrabe_shrinkage + q.shift2_scrabe_shrinkage ) / s.no_on_set as sum_scrabe_shrinkage_byset ,
			(q.shift1_scrabe_dimentions + q.shift1_scrabe_dimentions ) / s.no_on_set as sum_scrabe_dimentions_byset ,
			(q.shift1_scrabe_weight + q.shift1_scrabe_weight ) / s.no_on_set as sum_scrabe_weight_byset ,
			(q.shift1_scrabe_dirty + q.shift2_scrabe_dirty ) / s.no_on_set as sum_scrabe_dirty_byset ,
			(q.shift1_scrabe_cloration + q.shift2_scrabe_cloration ) / s.no_on_set as sum_scrabe_cloration_byset ,

			q.shift1_scrabe_shortage + q.shift1_scrabe_roll + q.shift1_scrabe_broken + q.shift1_scrabe_curve + q.shift1_scrabe_shrinkage + q.shift1_scrabe_dimentions + q.shift1_scrabe_weight + q.shift1_scrabe_dirty + q.shift1_scrabe_cloration as shift1_scrabe_No_parts,
			q.shift2_scrabe_shortage + q.shift2_scrabe_roll + q.shift2_scrabe_broken + q.shift2_scrabe_curve + q.shift2_scrabe_shrinkage + q.shift2_scrabe_dimentions + q.shift2_scrabe_weight + q.shift2_scrabe_dirty + q.shift2_scrabe_cloration as shift2_scrabe_No_parts,
			q.shift1_scrabe_no_parts + q.shift2_scrabe_no_parts as sum_scrabe_no_parts,
			
			q.shift1_scrabe_No_parts / s.no_on_set as shift1_scrabe_no_item,
			q.shift1_scrabe_No_parts / s.no_on_set as shift2_scrabe_no_item,

			shift1_proper_production + shift1_scrabe_no_item as shift1_all_production,
			shift2_proper_production + shift2_scrabe_no_item as shift2_all_production,

			sum_scrabe_no_parts/s.no_on_set as number_scrab_by_item,
			shift1_all_production + shift2_all_production as gross_production,
			q.average_dry_weight,
			q.average_wet_weight,
			q.rat_actually,
			q.rat_validation,
			q.c_t_actually,

			q.actuall_destiny_average,
			q.actuall_tall_mm_average,
			q.actuall_width_mm_average,
			q.id_DayPartUnique,
			q.parts_patchsNumbers,
			q.Items_patchsNumbers,
			q.bachStartDate,
			q.bachEndDate
			from insutech.t10inventory q
			left join v96item_specifications s
			on q.f11part_id=s.id_part
				)'''%veiw_quality_daily
		cursor.execute(calculate_quality_daily)
		conn.commit()
	def install_befor_reports_molds(self):	#for prepair data to get reports as mold list
			create_view_qulaity_inspection_as_molds_list='''/* for collect quality_inspection as yv_parts_items  */
				create view v106quality_inspection_molds as (select 
									q.year, q.month ,q.day ,q.f12molds_id,q.f14machine_id,
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
									
									
									s.density,
									q.date_day
									from v10quality_inpsection q
									left join v96item_specifications s
									on q.f12molds_id=s.f12molds_id
									group by q.year, q.month ,q.day,q.date_day,q.f14machine_id,q.f12molds_id,s.density
									
									order by q.year, q.month  ,q.date_day ,q.f14machine_id)
			'''
			cursor.execute(create_view_qulaity_inspection_as_molds_list)
			conn.commit()
			print("complete  install view befor_reports_molds")		
	
	def install_befor_reports_parts(self):		
			create_view_v107quality_inspection_parts='''/* for collect quality_inspection as parts  */
				create view v107quality_inspection_parts as (select 
									q.year, q.month ,q.date_day ,q.day,q.f12molds_id,q.f11part_id, q.f14machine_id,
		
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
									s.density
									from v10quality_inpsection q
									left join v96item_specifications s
									on q.f11part_id=s.id_part
								
									group by q.year, q.month ,q.day,q.date_day,q.f12molds_id,q.f11part_id,q.f14machine_id,s.density
									
									order by q.year, q.month ,q.date_day ,q.f14machine_id)
			'''
			cursor.execute(create_view_v107quality_inspection_parts)
			conn.commit()		
			print("complete install view befor_reports_parts")		
	def install_befor_reports_item_master(self):		

			create_view_qulaity_inspection_as_items_master='''/* for collect quality_inspection as v108items_master  */
								create view v105quality_inspection_items as (select 
								q.year, q.month ,q.date_day ,q.day,q.f12molds_id ,s.No_on_Set,q.f11part_item_id ,q.f14machine_id,q.factory,
	
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
								
								
								s.density
								from v10quality_inpsection q
								left join v108items_master s
								on q.f11part_item_id=s.item_id
						
								group by q.factory,q.year, q.month ,q.day,q.date_day ,q.f12molds_id,s.No_on_Set,q.f11part_item_id,q.f14machine_id,s.density
								
								order by q.year, q.month ,q.f14machine_id
										
										)'''
			cursor.execute(create_view_qulaity_inspection_as_items_master)
			
			conn.commit()		
			print("complete install view befor_reports_Items")	
	def install_befor_reports_material(self):		

			create_view_qulaity_inspection_as_items_master='''/* for collect material unique used ber day as v104material_daily_used  */
								create view v104material_daily_used as (select year ,month ,day ,date_day ,material ,sum(quantity) ,density 
								
								from insutech.t13material_mixed q
								
								group by year, month ,day,date_day ,density,material
								
								order by year, month , day ,date_day)'''
			cursor.execute(create_view_qulaity_inspection_as_items_master)
			
			conn.commit()		
			print("complete install view befor_reports_Items")	
	
	def install_reports(self):
		create_view_quality_daily='''create view v101molds_report_daily as(select q.date_day,q.day,q.month,q.year,q.f12molds_id,q.f11part_item_id,q.f14machine_id,
								
								p.product_name,p.product_code
								,p.machine_size,p.set,p.no_on_set
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
								p.standard_rate_hour,
								p.c_t_standard_per_second,								
								round(avg(q.rat_actually),0)as rat_actually,
								round(avg(q.c_t_actually),0)as c_t_actually,
								/*scrap record*/									
								
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
								
								
								p.customer_name,p.company_of_customer,p.item_code_customers,p.item_classification_customers,
								date_part('week', q.date_day::date) AS weeksNumbers,
								p.mold_name,m.machine_type,m.scrabe_standard
				from v105quality_inspection_items q
							
							left join v108items_master p
							on q.f11part_item_id=p.item_id
							left join insutech.t14machine m
							on m.id=q.f14machine_id
								group by q.factory,q.year, q.month ,q.day,q.date_day,q.f12molds_id,p.mold_name,
								q.f14machine_id,p.machine_size,m.machine_type,m.scrabe_standard,q.f11part_item_id,p.product_name,p.product_code,
								p.product_name_by_parts,p.product_parts,p.UOM,p.set,p.no_on_set,p.standard_dry_weight
								,p.standard_dry_weight_from,p.standard_dry_weight_to,p.standard_rate_hour
								,p.c_t_standard_per_second,p.customer_name,p.company_of_customer,p.item_code_customers,p.item_classification_customers
								
							order by q.year, q.month,q.day,q.f14machine_id
			)'''
		cursor.execute(create_view_quality_daily)
		create_monthly_report_view='''create view v102molds_report as (select 
							q.year, q.month ,q.f12molds_id,s.mold_name
							,s.c_t_standard_per_second,
							round(avg(q.c_t_actually),0)as c_t_actually,
							round(avg(q.rat_actually),0)as rat_actually,
							
							m.scrabe_standard
							
							
							from v106quality_inspection_molds q
							left join v12molds_list s
							on q.f12molds_id=s.mold_id
						left join insutech.t14machine m
						on m.id=q.f14machine_id
						
							group by q.year, q.month ,m.scrabe_standard,q.f12molds_id,s.mold_name
							,s.c_t_standard_per_second
							
						order by q.year, q.month )'''
		cursor.execute(create_monthly_report_view)
				

		create_item_report_view='''create view v100items_molds_report as (select 
								q.year ,q.month, q.f12molds_id,q.f11part_item_id,p.product_name
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
								,round(avg(q.c_t_actually),0)as c_t_actually,
								m.scrabe_standard,
								p.customer_name,
								p.item_name_customers,
								p.item_code_customers
								from v105quality_inspection_items q
							left join v108items_master p
							on q.f11part_item_id=p.item_id 
							left join insutech.t14machine m
							on m.id=q.f14machine_id
							
								group by q.year,q.month,p.customer_name, q.f12molds_id,q.f11part_item_id,p.product_name,p.item_name_customers,
								p.item_code_customers,p.product_code,p.standard_dry_weight
								,p.standard_dry_weight_from,p.standard_dry_weight_to,p.standard_rate_hour
								,p.c_t_standard_per_second,m.scrabe_standard
								
							order by q.year)'''
		cursor.execute(create_item_report_view)
		conn.commit()
		create_material_daily_view='''create view v103material_product_daily as(select
							q.year, q.month ,q.day,t2.material,q.f11part_item_id,p.Product_name,p.product_code
							,p.standard_dry_weight_from,p.standard_dry_weight_to
							,round(avg(q.average_dry_weight),1)as average_dry_weight,p.standard_rate_hour,
							p.c_t_standard_per_second,
							
							round(avg(q.rat_actually),0)as rat_actually,
							round(avg(q.c_t_actually),0)as c_t_actually,
							
							
							m.scrabe_standard,
						
							
				 			q.density
							
							from v105quality_inspection_items q
							left join v108items_master p
								on q.f11part_item_id=p.item_id
								
				 				left join insutech.t14machine m
								on m.id=q.f14machine_id
							
							left join v104material_daily_used t2
							on q.density = t2.density and q.date_day = t2.date_day
							group by q.year, q.month,q.day,t2.material,m.scrabe_standard,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight_from,p.standard_dry_weight_to
							,p.standard_rate_hour,p.c_t_standard_per_second,q.density	
							order by q.year,q.month,t2.material,p.product_name)'''
		cursor.execute(create_material_daily_view)
		#______________________________________t22records_reports___________________________________________
		#____________________________________________________________________________________________
		
		customercomplaints_view='''create view v103material_product_daily as(select
							q.year, q.month ,q.day,t2.material,q.f11part_item_id,p.Product_name,p.product_code
							,p.standard_dry_weight_from,p.standard_dry_weight_to
							,round(avg(q.average_dry_weight),1)as average_dry_weight,p.standard_rate_hour,
							p.c_t_standard_per_second,
							round(avg(q.rat_actually),0)as rat_actually,
							round(avg(q.c_t_actually),0)as c_t_actually,			
							m.scrabe_standard,
				 			q.density
							
							from v105quality_inspection_items q
							left join v108items_master p
								on q.f11part_item_id=p.item_id
								
				 				left join insutech.t14machine m
								on m.id=q.f14machine_id
							
							left join t22records t2
							on q.density = t2.density and q.date_day = t2.date_day
							group by q.year, q.month,q.day,t2.material,m.scrabe_standard,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight_from,p.standard_dry_weight_to
							,p.standard_rate_hour,p.c_t_standard_per_second,q.density	
							order by q.year,q.month,t2.material,p.product_name)'''
#		cursor.execute(customercomplaints_view)

		suppliers_complaints_view='''create view v103material_product_daily as(select
							q.year, q.month ,q.day,t2.material,q.f11part_item_id,p.Product_name,p.product_code
							,p.standard_dry_weight_from,p.standard_dry_weight_to
							,round(avg(q.average_dry_weight),1)as average_dry_weight,p.standard_rate_hour,
							p.c_t_standard_per_second,
							round(avg(q.rat_actually),0)as rat_actually,
							round(avg(q.c_t_actually),0)as c_t_actually,			
							m.scrabe_standard,
				 			q.density
							
							from v105quality_inspection_items q
							left join v108items_master p
								on q.f11part_item_id=p.item_id
								
				 				left join insutech.t14machine m
								on m.id=q.f14machine_id
							
							left join t22records t2
							on q.density = t2.density and q.date_day = t2.date_day
							group by q.year, q.month,q.day,t2.material,m.scrabe_standard,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight_from,p.standard_dry_weight_to
							,p.standard_rate_hour,p.c_t_standard_per_second,q.density	
							order by q.year,q.month,t2.material,p.product_name)'''
#		cursor.execute(suppliers_complaints_view)
		return_products_view='''create view v103material_product_daily as(select
							q.year, q.month ,q.day,t2.material,q.f11part_item_id,p.Product_name,p.product_code
							,p.standard_dry_weight_from,p.standard_dry_weight_to
							,round(avg(q.average_dry_weight),1)as average_dry_weight,p.standard_rate_hour,
							p.c_t_standard_per_second,
							round(avg(q.rat_actually),0)as rat_actually,
							round(avg(q.c_t_actually),0)as c_t_actually,			
							m.scrabe_standard,
				 			q.density
							
							from v105quality_inspection_items q
							left join v108items_master p
								on q.f11part_item_id=p.item_id
								
				 				left join insutech.t14machine m
								on m.id=q.f14machine_id
							
							left join t22records t2
							on q.density = t2.density and q.date_day = t2.date_day
							group by q.year, q.month,q.day,t2.material,m.scrabe_standard,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight_from,p.standard_dry_weight_to
							,p.standard_rate_hour,p.c_t_standard_per_second,q.density	
							order by q.year,q.month,t2.material,p.product_name)'''
#		cursor.execute(return_products_view)

		customercomplaints_view='''create view v103material_product_daily as(select
							q.year, q.month ,q.day,t2.material,q.f11part_item_id,p.Product_name,p.product_code
							,p.standard_dry_weight_from,p.standard_dry_weight_to
							,round(avg(q.average_dry_weight),1)as average_dry_weight,p.standard_rate_hour,
							p.c_t_standard_per_second,
							round(avg(q.rat_actually),0)as rat_actually,
							round(avg(q.c_t_actually),0)as c_t_actually,			
							m.scrabe_standard,
				 			q.density
							
							from v105quality_inspection_items q
							left join v108items_master p
								on q.f11part_item_id=p.item_id
								
				 				left join insutech.t14machine m
								on m.id=q.f14machine_id
							
							left join t22records t2
							on q.density = t2.density and q.date_day = t2.date_day
							group by q.year, q.month,q.day,t2.material,m.scrabe_standard,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight_from,p.standard_dry_weight_to
							,p.standard_rate_hour,p.c_t_standard_per_second,q.density	
							order by q.year,q.month,t2.material,p.product_name)'''
#		cursor.execute(customercomplaints_view)

		material_inspection_view='''create view v103material_product_daily as(select
							q.year, q.month ,q.day,t2.material,q.f11part_item_id,p.Product_name,p.product_code
							,p.standard_dry_weight_from,p.standard_dry_weight_to
							,round(avg(q.average_dry_weight),1)as average_dry_weight,p.standard_rate_hour,
							p.c_t_standard_per_second,
							round(avg(q.rat_actually),0)as rat_actually,
							round(avg(q.c_t_actually),0)as c_t_actually,			
							m.scrabe_standard,
				 			q.density
							
							from v105quality_inspection_items q
							left join v108items_master p
								on q.f11part_item_id=p.item_id
								
				 				left join insutech.t14machine m
								on m.id=q.f14machine_id
							
							left join t22records t2
							on q.density = t2.density and q.date_day = t2.date_day
							group by q.year, q.month,q.day,t2.material,m.scrabe_standard,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight_from,p.standard_dry_weight_to
							,p.standard_rate_hour,p.c_t_standard_per_second,q.density	
							order by q.year,q.month,t2.material,p.product_name)'''
#		cursor.execute(material_inspection_view)


		conn.commit()
		print("complete install reports")		

	def import_infrastructure(self):	
		print("_______test_________")
		print(self.folder)
		import_t14machine ='''copy insutech.t14machine (id,name,scrabe_standard,machine_type,place ,low_size,high_size,machineStatus)
		FROM '%s\machines.csv' (FORMAT csv, HEADER, DELIMITER ',');'''%self.folder
		
		cursor.execute(import_t14machine)
		
		conn.commit()
		print("import infrastructure data for day")
	def import_masterdata_molds(self):
		import_t12molds_list='''copy insutech.t12molds (
			mold_id ,
			ORG_CODE ,
			ORG_NAME ,
			Ctegory ,
			UOM ,
			machine_size ,
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
						
		cursor.execute(import_t12molds_list)
		conn.commit()
		print("import molds data for day")

	def import_masterdata_parts(self):
		import_ty_parts_list='''
					copy insutech.t11parts (
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
		SQL1="copy insutech.t10inventory (%s)" %SQL_quality_records
		SQL2=SQL1+" FROM '%s\quality_records.csv' (FORMAT csv, HEADER, DELIMITER ',');"%self.folder
		
		cursor.execute(SQL2)

		conn.commit()
	def import_material_records(self):
		SQL1='''copy insutech.t13material_mixed(
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
		SQL1='select * from v100items_molds_report where year = (%s) '%year
		
		SQL2 = SQL1+' and month=(%s);'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	

	def show_yearly_report_itemsByMonths(self,year,month):
			SQL1='select * from v100items_molds_report where year = (%s) '%year
			cursor.execute(SQL1)

	def show_monthly_report_view_month(self,year,month):

		SQL1='''with quary_molds_report as (select 
								q.year, q.month ,
								round(avg(q.average_dry_weight),1)as average_dry_weight,
								round(avg(q.rat_actually),0)as rat_actually,
								round(avg(q.c_t_actually),0)as c_t_actually
								
								
					
				from v105quality_inspection_items q
							
							
							left join v108items_master p
							on q.f11part_item_id=p.item_id
							left join insutech.t14machine m
							on m.id=q.f14machine_id
							
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
									q.year, q.month ,q.f14machine_id,m.scrabe_standard,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually
									
					from v105quality_inspection_items q
								
								left join v108items_master p
								on q.f11part_item_id=p.item_id 
								left join insutech.t14machine m
								on m.id=q.f14machine_id
								
									group by q.year, q.month ,q.f14machine_id,m.scrabe_standard
								order by q.year, q.month ,q.f14machine_id
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
									round(avg(q.c_t_actually),0)as c_t_actually
									
					from v105quality_inspection_items q
								
								
								left join v108items_master p
								on q.f11part_item_id=p.item_id 
								left join insutech.t14machine m
								on m.id=q.f14machine_id
								
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
									round(avg(q.c_t_actually),0)as c_t_actually
									
					from v105quality_inspection_items q
								
								
								left join v108items_master p
								on q.f11part_item_id=p.item_id 
								left join insutech.t14machine m
								on m.id=q.f14machine_id
								
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
									q.year ,q.f14machine_id,m.scrabe_standard,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually
									
					from v105quality_inspection_items q
								
								left join v108items_master p
								on q.f11part_item_id=p.item_id 
								left join insutech.t14machine m
								on m.id=q.f14machine_id
								
									group by q.year ,q.f14machine_id,m.scrabe_standard
								order by q.year ,q.f14machine_id
										)
								select * from quary_molds_report
								where year =(%s);'''%year

		cursor.execute(SQL1,)

	def monthly_report_ncr_weight_low(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year, q.month ,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									
									
									
									m.machine_type,
									round(avg(q.average_dry_weight-p.standard_dry_weight),0)as Weight_deviation,
									round(max(q.average_dry_weight),0)as max_WeightAtmonth,
									round(min(q.average_dry_weight),0)as min_WeightAtMonth,
									round(stddev(q.average_dry_weight),0)as standardWeightDeviationAtMonth
					
						
					from v105quality_inspection_items q
								
								
								left join v108items_master p
								on q.f11part_item_id=p.item_id 
								left join insutech.t14machine m
								on m.id=q.f14machine_id
									group by q.year, q.month ,m.machine_type,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight
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
									q.year, q.month ,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									
									
									
									m.machine_type,
									round(avg(q.average_dry_weight-p.standard_dry_weight),0)as Weight_deviation,
									round(max(q.average_dry_weight),0)as max_WeightAtmonth,
									round(min(q.average_dry_weight),0)as min_WeightAtMonth,
									round(stddev(q.average_dry_weight),0)as standardWeightDeviationAtMonth
												
						
					from v105quality_inspection_items q
								
								
								left join v108items_master p
								on q.f11part_item_id=p.item_id
								left join insutech.t14machine m
								on m.id=q.f14machine_id
									group by q.year, q.month ,m.machine_type,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight
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
		SQL1='''with quary_molds_report as (select q.year, q.month ,q.f12molds_id,p.mold_name,p.standard_rate_hour
									,p.c_t_standard_per_second,
									
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually,
									
									
									m.machine_type ,
									round(avg(q.c_t_actually-p.c_t_standard_per_second),0)as c_t_deviation,
									round(max(q.c_t_actually),0)as max_ctAtmonth,
									round(min(q.c_t_actually),0)as min_ctAtMonth,
									round(stddev(q.c_t_actually),0)as standardCtDeviationAtMonth,
									round(sum(q.gross_production),0)as gross_production,
									round((avg(q.c_t_actually-p.c_t_standard_per_second)*sum(gross_production)/(60*60)),0) as HoursProductionLost,
									round(avg(q.mold_avalibility),2)as mold_avalibility
								from v106quality_inspection_molds q
								
							
								left join v12molds_list p
								on q.f12molds_id=p.mold_id
								left join insutech.t14machine m
								on m.id=q.f14machine_id						
									group by q.year, q.month ,m.machine_type,q.f12molds_id,p.mold_name,p.standard_rate_hour
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
									q.year, q.month ,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,m.scrabe_standard
																		
								from v105quality_inspection_items q
								left join v108items_master p
								on q.f11part_item_id=p.item_id 
								left join insutech.t14machine m
								on m.id=q.f14machine_id
								
									group by q.year, q.month ,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,m.scrabe_standard
									
								order by q.year, q.month 
										)
								select * from quary_molds_report			
								where year =(%s)'''%year
		SQL2 = SQL1+' and month = (%s) and percentage>scrabe_standard'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	# show yearly reports	
	def yearly_report_ncr_weight(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to,
									round(avg(q.average_dry_weight),1)as average_dry_weight,
									
									
									m.machine_type,
									round(avg(q.average_dry_weight-p.standard_dry_weight),0)as Weight_deviation,
									round(max(q.average_dry_weight),0)as max_WeightAtmonth,
									round(min(q.average_dry_weight),0)as min_WeightAtMonth,
									round(stddev(q.average_dry_weight),0)as standardWeightDeviationAtMonth
					from v105quality_inspection_items q
								
								
								left join v108items_master p
								on q.f11part_item_id=p.item_id
								left join insutech.t14machine m
								on m.id=q.f14machine_id
									group by q.year,m.machine_type,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight
									,p.standard_dry_weight_from,p.standard_dry_weight_to
									
								order by q.year
										)
								select * from quary_molds_report
								where year =(%s) and (average_dry_weight>standard_dry_weight_to or average_dry_weight<standard_dry_weight_from)'''%year
		
		cursor.execute(SQL1)
	def yearly_report_ncr_ct(self,year,month):
		SQL1='''with quary_molds_report as (select q.year,q.f12molds_id,p.mold_name,p.standard_rate_hour
									,p.c_t_standard_per_second,
									
									round(avg(q.rat_actually),0)as rat_actually,
									round(avg(q.c_t_actually),0)as c_t_actually,
									
									
									m.machine_type,
									round(avg(q.c_t_actually-p.c_t_standard_per_second),0)as c_t_deviation,
									round(max(q.c_t_actually),0)as max_ctAtmonth,
									round(min(q.c_t_actually),0)as min_ctAtMonth,
									round(stddev(q.c_t_actually),0)as standardCtDeviationAtMonth,
									round(sum(q.gross_production),0)as gross_production,
									round((avg(q.c_t_actually-p.c_t_standard_per_second)*sum(gross_production)/(60*60)),0) as HoursProductionLost,
									round(avg(q.mold_avalibility),2)as mold_avalibility
				
								from v106quality_inspection_molds q
								
							
								left join v12molds_list p
								on q.f12molds_id=p.mold_id
								left join insutech.t14machine m
								on m.id=q.f14machine_id
									group by q.year ,m.machine_type,q.f12molds_id,p.mold_name,p.standard_rate_hour
									,p.c_t_standard_per_second
								order by q.year 
										)
								select * from quary_molds_report
								where year =(%s) and c_t_actually>c_t_standard_per_second*1.05'''%year
		
		
		cursor.execute(SQL1)
	def yearly_report_ncr_scrap(self,year,month):
		SQL1='''with quary_molds_report as (select 
									q.year ,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,m.scrabe_standard,					
									
									round(sum(q.number_scrab_by_item),0)as number_scrab_by_item,
									
									round(sum(q.gross_production),0)as gross_production,
									
									round((sum(q.number_scrab_by_item))/(sum(q.gross_production)),3)as percentage
																		
								from v105quality_inspection_items q
								left join v108items_master p
								on q.f11part_item_id=p.item_id 
								left join insutech.t14machine m
								on m.id=q.f14machine_id
								
									group by q.year ,q.f12molds_id,q.f11part_item_id,p.product_name,p.product_code,m.scrabe_standard
									
								order by q.year
										)
								select * from quary_molds_report			
								where year =(%s) and percentage>scrabe_standard'''%year
		
		cursor.execute(SQL1)
	def get_daily_dataentry_items(self,year,month,*args):
		SQL1='''with quary_molds_report as (select * from v101molds_report_daily 	
									)
							select * from quary_molds_report where year=(%s)'''%year
		
		SQL2 = SQL1+' and month = (%s)'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
#		SQL3 = SQL1+' and mold_id = (%s)'
#		cursor.execute(SQL3, (args, ))
		
	def get_daily_dataentry_items_yearly(self,year):
		SQL1='''with quary_items_report as (select * from v101molds_report_daily
									)
							select * from quary_items_report where year=(%s)'''%year
	
		cursor.execute(SQL1)	
	def yearly_report_molds_byWeeks(self,year,month,day,to_day):
		SQL1='''with quary_items_report_by_week as (select * from v101molds_report_daily
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
									
								/*	round(count(unique(q.f14machine_id)),0)as machines_number, */
									round(min(q.f14machine_id),0)as machines_min_use,
									round(max(q.f14machine_id),0)as machines_max_use						
					from v105quality_inspection_items q
								
								
								left join v108items_master p
								on q.f11part_item_id=p.item_id
								left join insutech.t14machine m
								on m.id=q.f14machine_id
								
									group by q.year, q.month 
									
								order by q.year, q.month
										)
								select * from quary_molds_report
								where year =(%s)'''%year
		cursor.execute(show_machine_report_yearly)
	def items_report_arabic_custom_item(self,year,*args):
		

		SQL1='''select %s '''%sql_quality_reporty_yearly_item
		SQL2=SQL1+''' from v100items_molds_report
		
			where year = (%s) '''%year
	

		SQL3=SQL2+''' group by year ,customer_name,scrabe_standard, f12molds_id,f11part_item_id,product_name
			,product_code,item_name_customers,
			item_code_customers	,standard_dry_weight,standard_dry_weight_from,standard_dry_weight_to,standard_rate_hour,c_t_standard_per_second order by year;
			'''
		
		if type(args) == tuple:   
			cursor.execute(SQL3)
		else:  
			SQL_mold = SQL2+''' and item_id =(%s) group by year ,customer_name,scrabe_standard, mold_id,item_id,product_name,item_name_customers,
								item_code_customers	,product_code,standard_dry_weight,standard_dry_weight_from,standard_dry_weight_to,standard_rate_hour,c_t_standard_per_second order by year;'''
			cursor.execute(SQL_mold, (args, ))


		
	def show_yearly_report_molds(self,year,month,*args):#report depend of mold structure
			SQL1='''select %s '''%sql_quality_reporty_yearly_mold
			SQL2=SQL1+''' from v102molds_report 
			
			 where year = (%s) '''%year
		

			SQL3=SQL2+'''group by year ,scrabe_standard,f12molds_id,mold_name 
			,c_t_standard_per_second 
			order by year
			 '''
			
			if type(args) == tuple:   
				cursor.execute(SQL3)
			else:  
				SQL_mold = SQL2+''' and mold_id =(%s) group by year ,scrabe_standard,f12molds_id,mold_name 
			,c_t_standard_per_second order by year;'''
				cursor.execute(SQL_mold, (args, ))

	def show_mnthly_report_molds(self,year,month):#report depend of mold structure
			#report depend of mold structure
		SQL1='''
							with quary_molds_report as (select * from v102molds_report)
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
							
							with quary_molds_report as(select * from v102molds_report)
										
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
							q.year, q.month ,q.f11part_item_id,p.Product_name,p.product_code
							,p.standard_dry_weight_from,p.standard_dry_weight_to
							,round(avg(q.average_dry_weight),1)as average_dry_weight,p.standard_rate_hour,
							p.c_t_standard_per_second,
							
							round(avg(q.rat_actually),0)as rat_actually,
							round(avg(q.c_t_actually),0)as c_t_actually,
							
							m.scrabe_standard,
	
							q.bachStartDate
							
	
							from insutech.t10inventory q
							left join v108items_master p
							on q.f11part_item_id=p.item_id
						left join insutech.t14machine m
						on m.id=q.f14machine_id
						
							group by q.year, q.month,m.scrabe_standard,q.f11part_item_id,p.product_name,p.product_code,p.standard_dry_weight_from,p.standard_dry_weight_to
							,p.standard_rate_hour,p.c_t_standard_per_second,q.bachStartDate		
							)
							select distinct t1.* ,t2.bachEndDate
							from monthly_baches_report t1
							left join 
								(select year, month ,bachStartDate ,bachEndDate
									from
									insutech.t10inventory q 
									where bachEndDate is not null
									group by year, month ,q.bachstartdate,bachEndDate)t2
							on t1.bachStartDate=t2.bachStartDate
							
							
						where t1.year = (%s) 
							'''%year
		SQL2 = SQL1+' and t1.month =(%s) order by t1.year, t1.month ,t1.bachStartDate DESC;'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)	
		else:
			cursor.execute(SQL2, (month,))	
	
	def returnProducts(self,year,month):#report depend of mold structure
			#report depend of mold structure
		SQL1='''select
							 %s,p.Product_name,p.product_code
							,t127.name
							from v105quality_inspection_items q
							left join v108items_master p
								on q.f11part_item_id=p.item_id
							
							left join insutech.t22records t22
							on q.f22records_id = t22.record_id 
							left join t127means t127
							on t127.means_id=t22.f127means_id
							order by q.year,q.month,p.product_name'''%product_return_column
		
		SQL2 = SQL1+' and month =(%s);'
		
		if type(month) == tuple:   
			cursor.execute(SQL2, month)
		if type(year) == tuple:   
			cursor.execute(SQL1, year)	
		else:
			cursor.execute(SQL1, (year,))	
	
	def show_water_content_daily(self,year,month,day,to_day):#report depend of mold structure
			SQL1='''select %s '''%sql_quality_water_content
			sql2=SQL1+''' from v101molds_report_daily 
			
			 where year = %s  ''' %year 
			sql3=sql2+'''and month =%s 
						group by year ,month,day,f14machine_id,f12molds_id,f11part_item_id,product_code,
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
		SQL1=SQL0+''' from insutech.t13material_mixed q where year = (%s)'''%year
		SQL2=SQL1+'''and month= (%s) '''%month
		SQL3=SQL2+'''and day=(%s) order by date_day,shift,silo_number,material
				 '''%day
		cursor.execute(SQL3)	
	def materialToPorduct_daily(self,year):#report depend of mold structure
			#report depend of mold structure
		SQL1='''select * from v103material_product_daily q
							
							
							where year = (%s)
							order by year , month  , material,product_name'''%year
		
		if type(year) == tuple:   
			cursor.execute(SQL1, year)	
		else:
			cursor.execute(SQL1, (year,))	
	def materialToPorduct(self,year):#report depend of mold structure
			#report depend of mold structure
		SQL1='''with material_product as (select
							year, month ,material,f11part_item_id,Product_name,product_code
							,standard_dry_weight_from,standard_dry_weight_to
							,round(avg(average_dry_weight),1)as average_dry_weight,standard_rate_hour,
							c_t_standard_per_second,
							
							round(avg(rat_actually),0)as rat_actually,
							round(avg(c_t_actually),0)as c_t_actually,
							
				 			density
				
							from v103material_product_daily q
							
							group by year, month,material,scrabe_standard,f11part_item_id,product_name,product_code,standard_dry_weight_from,standard_dry_weight_to
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

def mold_shout_count_weekly(self,year,month,day,to_day):#report depend of mold structure
			SQL1='''select %s '''%sql_quality_water_content
			sql2=SQL1+''' from v101molds_report_daily 
			
			 where year = %s  ''' %year 
			sql3=sql2+'''and month =%s 
						group by year ,month,day,f14machine_id,f12molds_id,f11part_item_id,product_code,
						product_name,standard_dry_weight,standard_dry_weight_from,
						standard_dry_weight_to order by day'''  %month

			if type(month) == tuple:   
				cursor.execute(sql3, month)	
			else:
				cursor.execute(sql3,(month,))

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
			SQL3_row=SQL3_day+'and f11part_item_id=%s;'
			cursor.execute(SQL3_row, (item_id, ))
			record = cursor.fetchone()
			#record = cursor.fetchall()
			print(record)
			
			# Update single record now
			updateSQL1_column = """Update %s """%table
			updateSQL2_table=SQL1_column+'set %s '%column
			updateSQL3_day=SQL2_table+'where year=2020 and month=2 and day =%s '%day
			updateSQL3_row=SQL3_day+'and f11part_item_id=%s;'
			cursor.execute(SQL3_row, (f11part_item_id, ))

			sql_update_query = """Update insutech.t10inventory set where year=2020 and month=2 and day =5 and f11part_item_id=%s"""
			
	def delete_rows(self,table,year,month,*args,monthly=True):
			
		SQL_table=' DELETE from %s '%table
		SQL_year=SQL_table+'where year=%s'%year
		SQL_month=SQL_year+' and month =%s '%month
				
		#SQL3_row=SQL3_day+'and f11part_item_id=%s;
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

class ORM():
	move_table_to_schema=	'''ALTER TABLE yksus1
    			SET SCHEMA firma1;'''