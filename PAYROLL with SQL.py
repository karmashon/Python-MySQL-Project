#Payroll SQL Project #Password/OTP
import time
import random
import mysql.connector
def OTP4():
    n=''
    for i in range(4):
        n+=str(random.randint(0,9))
    return int(n)
def salary():
    mycursor.execute("update Payroll set SALARY=20000 where POSITION='ClerkJNR'")
    mycursor.execute("update Payroll set SALARY=25000 where POSITION='ClerkSNR'")
    mycursor.execute("update Payroll set SALARY=35000 where POSITION='AccountantJNR'")
    mycursor.execute("update Payroll set SALARY=50000 where POSITION='AccountantSNR'")
    mycursor.execute("update Payroll set SALARY=75000 where POSITION='ManagerJNR'")
    mycursor.execute("update Payroll set SALARY=100000 where POSITION='ManagerSNR'")
    mycursor.execute("update Payroll set SALARY=125000 where POSITION='CEO'")

    mycursor.execute("update Payroll set TAX=0 where POSITION='ClerkJNR'")
    mycursor.execute("update Payroll set TAX=SALARY*0.025 where POSITION='ClerkSNR'")
    mycursor.execute("update Payroll set TAX=SALARY*0.05 where POSITION='AccountantJNR'")
    mycursor.execute("update Payroll set TAX=SALARY*0.10 where POSITION='AccountantSNR'")
    mycursor.execute("update Payroll set TAX=SALARY*0.125 where POSITION='ManagerJNR'")
    mycursor.execute("update Payroll set TAX=SALARY*0.15 where POSITION='ManagerSNR'")
    mycursor.execute("update Payroll set TAX=SALARY*0.175 where POSITION='CEO'")

    mycursor.execute("update Payroll set BONUS=(NOOFDAYSWORKED_MONTH-18)*SALARY/30 where NOOFDAYSWORKED_MONTH>18 and NOOFDAYSWORKED_MONTH<=22")
    mycursor.execute("update Payroll set BONUS=0 where NOOFDAYSWORKED_MONTH=18")
    mycursor.execute("update Payroll set DEDUCT=(18-NOOFDAYSWORKED_MONTH)*SALARY/30 where NOOFDAYSWORKED_MONTH<18 and NOOFDAYSWORKED_MONTH>=0")
    mycursor.execute("update Payroll set DEDUCT=0 where NOOFDAYSWORKED_MONTH=18")
    
    mycursor.execute("update Payroll set NETSALARY=SALARY-TAX+BONUS-DEDUCT")
def add():
    print("Type the following as syntax for adding: insert into <Table name> values(<id>,<name>,<age>,<doj>,<position>,<no of days worked in month>,<phno>,<passwd>,<status>,0,0,0,0,0)")                                           
    s=input("==>")
    mycursor.execute(s)
    salary()
    mydb.commit()
    print("Successfully added")
def delete():
    mycursor.execute("delete from Payroll where STATUS='INACTIVE'")
    mydb.commit()
    print("Deleted INACTIVE employees")
def modify():
    status=0
    mycursor.execute("select * from Payroll")
    rec=mycursor.fetchall()
    tempid=int(input("Enter Employee ID To Modify:"))
    for i in range(len(rec)):
        if rec[i][0]==tempid:
            status=1
            tempposition=input("Enter New Position:")
            if tempposition in ["ClerkJNR","ClerkSNR","AccountantJNR","AccountantSNR","ManagerJNR","ManagerSNR","CEO"]:
                print("Type the following as syntax for Modifying: Update <Table Name> set POSITION=<position> where EMPID=<id>")
                s=input("==>")
                mycursor.execute(s)
                salary()
                mydb.commit()
                print("Position modified")
            else:
                print("Position not found")
                break
    if status==0:
        print("EMPID not found")

