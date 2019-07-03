from tkinter import *
from tkinter import messagebox
from MarketBackend import *
import random
import mysql.connector
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="chetan pant")
cursor = con.cursor()

db=dbHelper()


window=Tk()
window.geometry("1200x600")
window.resizable(0,0)
pic1=PhotoImage(file="C:\\Users\\CHETAN PANT\\Desktop\\G3.png")
pic11 = pic1
pic2=PhotoImage(file="C:\\Users\\CHETAN PANT\\Desktop\\G3.png")
pic22 = pic2

def newCustomer():
    def popup(s,s1):
        messagebox.showinfo(s,s1)

    def add():
        cRef = customer(None, None, None, 100, None, 1)
        cRef.name = e1.get()
        cRef.phone = e2.get()
        cRef.email = e3.get()
        cRef.uid = random.randrange(1000, 10000)

        if len(e1.get())==0:
            messagebox.showerror("Error","Name left Empty")


        elif len(e2.get())==0:
            messagebox.showerror("Error","Phone left Empty")


        elif len(e3.get())==0:
            messagebox.showerror("Error","Email left Empty")

        else:
            win1.destroy()
            db.saveCustomerInDB(cRef)
            popup("ADDED", F"YOUR UID={cRef.uid}")
            win1.destroy




    win1=Toplevel(window)
    c=Canvas(win1,bg='red',width=900,height=400)

    background=Label(win1,image=pic11)
    background.place(x=0,y=0,relwidth=1,relheight=1)
    l1 = Label(win1, text="C", fg="white",bg="black",font=("ARIAL",20)).place(x=200, y=20)
    l1 = Label(win1, text="U", bg="white", fg="black", font=("ARIAL", 20)).place(x=230, y=20)
    l1 = Label(win1, text="S", fg="white", bg="black", font=("ARIAL", 25)).place(x=260, y=20)
    l1 = Label(win1, text="T", bg="white", fg="black", font=("ARIAL", 20)).place(x=290, y=20)
    l1 = Label(win1, text="O", fg="white", bg="black", font=("ARIAL", 25)).place(x=310, y=20)
    l1 = Label(win1, text="M", bg="white", fg="black", font=("ARIAL", 20)).place(x=340, y=20)
    l1 = Label(win1, text="E", fg="white", bg="black", font=("ARIAL", 25)).place(x=370, y=20)
    l1 = Label(win1, text="R", bg="white", fg="black", font=("ARIAL", 20)).place(x=400, y=20)
    l1 = Label(win1, text="D", fg="white", bg="black", font=("ARIAL", 25)).place(x=460, y=20)
    l1 = Label(win1, text="E", bg="white", fg="black", font=("ARIAL", 20)).place(x=490, y=20)
    l1 = Label(win1, text="T", fg="white", bg="black", font=("ARIAL", 25)).place(x=520, y=20)
    l1 = Label(win1, text="A", bg="white", fg="black", font=("ARIAL", 20)).place(x=550, y=20)
    l1 = Label(win1, text="I", fg="white", bg="black", font=("ARIAL", 25)).place(x=580, y=20)
    l1 = Label(win1, text="L", bg="white", fg="black", font=("ARIAL", 20)).place(x=610, y=20)
    l1 = Label(win1, text="S", fg="white", bg="black", font=("ARIAL", 25)).place(x=640, y=20)
    l1=Label(win1,text="NAME",bg="black",fg="white",font=("ARIAL",15)).place(x=220,y=110)
    e1=Entry(win1,width=50)
    e1.place(x=350,y=120)
    l1=Label(win1,text="PHONE",bg="black",fg="white",font=("ARIAL",15)).place(x=220,y=165)
    e2=Entry(win1,width=50)
    e2.place(x=350,y=170)
    l1=Label(win1,text="EMAIL",bg="black",fg="white",font=("ARIAL",15)).place(x=220,y=220)
    e3=Entry(win1,width=50)
    e3.place(x=350,y=220)
    b1 =Button(win1, text="ADD", bd=0, bg="black", fg="white", width="30", height=2,command=add).place(x=350,y=300)
    exit = Button(win1, text="EXIT", bd=0, bg="black", fg="white", width="30", height=2, command=win1.destroy).place(x=350, y=340)
    c.pack()



