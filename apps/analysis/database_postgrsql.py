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

#try:

	#connect to share database_______________
#try:
pc__server="host='localhost' dbname='Block' user='postgres' password='admin'"#connect to data base form my device
network_server="host='AHMED-RASHAD' dbname='Block' user='youssri.ahmed' password='Aa1234567#'"
network_server_test="host='AHMED-RASHAD' dbname='Block_test' user='youssri.ahmed' password='Aa1234567#'"
remote_server="host='185.65.207.126'  dbname='aeraeg_insutech' user='aeraeg_postgres'	password='qhserp12345#' "
conn_string = network_server
table="yt_quality"

# print the connection string we will use to connect
print ("Connecting to database\n	->%s" % (conn_string))


# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()

#if (conn):
#	psss
#else:
	#conn_string = pc__server
	#	cursor.close()
	#	conn.close