def archive():
    status=0
    mycursor.execute("select * from Payroll")
    rec=mycursor.fetchall()
    tempid=int(input("Enter Employee ID To Archive:"))
    for i in range(len(rec)):
        if rec[i][0]==tempid:
            status=1
            print("EMPID found")
            print("Type the following as syntax for Archiving: Update <Table Name> set STATUS='INACTIVE' where EMPID=<id>")
            s=input("==>")
            mycursor.execute(s)
            mydb.commit()
            print("Successfully Archived")
            break
    if status==0:
        print("EMPID not found")

def display():
    mycursor.execute("select * from Payroll")
    rec=mycursor.fetchall()
    for i in rec:
        print(i)
                    
mydb=mysql.connector.connect(host='localhost',user='root',passwd='rushilben10',port='3306',database='DAV')
mycursor=mydb.cursor()
AP1=277353
AP2=234231
AP3=871341
print("Admin Level 1 Password:",AP1)
print("Admin Level 2 Password:",AP2)
print("Admin Level 3 Password:",AP3)

#Create table

'''mycursor.execute("drop table Payroll")

mycursor.execute("create table Payroll(EMPID int primary key NOT NULL,EMPNAME char(20),AGE int,DOJ date,POSITION char(20),NOOFDAYSWORKED_MONTH int,PHNO char(20), PASSWORD char(20),STATUS char(20))")

mycursor.execute("insert into Payroll values(1,'a',24,'2019-07-12','ClerkJNR',18,'9566134234','111','ACTIVE')")
mycursor.execute("insert into Payroll values(2,'b',26,'2017-08-13','ClerkSNR',22,'9421447145','222','INACTIVE')")
mycursor.execute("insert into Payroll values(3,'c',27,'2014-07-11','AccountantJNR',19,'9377385710','333','ACTIVE')")
mycursor.execute("insert into Payroll values(4,'d',29,'2013-01-15','AccountantSNR',17,'9942617632','444','ACTIVE')")
mycursor.execute("insert into Payroll values(5,'e',36,'2011-01-18','ManagerJNR',20,'9274235723','555','INACTIVE')")
mycursor.execute("insert into Payroll values(6,'f',39,'2009-09-12','ManagerSNR',16,'9173757385','666','ACTIVE')")
mycursor.execute("insert into Payroll values(7,'g',42,'2009-07-12','CEO',0,'9185363643','777','ACTIVE')")


mycursor.execute("alter table Payroll add SALARY float NOT NULL default 0")
mycursor.execute("alter table Payroll add TAX float NOT NULL default 0")
mycursor.execute("alter table Payroll add BONUS float NOT NULL default 0")
mycursor.execute("alter table Payroll add DEDUCT float NOT NULL default 0")
mycursor.execute("alter table Payroll add NETSALARY float NOT NULL default 0")
salary()
mydb.commit()'''

#Printing all records
display()
print()
print()

#create window
box=Tk()
box.title("Test Box")
l=Label(text='''Welcome to Payroll System''',justify=CENTER,font='Calibri',fg='black')
l.pack()
b2=Button(text="2. Access as User",fg="blue")
b3=Button(text="3. Exit",fg="blue",command=box.quit)
b1.pack()
b2.pack()
b3.pack()



#Access as Admin/User

print('''\tMENU
        1.Access as Admin
        2.Access as User
        3.Exit''')