def existingCustomer():

    def checkActive():
        cRef = customer(None, None, None, None, None, None)

        uid = e1.get()
        z = db.fetch_Active_Status(uid)
        if z == 1:
            def updateCustomer():

                def popup(s, s1):
                    messagebox.showinfo(s, s1)

                def add():
                    cRef = customer(None, None, None, 100, None, 1)
                    cRef.name = e1.get()
                    cRef.phone = e2.get()
                    cRef.email = e3.get()
                    cRef.uid = random.randrange(1000, 10000)

                    if len(e1.get()) == 0:
                        messagebox.showerror("Error", "Name left Empty")
                        win4.destroy

                    elif len(e2.get()) == 0:
                        messagebox.showerror("Error", "Phone left Empty")
                        win4.destroy

                    elif len(e3.get()) == 0:
                        messagebox.showerror("Error", "Email left Empty")
                        win4.destroy
                    else:
                        db.updateCustomerInDB(cRef, uid)
                        popup("UPDATED", "YOUR DETAILS GET UPDATED")
                        win4.destroy

                win4 = Toplevel(window)
                win3.destroy()
                c = Canvas(win4, bg='red', width=900, height=400)

                background = Label(win4, image=pic11)
                background.place(x=0, y=0, relwidth=1, relheight=1)
                l1 = Label(win4, text="C", fg="white", bg="black", font=("ARIAL", 20)).place(x=200, y=20)
                l1 = Label(win4, text="U", bg="white", fg="black", font=("ARIAL", 20)).place(x=230, y=20)
                l1 = Label(win4, text="S", fg="white", bg="black", font=("ARIAL", 25)).place(x=260, y=20)
                l1 = Label(win4, text="T", bg="white", fg="black", font=("ARIAL", 20)).place(x=290, y=20)
                l1 = Label(win4, text="O", fg="white", bg="black", font=("ARIAL", 25)).place(x=310, y=20)
                l1 = Label(win4, text="M", bg="white", fg="black", font=("ARIAL", 20)).place(x=340, y=20)
                l1 = Label(win4, text="E", fg="white", bg="black", font=("ARIAL", 25)).place(x=370, y=20)
                l1 = Label(win4, text="R", bg="white", fg="black", font=("ARIAL", 20)).place(x=400, y=20)
                l1 = Label(win4, text="D", fg="white", bg="black", font=("ARIAL", 25)).place(x=460, y=20)
                l1 = Label(win4, text="E", bg="white", fg="black", font=("ARIAL", 20)).place(x=490, y=20)
                l1 = Label(win4, text="T", fg="white", bg="black", font=("ARIAL", 25)).place(x=520, y=20)
                l1 = Label(win4, text="A", bg="white", fg="black", font=("ARIAL", 20)).place(x=550, y=20)
                l1 = Label(win4, text="I", fg="white", bg="black", font=("ARIAL", 25)).place(x=580, y=20)
                l1 = Label(win4, text="L", bg="white", fg="black", font=("ARIAL", 20)).place(x=610, y=20)
                l1 = Label(win4, text="S", fg="white", bg="black", font=("ARIAL", 25)).place(x=640, y=20)
                l1 = Label(win4, text="NAME", bg="black", fg="white", font=("ARIAL", 15)).place(x=220, y=110)
                e1 = Entry(win4, width=50)
                e1.place(x=350, y=120)
                l1 = Label(win4, text="PHONE", bg="black", fg="white", font=("ARIAL", 15)).place(x=220, y=165)
                e2 = Entry(win4, width=50)
                e2.place(x=350, y=170)
                l1 = Label(win4, text="EMAIL", bg="black", fg="white", font=("ARIAL", 15)).place(x=220, y=220)
                e3 = Entry(win4, width=50)
                e3.place(x=350, y=220)
                b1 = Button(win4, text="UPDATE", bd=0, bg="black", fg="white", width="30", height=2, command=add).place(
                    x=350, y=300)
                exit = Button(win4, text="EXIT", bd=0, bg="black", fg="white", width="30", height=2,
                              command=win4.destroy).place(x=350, y=340)
                c.pack()

            def deleteCustomer():
                def popup(s, s1):
                    messagebox.showinfo(s, s1)

                db.deleteCustomerInDB(cRef, uid)

                popup("DELETED", "YOUR CUSTOMER HAS BEEN DELETED")
                win3.destroy

            def shopping():

                win5 = Toplevel(window)
                win3.destroy()
                c = Canvas(win5, bg='red', width=900, height=400)
                def popup(s, s1):
                    messagebox.showinfo(s, s1)
                db = dbHelper()
                lt = Label(win5, text="ENTER THE AMOUNT OF SHOPPING CUSTOMER DID", fg="white", bg="black",
                           font=(20)).place(x=330, y=150)
                e1 = Entry(win5, width=100)
                e1.place(x=330, y=100)

                previousLp = db.fetchLp(uid)
                cRef = customer(None, None, None, previousLp, None, None)

                def abc():

                    cost = int(e5.get())
                    cost1=db.manipulateLP(cRef, cost, uid)
                    popup("SHOPPING","YOU HAVE TO PAY \u20b9{}".format(cost1))
                    win5.destroy

                background = Label(win5, image=pic11)
                background.place(x=0, y=0, relwidth=1, relheight=1)
                lt = Label(win5, text="ENTER THE AMOUNT OF SHOPPING ", fg="white", bg="black", font=("ARIAL", 20)).place(x=250,y=80)
                e5 = Entry(win5, width=50)
                e5.place(x=300, y=190)
                b1 = Button(win5, text="ENTER", bd=0, bg="black", fg="white", width="30", height=2, command=abc).place(x=350,y=270)

                exit = Button(win5, text="EXIT", bd=0, bg="black", fg="white", width="30", height=2,command=win5.destroy).place(x=350, y=330)
                c.pack()




            win3 = Toplevel(window)
            win2.destroy()
            c = Canvas(win3, bg='red', width=900, height=400)

            background = Label(win3, image=pic11)
            background.place(x=0, y=0, relwidth=1, relheight=1)
            l1 = Label(win3, text="WHAT DO YOU WANT TO CHOOSE", fg="white", bg="black", font=("ARIAL", 20)).place(x=260, y=20)
            b = Button(win3, text="Update Customer Details", bg="sky blue", bd=0, width=50, height=2, fg="black",command=updateCustomer).place(x=300, y=120)
            b2 = Button(win3, text="Delete the customer Details", bg="sky blue", bd=0, width=50, height=2, fg="black",command=deleteCustomer).place(x=300, y=180)
            b3 = Button(win3, text="Shopping", bg="sky blue", bd=0, width=50, height=2, fg="black",command= shopping ).place(x=300, y=240)
            exit = Button(win3, text="EXIT", bd=0, bg="black", fg="white", width="30", height=2,command=win3.destroy).place(x=350, y=330)
            c.pack()

        elif z==0:
            def popup(s, s1):
                messagebox.showinfo(s, s1)
            popup("SORRY", "NO CUSTOMER EXIST")

        else:
            def popup(s, s1):
                messagebox.showinfo(s, s1)
            popup("SORRY", "Wrong UID .... Plzz Enter The correct UID")

    win2 = Toplevel(window)
    c = Canvas(win2, bg='red', width=900, height=400)

    background = Label(win2, image=pic11)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    l1 = Label(win2, text="E", fg="white", bg="black", font=("ARIAL", 20)).place(x=200, y=60)
    l1 = Label(win2, text="N", bg="white", fg="black", font=("ARIAL", 20)).place(x=230, y=60)
    l1 = Label(win2, text="T", fg="white", bg="black", font=("ARIAL", 25)).place(x=260, y=60)
    l1 = Label(win2, text="E", bg="white", fg="black", font=("ARIAL", 20)).place(x=290, y=60)
    l1 = Label(win2, text="R", fg="white", bg="black", font=("ARIAL", 25)).place(x=310, y=60)
    l1 = Label(win2, text="C", bg="white", fg="black", font=("ARIAL", 20)).place(x=350, y=60)
    l1 = Label(win2, text="U", fg="white", bg="black", font=("ARIAL", 25)).place(x=380, y=60)
    l1 = Label(win2, text="S", bg="white", fg="black", font=("ARIAL", 20)).place(x=410, y=60)
    l1 = Label(win2, text="T", fg="white", bg="black", font=("ARIAL", 25)).place(x=440, y=60)
    l1 = Label(win2, text="O", bg="white", fg="black", font=("ARIAL", 20)).place(x=470, y=60)
    l1 = Label(win2, text="M", fg="white", bg="black", font=("ARIAL", 25)).place(x=500, y=60)
    l1 = Label(win2, text="E", bg="white", fg="black", font=("ARIAL", 20)).place(x=530, y=60)
    l1 = Label(win2, text="R", fg="white", bg="black", font=("ARIAL", 25)).place(x=560, y=60)
    l1 = Label(win2, text="I", bg="white", fg="black", font=("ARIAL", 20)).place(x=610, y=60)
    l1 = Label(win2, text="D", fg="white", bg="black", font=("ARIAL", 25)).place(x=640, y=60)


    e1 = Entry(win2, width=50)
    e1.place(x=290, y=200)

    B2 = Button(win2, text="CONTINUE", bd=0, bg="black", fg="white", width="30", height=2, command=checkActive).place(x=350, y=270)

    exit = Button(win2, text="EXIT", bd=0, bg="black", fg="white", width="30", height=2, command=win2.destroy).place(x=350, y=330)
    c.pack()


