from MySqlAdvance.mysqlconnection import Connection
import mysql.connector
class CallProcedure():
    def __init__(self):
        super().__init__('localhost','root','pavithra1969','myhcl',3306)
        self.cur=self.connect.cursor()
    def procedure(self):
        sql="create procedure region_data(in reg ;"
        self.cur.callprocedure()