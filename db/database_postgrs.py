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
import psycopg2
import sys
import os
from .config import config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#connect to share database_______________
#try:
table="yt_quality"

# print the connection string we will use to connect

import psycopg2



conn = None
params = config(filename=BASE_DIR+r'\\db\database.ini', section="postgresql_remote_server")
print ("Connecting to database\n	->%s" % params)
conn = psycopg2.connect(**params)
cursor = conn.cursor()

'''
except psycopg2.DatabaseError, e:
	print ('Error %s' % e)
	sys.exit(1)
finally:
	if conn:
		cursor.close()
		conn.close()
T
'''
#!/usr/bin/python

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()