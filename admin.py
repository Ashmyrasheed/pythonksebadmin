import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'admindb')
mycursor = mydb.cursor()


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

        print('consumer enter selected')
        
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

    elif(choice == 8):
        break