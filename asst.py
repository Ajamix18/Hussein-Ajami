import pyodbc
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT top 10 * from Person.Person")
row = cursor.fetchone()
fl=open('person.html',"w")
fl.writelines('''<main><!DOCTYPE html>
<html>
<head>
    <title style="font-size:300%;" > Persons </title>
</head>
    <body>
        <table border = "1",<table align="center">
        <caption style="color:red;"> Persons </caption><th>First name</th>,<th>Last name</th>''')
while row:
   fl.write("<tr><td>" + row[4] + "</td><td>" + row[6] + "</tr>")
   row = cursor.fetchone()
fl.writelines('''</table>
    </body>
</html>''')