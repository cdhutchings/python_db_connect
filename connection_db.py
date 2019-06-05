import pyodbc

# Our variables consists of all details required to initiate a connection

server = "localhost,1433"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"

# Creatoing the connection using pyodbc
docker_northwind_cc = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL '
                                'Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)



