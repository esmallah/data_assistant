#test road map
#un upload dublicate data
#the same value to each value by more one process
'''
for test discovery
batches sheet comprartibe by input_daily sheet 
    if batches > input_daily 
    if batches < input_daily there are error in date of start or 
'''
import unittest

from memory import Block,cursor,DatabaseTables
from apps.analysis import Select
import pandas as pd

class TestAnalyss(unittest.TestCase):
    def test_database_postgrsql(esult,asureResult):
        #self.assertAlmostEqual(cuboid_volume(2),8)
        
        assertAlmostEqual(result==asureResult,"number of scrap not equal between baches and mold daily report")
        
#get data from baches
class Apply_testAnalysis():
    
    def __init__(self,year,month):
        #self.folder=folder
        self.year=year
        self.month=month
    def get_columns_names(self,*table):
        #with psycopg2.connect(DSN) as connection:
         #   with connection.cursor() as cursor:
          #      cursor.execute("select column_name from information_schema.columns where table_schema = 'Block' and table_name='YOUR_TABLE_NAME'")
           #     column_names = [row[0] for row in cursor]
        # declare an empty list for the column names
        #columns = []

        DatabaseTables.head_show_monthly_Baches(self)
        rows = cursor.fetchall()
        print ("\n test_____:", rows)

        columns= [rows[0] for row in rows]

        # print list of tuples with column names
        print ("\n col_names_____:", columns)

        # iterate list of tuples and grab first element
        #for tup in rows:

            # append the col name string to the list
         #   columns += [ tup[0] ]

        # close the cursor object to prevent memory leaks
#
#         cursor.close()

#        except Exception as err:
     #       print ("get_columns_names ERROR:", err)

        # return the list of column names
        return columns

    # if the connection to PostgreSQL is valid

        # pass a PostgreSQL string for the table name to the function
        
    def test_analysis_scrap(self):
        """for get data from baches function"""
        
        columns_name=self.get_columns_names()
        Block.head_show_monthly_Baches(self)
        rows = cursor.fetchall()
        #column_names = ["number_scrab_by_item"]
        
        #for creating dataframe
        collect_lists=[] #step one create lists
        #column_headers = [[td.getText() for td in rows[i].findAll(['number_scrab_by_item'])] for i in range(len(rows))]
        
        show_monthly_Baches=pd.DataFrame(rows,columns=[columns_name]) #step 2 create dataframe
        
        print("show_monthly_Baches.head()", show_monthly_Baches.head() )

        #https://stackoverflow.com/questions/40855030/assertionerror-22-columns-passed-passed-data-had-21-columns
        
        # Connect to the database
        # Execute the "SELECT *" query
        #df = postgresql_to_dataframe(conn, "select * from MonthlyTemp", column_names)
        
        print("show_monthly_Baches",  show_monthly_Baches[10] )

        scrap_form_baches=sum(show_monthly_Baches.number_scrab_by_item)
    
        """for get data from baches function"""
        Block.show_monthly_Baches(self,self.year,self.month)
        rows = cursor.fetchall()
        print("____rows___>",rows[5])

        #for creating dataframe
        collect_lists=[] #step one create lists
#        show_monthly_input=pd.DataFrame(rows,columns='number_scrab_by_item') #step 2 create dataframe
        show_monthly_input=pd.DataFrame(rows,columns=['number_scrab_by_item']) #step 2 create dataframe
        
        
        print(show_monthly_input['number_scrab_by_item'][5] )
        scrap_from_input=sum(show_monthly_input['number_scrab_by_item'])
        
        print("test_analysis_input",scrap_from_input)
        print("test_analysis_batches",scrap_form_baches)
        assert scrap_from_input == scrap_form_baches , "number of scrap not equal between baches and mold daily report"