ch=int(input("Enter choice:"))
if ch==1:
    print("Accessing as Admin. Please Wait")
    for i in range(4):
        print(".",end=' ')
        time.sleep(1)
    ap=int(input("Enter Admin password:"))
    print("Verifying",end=' ')
    for i in range(4):
        print(".",end=' ')
        time.sleep(1)
    if ap==AP1:
        print("Correct Password-Admin Level 1 Access Granted")
        print('''\tMENU
        1.Add Record
        2.Modify Record
        3.Archive Record
        4.Delete Record
        5.Display
        6.Exit''')
        while True:
            ch=int(input("Enter choice:"))
            if ch==1:
                add()
            elif ch==2:
                modify()
            elif ch==3:
                archive()
            elif ch==4:
                delete()
            elif ch==5:
                display()
            elif ch==6:
                print("Exiting",end='')
                for i in range(4):
                    print(".",end='')
                    time.sleep(1)
                print("Exited!")
                break
            else:
                print("Wrong Choice!")
    elif ap==AP2:
        print("Correct Password-Admin Level 2 Access Granted")
        print("""\tMENU
        1.Add Record
        2.Modify Record
        3.Archive Record
        4.Display
        5.Exit""")
        while True:
            ch=int(input("Enter choice: "))
            if ch==1:
                add()
            elif ch==2:
                modify()
            elif ch==3:
                archive()
            elif ch==4:
                display()
            elif ch==5:
                print("Exiting",end=' ')
                for i in range(4):
                    print(".",end=' ')
                    time.sleep(1)
                print("Exited!")
                break
            else:
                print("Wrong choice!")
    
    elif ap==AP3:
        print("Correct Password-Admin Level 3 Access Granted")
        print("""\tMENU
        1.Add Record
        2.Display
        3.Exit""")
        while True:
            ch=int(input("Enter choice: "))
            if ch==1:
                add()
            elif ch==2:
                display()
            elif ch==3:
                print("Exiting",end=' ')
                for i in range(4):
                    print(".",end=' ')
                    time.sleep(1)
                print("Exited!")
                break
            else:
                print("Wrong choice")
    else:
        print("Wrong Password-Access Denied")
        print("Exiting")

elif ch==2:
    print("Accessing as User. Please Wait")
    for i in range(4):
        print(".",end=' ')
        time.sleep(1)
    print("Access Granted")
    x=int(input("Enter employee id to search:"))
    li=[]
    mycursor.execute("select * from Payroll")
    rec=mycursor.fetchall()
    for i in rec:
        li.append(i[0])
    if x in li:
        for i in range(len(rec)):
            if rec[i][0]==x:
                c0=-1
                print("Enter Password OR Forgot Password (press Enter)")
                for j in range(3):
                    p=input("==>")
                    if rec[i][7]==p:
                        c0=1
                        print("Details are:")
                        print("    EMPID:",rec[i][0])
                        print("    EMPNAME:",rec[i][1])
                        print("    AGE:",rec[i][2])
                        print("    DOJ:",rec[i][3])
                        print("    PH NO:",rec[i][6])
                        print("    POSITION:",rec[i][4])
                        print("    NET SALARY:",rec[i][12])
                        print()
                        print("Exiting")
                        break
                    elif p=='':
                        c0=2
                        break
                    else:
                        print("Incorrect Password.",3-i-1,"attempts left")                
                if c0==-1:
                    print("Ran out of attempts. Exiting")
                elif c0==2:
                    c1=-1
                    print('Enter Phone No. of employee which begins like','******'+rec[i][6][6:],'to generate OTP')
                    for j in range(3):
                        pno=input("==>")
                        if pno==rec[i][6]:
                            c1=1
                            break
                        else:
                            print("Incorrect Phone No.",3-j-1,"chances left")
                    if c1==-1:
                        print("Ran out of attempts. Exiting")
                    elif c1==1:
                        otp=OTP4()
                        print("Generated OTP is:",otp)
                        c2=-1
                        for j in range(3):
                            o=input("Enter OTP:")
                            if str(otp)==o:
                                c2=1
                                print("Details are:")
                                print("    EMPID:",rec[i][0])
                                print("    EMPNAME:",rec[i][1])
                                print("    AGE:",rec[i][2])
                                print("    DOJ:",rec[i][3])
                                print("    PH NO:",rec[i][6])
                                print("    POSITION:",rec[i][4])
                                print("    NET SALARY:",rec[i][12])
                                print()
                                print("Exiting")
                                break
                            else:
                                print("Incorrect OTP.",3-j-1,"chances left")
                        if c2==-1:
                            print("Ran out of attempts. Exiting")
    else:
        print("Sorry. EMPID not found.")
elif ch==3:
    print("Exiting",end='')
    for i in range(4):
        print('.',end='')
        time.sleep(1)
    print("Exiting!")
else:
    print("Wrong Choice!")

#After all code
box.mainloop()
            
