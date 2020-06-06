# MySQL2CSV
Export MySQL query to CSV and fire an Update-Statement

#Query for SELECT and UPDATE

    QUERY='SELECT * FROM test.testp WHERE Export = "N";'
    UPDATE_DB = 'UPDATE test.testp SET Export = "Y" WHERE Export = "N";'
Set your querys for SELECT (and Update if needed)

# Connection to MySQL
    con = pymysql.connect(host = 'localhost', port = 8889,user = 'root',passwd = 'root',db = 'test')
Setup your connection to MySQL-DB
