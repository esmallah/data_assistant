from .database_postgrsql import cursor,conn
					
class MoldsQuality():
	'''
		this class for manage data base on sahrenetowrk or cpanel to mold categories in foam industries
	'''		
	def __init__(self,folder,table):
		self.folder=folder
		self.table=table

	def uninstall_dataentry_reports(self):
		#uninstall report first steps to uninistall database structures'''			
		drop_yv_items_molds_report=	'drop view yv_load_machine'
		cursor.execute(drop_yv_items_molds_report)
		conn.commit()	
		print("complete uninistall reports data entry")

	def uninstall_dataentry_views(self):
		#for uninstall records tables
		drop_yt_quality=	'''drop table yt_load_machine''' 
		cursor.execute(drop_yt_quality)
		conn.commit()
		print("complete uninistall quality records for data entry")

	def install_tables_machine_loaded(self):
		create_table_quality='''
			create table yt_load_machine (
			id serial primary key,
			machine_id int,
			mold_id int,
			factory  varchar(50),
			date_day date);'''
		cursor.execute(create_table_quality)
		conn.commit()
		print("complete install machine loaded")
	def install_views_machine_loaded(self):
		create_table_quality='''
				create table yv_load_machine (
				id serial primary key,
				date_day date,

				machine_id int,
				mold_id int,
				factory  varchar(50)				
				from yt_load_machine 
					left join yv_item_specifications s
					on q.mold_id=s.mold_id
				);'''
		cursor.execute(create_table_quality)
		conn.commit()
		print("complete install machine loaded")
