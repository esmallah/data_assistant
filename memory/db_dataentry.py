from .database_postgrs import connect as conn
					
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
		conn.cursor.execute(drop_yv_items_molds_report)
		conn.commit()	
		print("complete uninistall reports data entry")

	def uninstall_dataentry_views(self):
		#for uninstall records tables
		drop_yt_quality=	'''drop table yt_load_machine''' 
		conn.cursor.execute(drop_yt_quality)
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
		conn.cursor.execute(create_table_quality)
		conn.commit()
		print("complete install machine loaded")
	def install_views_machine_loaded(self):
		create_view_quality='''
				create view yv_load_machine as(select 
				l.date_day ,
				m.name,
				mo.mold_name ,
				l.factory		
				from yt_load_machine l
				left join yt_machine_list m
				on m.id = l.machine_id
				left join Yt_molds_list mo
				on mo.mold_id=l.mold_id
					
				);'''
		conn.cursor.execute(create_view_quality)
		conn.commit()
		print("complete install machine loaded")
	def select_list_items(self):
		select_items='''
				select 
				l.date_day ,
				m.name,
				mo.mold_name ,
				l.factory		
				from yt_load_machine l
				left join yt_machine_list m
				on m.id = l.machine_id
				left join Yt_molds_list mo
				on mo.mold_id=l.mold_id
					
				);'''
		conn.cursor.execute(select_items)
		conn.commit()
		print("complete install machine loaded")
