import cx_Oracle
try:
    con = cx_Oracle.connect('hr/hr123@localhost')
    cursor = con.cursor()
    sql = "insert into temp_emps values(:eno,:ename,:esal,:eaddr)"
    records = [(200,'sunny',2000,'mumbai'),
               (300,'chinny',3000,'Hyd'),
               (400,'Bunny',4000,'Hyd')]
    cursor.executemany(sql,records)
    con.commit()
    print("records inserted successfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print("there is problem with sql ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
