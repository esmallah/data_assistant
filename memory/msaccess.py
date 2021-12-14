import win32com.client
import pyodbc
import logging
from pathlib import Path
access_database_location=r"D:\work\contact_group\database\management system.accdb"
pg_port=2345
pg_user="youssri.ahmed"
db_name="Blcok"
password="Aa1234567#"
host="AHMED-ALY"




conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; 'rf'DBQ={access_database_location};')
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

a = win32com.client.Dispatch("Access.Application")
a.OpenCurrentDatabase(access_database_location)

table_list = []

for table_info in cursor.tables(tableType='TABLE'):
    table_list.append(table_info.table_name)

for table in table_list:
    logging.info(f"Exporting: {table}")

    acExport = 1
    acTable = 0
    db_name = Path(access_database_location).stem.lower()

    a.DoCmd.TransferDatabase(acExport, "ODBC Database", "ODBC;DRIVER={PostgreSQL Unicode};"f"DATABASE={db_name};"f"UID={pg_user};"f"PWD={pg_pwd};""SERVER=localhost;"f"PORT={pg_port};", acTable, f"{table}", f"{table.lower()}_export_from_access")

    logging.info(f"Finished Export of Table: {table}")
    logging.info("Creating empty table in EGDB based off of this")