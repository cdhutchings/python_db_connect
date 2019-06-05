from connection_db import *

# Creates a cursor that can execute SQL functions on connected db
cursor = docker_northwind_cc.cursor()

# Executes an SQL query using the cursor. This query is now maintained in "cursor" and can have its elements printed
cursor.execute("SELECT * FROM Customers WHERE fax IS NULL;")

# The cursor exists as a list of entries, each of which is given as a tuple
row = cursor.fetchall()

print("Companies which do not have fax numbers:\n")
for x in row:
    print(f"Company: {x.CompanyName}, Customer: {x.ContactName}, Phone Number: {x.Phone}")
    #print(f"Company - {x.CompanyName}, Fax Number - {x.Fax}, Customer - {x.ContactName}" )