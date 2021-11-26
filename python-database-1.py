#connecting pyhton and database
#importing database specific module
import cx_Oracle
#establishing connection
con = cx_Oracle.connect('hr/hr123@localhost')
print(con.version)
con.close()