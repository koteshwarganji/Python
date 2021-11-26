import cx_Oracle
try:
    con=cx_Oracle.connect('hr/hr123@localhost')
    cursor = con.cursor()
    cursor.execute("insert into temp_emps values(100,'koti',1000,'hyd')")
    con.commit()
    print("record inserted successfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print("there is a problem with sql ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()