def showAll():
    win1=Toplevel(window)
    win1.geometry("900x600")
    c=Canvas(win1,bg='red',width=900,height=400)
    background = Label(win1, image=pic11)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    l1 = Label(win1, text="C", fg="white", bg="black", font=("ARIAL", 20)).place(x=200, y=20)
    l1 = Label(win1, text="U", bg="white", fg="black", font=("ARIAL", 20)).place(x=230, y=20)
    l1 = Label(win1, text="S", fg="white", bg="black", font=("ARIAL", 25)).place(x=260, y=20)
    l1 = Label(win1, text="T", bg="white", fg="black", font=("ARIAL", 20)).place(x=290, y=20)
    l1 = Label(win1, text="O", fg="white", bg="black", font=("ARIAL", 25)).place(x=310, y=20)
    l1 = Label(win1, text="M", bg="white", fg="black", font=("ARIAL", 20)).place(x=340, y=20)
    l1 = Label(win1, text="E", fg="white", bg="black", font=("ARIAL", 25)).place(x=370, y=20)
    l1 = Label(win1, text="R", bg="white", fg="black", font=("ARIAL", 20)).place(x=400, y=20)
    l1 = Label(win1, text="D", fg="white", bg="black", font=("ARIAL", 25)).place(x=460, y=20)
    l1 = Label(win1, text="E", bg="white", fg="black", font=("ARIAL", 20)).place(x=490, y=20)
    l1 = Label(win1, text="T", fg="white", bg="black", font=("ARIAL", 25)).place(x=520, y=20)
    l1 = Label(win1, text="A", bg="white", fg="black", font=("ARIAL", 20)).place(x=550, y=20)
    l1 = Label(win1, text="I", fg="white", bg="black", font=("ARIAL", 25)).place(x=580, y=20)
    l1 = Label(win1, text="L", bg="white", fg="black", font=("ARIAL", 20)).place(x=610, y=20)
    l1 = Label(win1, text="S", fg="white", bg="black", font=("ARIAL", 25)).place(x=640, y=20)
    l1 = Label(win1, text="CID", fg="white", bg="dark green", font=("ARIAL", 15)).place(x=0, y=120)
    l1 = Label(win1, text="Name", fg="white", bg="dark green", font=("ARIAL", 15)).place(x=50, y=120)
    l1 = Label(win1, text="Phone", fg="white", bg="dark green", font=("ARIAL", 15)).place(x=120, y=120)
    l1 = Label(win1, text="Email", fg="white", bg="dark green", font=("ARIAL", 15)).place(x=250, y=120)
    l1 = Label(win1, text="LP", fg="white", bg="dark green", font=("ARIAL", 15)).place(x=360, y=120)
    l1 = Label(win1, text="UID", fg="white", bg="dark green", font=("ARIAL", 15)).place(x=400, y=120)
    l1 = Label(win1, text="Active", fg="white", bg="dark green", font=("ARIAL", 15)).place(x=440, y=120)

    a = db.fetchAllCustomers()
    s=0
    z=160
    for a1 in a:
        l1 = Label(win1, text=a1, fg="white",bg="black", font=("ARIAL", 13)).place(x=s, y=z)
        z=z+40
    c.pack()

