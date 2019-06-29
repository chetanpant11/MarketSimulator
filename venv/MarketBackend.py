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
        sql = "select * from Customer order by name desc"

        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)

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

    def updatelp(self,abc):

        sql="update customer set lp={} where uid = {}".format(abc.lp,uid)
        cursor.execute(sql)
        con.commit()

    def fetchLp(self):
        lp1 = "select lp from customer where uid='{}'".format(uid)
        cursor.execute(lp1)
        result = cursor.fetchone()
        previousLp = int(result[0])
        return previousLp

    def manipulateLP(self,cost):


        if cost >= 500 and cost < 1000:
            if cRef.lp >=100:
                cost = cost-100
                cRef.lp = cRef.lp-100
                db.updatelp(cRef)
                return cost

            elif cRef.lp<100:
                cost = cost - cRef.lp
                cRef.lp=0
                db.updatelp(cRef)
                return cost


        elif cost >= 1000:
            if cRef.lp >=100:
                cost = cost-100

                cRef.lp = cRef.lp-100 + (0.1*cost)

                db.updatelp(cRef)
                return cost

            elif cRef.lp<100:
                cost = cost - cRef.lp
                cRef.lp = 0  + (0.1*cost)
                db.updatelp(cRef)
                return cost



    def showCost(self,finalcost):
        print("the amount you have to pay after applying lp = ",finalcost)

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

print("1.  Add Customer Details!!!")

print("2. Already a Customer!!!")

print("3. Show all customers")

choice = int(input("Enter your Choice : "))
cost=0
lp1="select lp from customer "
if choice == 1:

    cRef = customer(None, None,None,100,None,1)
    cRef.name = input("Enter name of the customer : ")
    cRef.phone = input("Enter phone of the customer : ")
    cRef.email = input("Enter email of the customer : ")
    cRef.uid = random.randrange(1000,10000)


    save = input("Do you want to save the details of the customer (yes/no): ")
    if save == "yes":

        db = dbHelper()
        db.saveCustomerInDB(cRef)
        print("*****CONGRATULATIONS YOU HAVE BEEN GIVEN 100 Loyalty Points*********")
        print("")
        cRef.showCustomerDetails()
        #loyalty points assign

#=========================================================================================
if choice == 2:
    uid = int(input("Enter your unique Customer id : "))
    db = dbHelper()
    z = db.fetch_Active_Status(uid)

    if z == 1:
        print("1.  Update Customer Details!!")
        print("2. Delete the customer Details")
        print("3. Shopping")

        second_choice = int(input("Enter your Second Choice: "))

        if second_choice == 1:
            db = dbHelper()

            cRef = customer(None, None, None, None, None, None)
            db.fetchCustomer(uid)
            cRef.name = input("Enter name of the customer : ")
            cRef.phone = input("Enter phone of the customer : ")
            cRef.email = input("Enter email of the customer : ")

            save = input("Do you want to update the details (yes/no): ")
            if save == "yes":
                db = dbHelper()
                db.updateCustomerInDB(cRef,uid)

        if second_choice == 2:

            cRef = customer(None, None, None, None, None, None)
            cRef.Active = 0

            save = input("Do you want to Delete the details (yes/no): ")
            if save == "yes":
                db = dbHelper()
                db.deleteCustomerInDB(cRef, uid)

        if second_choice == 3:
            db = dbHelper()
            previousLp=db.fetchLp()
            cRef = customer(None, None, None, previousLp, None, None)
            cost = int(input("Enter cost="))
            final_cost = db.manipulateLP(cost)
            db.showCost(final_cost)
    else:
        print("No customer of the entered uid exists!!!!!!!!")
if choice == 3:
    db = dbHelper()
    db.fetchAllCustomers()
