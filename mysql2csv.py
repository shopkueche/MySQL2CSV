import pymysql
import sys
import csv
from datetime import datetime

#Query for SELECT and UPDATE
QUERY='SELECT * FROM test.testp WHERE Export = "N";'
UPDATE_DB = 'UPDATE test.testp SET Export = "Y" WHERE Export = "N";'

# Connection to MySQL
con = pymysql.connect(host = 'localhost', port = 8889,user = 'root',passwd = 'root',db = 'test')

# Execute SELECT and UPDATE only if the SELECT-Result is not empty
cur=con.cursor()
rows_count = cur.execute(QUERY)
if rows_count > 0:
     result = cur.fetchall()
     # Write CSV
     filename = datetime.now().strftime('export-%Y-%m-%d-%H-%M.csv')
     c = csv.writer(open(filename, 'w'))
     for x in result:
         c.writerow(x)

     # Fire UPDATE Query
     cur = con.cursor()
     cur.execute(UPDATE_DB)
     con.commit()
else:
     print("SELECT is empty!")


# Close Connection to MySQL
con.close()