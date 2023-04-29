import mysql.connector as connector
import os    
from dotenv import load_dotenv                                               


load_dotenv("pass.env")
passw=os.getenv("pass")

class Db_helper:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',password=passw,database='MySQL_Python_CRUD')
        query = 'create table if not exists user(User_Id int primary key, User_Name varchar(150), Mobile_Number varchar(13))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Table Created Succesfully! ")


    #inserting
    def insert_user(self,userid,username,mobile):
        query = "insert into user(User_Id,User_Name,Mobile_Number) values({},'{}','{}')".format(userid, username, mobile)
        print(query)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Row inserted")

    #Fetching all Data
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0]," User Name :  ",row[1]," Contact : ",row[2])


    #deleting one row
    def delete_user(self, uid):
        query = "delete from user where User_Id = '{}'".format(uid)
        cur_del = self.con.cursor()
        cur_del.execute(query)
        self.con.commit()
        print("Row deleted")


    #updating one row
    def update_user(self, userid,new_name,new_mobile):
        query = "update user set User_Name = '{}', Mobile_Number = '{}' where User_Id = {}".format(new_name,new_mobile,userid)
        cur_upd = self.con.cursor()
        cur_upd.execute(query)
        self.con.commit()
        print("Row updated")

