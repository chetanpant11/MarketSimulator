import random

import mysql.connector

con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="chetan pant")

cursor = con.cursor()

class dbHelper():
    def saveCustomerInDB(self,customer):

        sql = f"insert into Customer values(null, '{customer.name}', '{customer.phone}', '{customer.email}',{customer.lp},{customer.uid}, {customer.Active})"


        cursor.execute(sql)

        con.commit()

        print("details of customer saved!!!!!!!!")

    def updateCustomerInDB(self, customer, uid):
        sql = f"update Customer set name = '{customer.name}', email = '{customer.email}', phone = '{customer.phone}' where uid = {uid}"

        cursor.execute(sql)

        con.commit()

        print("details of customer UPDATED!!!!!!!!")

    def deleteCustomerInDB(self, customer, uid):
        sql = f"update Customer set Active = '{customer.Active}' where uid = {uid}"

        cursor.execute(sql)

        con.commit()

        print(f"details of customerID {uid} Deleted!!!!!!!!")

    def fetchAllCustomers(self):
        sql = "select * from Customer order by cid asc"

        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    def fetchCustomer(self, uid):
        sql = "select * from Customer where uid = {}".format(uid)

        cursor.execute(sql)

        row = cursor.fetchone()
        print(row)

    def fetch_Active_Status(self, uid):
        sql = "select Active from Customer where uid = {}".format(uid)

        cursor.execute(sql)

        row = cursor.fetchone()
        r1 = int(row[0])
        return r1

    def updatelp(self,customer,uid):

        sql="update customer set lp={} where uid = {}".format(customer.lp,uid)
        cursor.execute(sql)
        con.commit()

    def fetchLp(self,uid):
        lp1 = "select lp from customer where uid='{}'".format(uid)
        cursor.execute(lp1)
        result = cursor.fetchone()
        previousLp = int(result[0])
        return previousLp

    def manipulateLP(self,cRef,cost,uid):

        db = dbHelper()
        if cost >= 500 and cost < 1000:
            if cRef.lp >=100:
                cost = cost-100
                cRef.lp = cRef.lp-100
                db.updatelp(cRef,uid)
                return cost

            elif cRef.lp<100:
                cost = cost - cRef.lp
                cRef.lp=0
                db.updatelp(cRef,uid)
                return cost


        elif cost >= 1000:
            if cRef.lp >=100:
                cost = cost-100

                cRef.lp = cRef.lp-100 + (0.1*cost)

                db.updatelp(cRef,uid)
                return cost

            elif cRef.lp<100:
                cost = cost - cRef.lp
                cRef.lp = 0  + (0.1*cost)
                db.updatelp(cRef,uid)
                return cost



    def showCost(self,finalcost):
        print("the amount you have to pay after applying lp = ",finalcost)

    def convert(self,cost):
        return int(cost)

class customer():
    def __init__(self, name, phone, email, lp,uid, Active):
        self.name = name
        self.phone = phone
        self.email = email
        self.lp = lp
        self.uid = uid
        self.Active = Active

    def showCustomerDetails(self):
        print(f"Name  : {self.name}")
        print(f"Phone : {self.phone}")
        print(f"Email : {self.email}")
        print(f"UID =   {self.uid}")