pic=PhotoImage(file="C:\\Users\\CHETAN PANT\\Desktop\\G3.png")
background=Label(window,image=pic1)
background.place(x=0,y=0,relwidth=1,relheight=1)




lab=Label(window,text="M",bg="black",fg="white",font=("ARIAL",35)).place(x=390,y=50)
lab=Label(window,text="A",font=("ARIAL",30)).place(x=440,y=45)
lab=Label(window,text="R",bg="black",fg="white",font=("ARIAL",35)).place(x=480,y=50)
lab=Label(window,text="K",font=("ARIAL",30)).place(x=520,y=45)
lab=Label(window,text="E",bg="black",fg="white",font=("ARIAL",35)).place(x=560,y=50)
lab=Label(window,text="T",font=("ARIAL",30)).place(x=600,y=45)
lab=Label(window,text="A",bg="black",fg="white",font=("ARIAL",35)).place(x=665,y=45)
lab=Label(window,text="P",font=("ARIAL",30)).place(x=705,y=50)
lab=Label(window,text="P",bg="black",fg="white",font=("ARIAL",35)).place(x=745,y=45)
b=Button(window,text="NEW CUSTOMER",bg="sky blue",bd=0,width=50,height=2,fg="black",command=newCustomer).place(x=420,y=240)
b=Button(window,text="EXISTING CUSTOMER",bg="sky blue",bd=0,width=50,height=2,fg="black",command=existingCustomer).place(x=420,y=300)
b=Button(window,text="SHOW ALL CUSTOMERS",bg="sky blue",bd=0,width=50,height=2,fg="black",command=showAll).place(x=420,y=360)

exit=Button(window,text="EXIT",bd=0,bg="black",fg="white",width="30",height=2,command=window.destroy).place(x=500,y=500)
window.mainloop()
