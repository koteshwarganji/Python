import cx_Oracle
try:
    con = cx_Oracle.connect('hr/hr123@localhost')
    cursor = con.cursor()
    cursor.execute("create table temp_emps(eno number,ename varchar2(10),esal number(10,2),eaddr varchar2(10))")
    print("table created successfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print("there is a problem with sql ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()