from connection_db import *

# Fetchall is dangerous when working with very large databases. Using it without thinking can deplete RAM if the
# query has large numbers of rows. This will slow down all servers connected to the database.

# Instead of that, a while loop can be used to fetch one at a time
# Be aware that using public Clouds may pay per fetchone, therefore efficient use of fetching is essential

cursor = docker_northwind_cc.cursor()

rows = cursor.execute("SELECT * FROM Products;")

while True:
    record = rows.fetchone()
    if record is None:
        break
    else:
        print(record.UnitPrice)