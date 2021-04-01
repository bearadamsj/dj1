import pyodbc
server = '10.15.1.199'
database = 'input'
username = 'sa'
password = 'bitzer,.123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT Top(1) * from dbo.[CNC-Status-V1];")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()