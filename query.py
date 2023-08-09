from myapp.models import attendance_table,employee
import mysql.connector as connector

class queryclass:
    def _init_(self):
        pass
        # self.con = connector.connect(host = 'localhost',
        #                             port = '3306',
        #                             user = 'root',
        #                             password = 'Kishan@123',
        #                             database = 'employee')
        

    def insert_emp_attandace(self,emp_id,Date,Time,Type):
        con = connector.connect(host = 'localhost',
                                    port = '3306',
                                    user = 'root',
                                    password = 'Kishan@123',
                                    database = 'employee1')
        # a = "select id from employee name= '{}'".format(emp_id)
        # print()
        query1 = "insert into attendance_table(emp_id,Date,Time,Type) values( {},'{}' ,'{}','{}')".format(emp_id,Date,Time,Type)
        # query= "insert into attendance_table(emp_id,Date,Time) values('1','28/07/2023' ,'00:50:40')"
        # query = "insert into attendance_table(emp_id,Date,Time) values( {},'{}' ,'{}')".format(a,Date,Time)
        # print(query1)
        cur = con.cursor()
        cur.execute(query1)
        con.commit()
        return query1

# x = queryclass()
# x.insert_emp_attandace('kishan','23/4/2021','2:2:21')