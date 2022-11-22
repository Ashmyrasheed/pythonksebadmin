import mysql.connector
import sys
import random
from datetime import date
from tabulate import tabulate
try:
    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'admindb')
    mycursor = mydb.cursor()
except mysql.connector.Error as e:
    sys.exit("data error")
mycursor=mydb.cursor()


while True:

    print("select an option from the menu")

    print("1 add consumer")

    print("2 view all consumer")  

    print("3 search a consumer")

    print("4 update the consumer")    

    print("5 delete a consumer")
    
    print("6 generate bill")
    
    print("7 view bill")
   
    print("8 top 2 high bill")
    
    print("9 exit")
   

    choice = int(input('enter an option:'))

    if(choice==1):

        print('consumer add selected')
        code=input("enter the consumer code")
        name=input("enter the name")
        address=input("enter the address")
        phno=input("enter the ph no")
        email=input("enter the email")
        try:
            sql="INSERT INTO `consumer`(`code`, `name`, `address`, `phno`, `email`) VALUES(%s,%s,%s,%s,%s)"
            data=(code,name,address,phno,email)
            mycursor.execute(sql,data)
            mydb.commit()
            print("values insertred successfully")
        except mysql.connector.Error as e:
            sys.exit("view data errors")
        
    elif(choice==2):
        print('view consumer')
        try:
            sql="SELECT  `code`, `name`, `address`, `phno`, `email` FROM `consumer`"
            mycursor.execute(sql)
            result=mycursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as e:
            sys.exit("view data error")
    

    elif(choice==3):

        print('search consumer selected')

        print("1.search by consumer name")

        print("2.search by consumer code")

        print("3.search by consumer phone number")

        choice1 = int(input('enter an option:'))

        if(choice1==1):

            print("consumer details")

            name=input("enter the name ")

            sql="SELECT `code`, `name`, `address`, `phno`, `email` FROM `consumer` WHERE `name`='"+name+"'"

        elif(choice1==2):

            code=input("enter the consumer code")

            sql="SELECT `code`, `name`, `address`, `phno`, `email` FROM `consumer` WHERE `code` ='"+code+"'"

        elif(choice1==3):

            phno=input("enter the phone number")

            sql="SELECT `code`, `name`, `address`, `phno`, `email` FROM `consumer` WHERE `phno`='"+phno+"'"

        mycursor.execute(sql)

        result=mycursor.fetchall()

        print(result)

        break
             
            
    
    elif(choice==4):

        print('update consumer')
        
        
        code=input("enter the consumer code")
        name=input("enter the name to be updated")
        address=input("enter the address to be updated")
        phno=input("enter the ph no to be updated")
        email=input("enter the email to be updated")
        sql= "UPDATE `consumer` SET `code`='"+code+"',`name`='"+name+"',`address`='"+address+"',`phno`='"+phno+"',`email`='"+email+"'"
        mycursor.execute(sql)

        mydb.commit()

        print('Updated sucessfully !!!')
        

    elif(choice==5):

            print('delete consumer')
            code=input("enter the consumer code")
            sql="DELETE FROM `consumer` WHERE `code`='"+code+"'"
            mycursor.execute(sql)
            mydb.commit()
            print("data deleted succesfully") 
    elif(choice==6):
        print('generate bill selected')
        dates = date.today()
        year = dates.year
        month = dates.month
        sql="DELETE FROM `bill` WHERE `month`='"+str(month)+"' AND `year`= '"+str(year)+"'"
        mycursor.execute(sql)
        mydb.commit()
       
        sql="SELECT `id` FROM `consumer`"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            a=i[0]
            print(a)
          
            sql="SELECT SUM(unit) FROM `usages` WHERE `userid`='"+str(a)+"' AND MONTH(datetime)='"+str(month)+"' AND YEAR(datetime)='"+str(year)+"' "
            mycursor.execute(sql)
            result=mycursor.fetchone()
            unit=(result[0])
            print(result)
            #print(i)
            total_bill=int(str(result[0])) * 5
            print(total_bill)
            #date= datetime.today().strftime('%Y-%m-%d')
            sql="INSERT INTO `bill`(`userid`, `month`, `year`, `bill`, `paid status`, `billdate`, `totalunit`,`duedate`) VALUES (%s,%s,%s,%s,%s,now(),%s,now()+interval 14 day)"
            data = (str(a),str(month),str(year),total_bill,'0',unit)
            mycursor.execute(sql,data)
            mydb.commit()
            print("Bill inserted successfully.")
        
    elif(choice==7):
        print('view bill')
        sql = "SELECT c.name,c.address,b.`userid`, b.`month`, b.`year`, b.`bill`, b.`paidstatus`, b.`billdate`, b.`totalunit` FROM `bill` b JOIN consumer c ON b.userid=c.id "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(tabulate(result,headers=['name','address','user_id','month','year','bill','paidstatus','billdate','totalunit',],tablefmt = "psql"))
    elif(choice==8):

        print('Top 2 high bill')

        sql = "SELECT * FROM `bill` ORDER BY `bill`DESC LIMIT 2"

        mycursor.execute(sql)

        result = mycursor.fetchall()

        print(tabulate(result,headers=['id', 'user_id', 'month', 'year', 'bill', 'paidstatus', 'bill date',  'total_unit']))
        break
    elif(choice==9):
        break
    
    
    