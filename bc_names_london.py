from connection_db import *
import csv

# Need:

# Customers in london which have m and/or n in their name (contact name and name)

# Use a while loop and fetchone()
# Then create csv with relavent data

cursor = docker_northwind_cc.cursor()

rows = cursor.execute("SELECT ContactName, Phone FROM Customers WHERE City LIKE 'London' AND (ContactName LIKE '%m%' "
                      "OR ContactName LIKE '%n%');")

newfile = open("london_mn_names.csv", "w", newline="")

with newfile:

    record = list(rows)
    record.insert(0, ["Customer Name", "Phone Number"])
    csv.writer(newfile, delimiter=",").writerows(record)