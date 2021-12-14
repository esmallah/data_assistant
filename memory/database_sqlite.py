#for collect data from excel sheet then send it to database
#!/usr/bin/env python
"""This file is part of the leader analysis system

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = 'youssri Ahmed Hamdy <estratigy@yahoo.com>'
__copyright__ = 'Copyright (c) 2021'
__version__ = '0.0.1'


#!/usr/bin/python
import sys, sqlite3
from sqlite3 import Error
from .config import config
from setting import BASE_DIR

#connect to share database_______________
#try:
table="yt_quality"

# print the connection string we will use to connect


#class Database(): 
conn = None
#try:
    # read connection parameters

#params = config(filename=BASE_DIR+'\y_data_assistant\memory\database.ini', section='postgresql_network_server')

# get a connection, if a connect cannot be made an exception will be raised here
#print ("Connecting to database\n	->%s" % params)
conn = sqlite3.connect('insutech.db')


# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
    #print('PostgreSQL database version:')
    #cursor.execute('SELECT version()')

    # display the PostgreSQL database server version
    #db_version = cursor.fetchone()
    #print(db_version)
    
# close the communication with the PostgreSQL
#    cursor.close()

#except (Exception, psycopg2.DatabaseError) as error:
#        print(error)
#finally:
#    if conn is not None:
#        conn.close()
#        print('Database connection closed.')

