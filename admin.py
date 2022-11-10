import mysql.connector
import sys
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
   
    print("8 exit")

   

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
            sys.exit("view data error")
        
    elif(choice==2):

        print('view consumer')
    

    elif(choice==3):

        print('search consumer')
        
    
    elif(choice==4):

        print('update consumer')
        

    elif(choice==5):

            print('delete consumer')
        

    elif(choice==6):
        

        print('Generate bill')

       
    elif(choice==7):
         

        print('view bill')
        try:
            sql="SELECT  `code`, `name`, `address`, `phno`, `email` FROM `consumer`"
            mycursor.execute(sql)
            result=mycursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as e:
            sys.exit("view data error")

    elif(choice == 8):
        break