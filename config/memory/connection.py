import pyodbc
 
#def write(): 
msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
print(f'MS-Access Drivers : {msa_drivers}')

 
try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\center\database\Q-H.S.E_RB.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")
 

except pyodbc.Error as e:
    print("Error in Connection", e)