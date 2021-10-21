import sqlite3
from sqlite3 import Error
 
class Sqlite_db(): 
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connecction object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
    
        return conn
    
    
    def create_table(conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
    
    
    def main():
        database = r".\db.db"
    
        sql_create_table_quality = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """
    
        sql_view_create_quality = """CREATE TABLE IF NOT EXISTS tasks (
                id serial primary key,
                machine_id int,
                mold_id int,
                factory  varchar(50),
                date_day date
                FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""
    

        create_table_quality='''
            create table yt_load_machine (
            );'''
        
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
        
        # create a database connection
        conn = create_connection(database)
    
        # create tables
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_table_quality)
    
            # create tasks table
            create_table(conn, sql_view_create_quality)
        else:
            print("Error! cannot create the database connection.")
    
    
    if __name__ == '__main__':
        main()