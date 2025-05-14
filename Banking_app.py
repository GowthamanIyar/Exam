#======================First using time in this Application Admin Must Be Change His Password & His details Go throw Customer Details Help For This Application Works Correct Way=================
Entering_User_ID=10000 #Admin ID(Bank Managenment login) & Admin Can Not change His Admin ID
#Because I defined He is As 1st Customer & New Customer IDs are incresing like New_Customer_ID=Admin_ID+1
#If Bank want other kind of int Number   Bank Want to say to SoftWare Engineer & He will Change what they want starting to Admin ID Number
#If they want other kind of str Number(int number with Letter or letters or ect...)  SoftWare Engineer want to add some codeing this Platform
#Because I Write this Code For only int Type of ID Numbers
Entering_User_password='8170126Gk' #Admin Password  & Admin can Change This password 
# Admin's Customer Log Password=35666960Gk It is for Admin's ATM Usage. This can change in Customer Log in -> Change Password
#Admin's Customer Log ID & Admin's Bank Managenment login ID are Same  
Balance=50000
Entering_User_Activity_No=00
Amount=00                                       #global variable
Customer=[]
User=[]
Activity=[]

import datetime as dt           #Time input for even every Transaction when were Done

Customers={10000:{'No':00,'ID':10000,'name':'admin','age':21,'address':'address','NIC_No':'NIC_No','Contact_No':123456789}}
Dic_Customer_Details=Customers[Entering_User_ID]                             #Dic customers --> import recoded data list 
List_Customer_Details=list(Dic_Customer_Details.values())

Customers_activities={10000:{00:{'No':00,"Time":00,'deposit':00,'withdraw':00,'balance':00}}}
Dic_Customer_activities=Customers_activities[Entering_User_ID]
Next_Activity_No=len(Dic_Customer_activities)
Dic_Customer_activity=Dic_Customer_activities[00]
list_Customer_activity=list(Dic_Customer_activities.values())                   #Dic Customers_activities --> import recoded data list

Users={10000:{'NO':00,'ID':10000,'password':'35666960Gk','password_1':'8170126Gk'}}
Dic_User=Users[Entering_User_ID]
List_User=list(Dic_User.values())

def Choice_1():    
    while True:
        try:
            print("====================================================================")
            print("1.Main Menu \t2.Exit \n")
            Choice_1=int(input("Please Enter Your New Choice: ",))
            if Choice_1==1:                                                #Ask to Customer; are you going do another service or exit
                Main_Menu()
            elif Choice_1==2:
                print("\nThank For Using Our Service. \nPlease take Your Card!!!")
                print("====================================================================")
                Options()
            else:
                print("\nEnter the Correct Number For Your New Choice!!!")
        except ValueError:
            print("\nPlease Enter Number Only For Your New Choice!!!")

def Main_Menu():    
    while True:
        try:
            print("====================================================================")
            print("1.Deposit Money \t\t2.Withdraw Money \n3.Check Balance \t\t4.Transaction History") 
            print("5.Change Password \t\t6.Transfer Amount \n7.Exit \n")       
            Choice=int(input("Enter Your Choice: ",))
            if Choice==1:
                Customer_Deposit()
                Choice_1()
            elif Choice==2:
                User_2nd_time()
                Customer_withdraw()
                Choice_1()                
            elif Choice==3:
                print("====================================================================")
                Balance_check()
                print("Your Available Balance is:Rs ",Balance)        
                Choice_1()
            elif Choice==4:
                print("====================================================================")
                print("Your Transactions Are blow Here!\n")
                Transactions_History()
                Choice_1()
            elif Choice==5:                                                           #to show howmany services are have for customer
                User_2nd_time()                                                       #those are what
                Change_Password()                                                     #ask to customer which service you want
                Choice_1()
            elif Choice==6:
                User_2nd_time()
                Transfer_Amount()
                Choice_1()
            elif Choice==7:
                print("====================================================================")
                print("Thank For Using Our Service. \nPlease take Your Card!!!")
                print("====================================================================")
                Options()
            else:
                print("\nPlease Enter the Correct Number For Your Choice!!!") 
        except ValueError:
            print("\nPlease Enter Number Only For Your Choice!!!")
            
def User_2nd_time():
    while True:
        try:
            print("====================================================================")            
            User_1=int(input("Please Enter Your User ID Again: ",))
            User_1passcode=input("Please Enter Your Password Again: ",)
            if User_1==Entering_User_ID and User_1passcode==Entering_User_password:
                print("\nRe_Entry Successful!")
                break                                                       #for the safty purposes customer re_login
            else:                                                           #it is important for withdraw & transfer
                print("\nYour User ID or Password is Incorrect!!!")    
                print("Please Enter the Correct User ID and Password!!!")
                print("Thank For Using Our Service. \nPlease take Your Card!!!\n")
                print("====================================================================")
                print("====================================================================")
            Options()
        except ValueError:
            print("\nPlease Enter Number Only For User ID!!!")

def User():
    global Entering_User_ID
    global Entering_User_password 
    while True:
        try:
            print("====================================================================")
            User_1_ID=int(input("\nEnter Your User ID: ",))
            User_1passcode=input("Enter Your Password: ",)
            for key,value in Customers.items():
                if User_1_ID==key:
                    Dic_of_User_1= Users[key]                                          #ustomer Login
                    User_1Password=Dic_of_User_1.get('password')
                    if User_1Password==User_1passcode:
                        Entering_User_ID=User_1_ID
                        Entering_User_password=User_1passcode
                        print("\nlog in is sucessfull!")
                        break                                          
            else:
                print("\nYour User ID or Password is Incorrect!!!")    
                print("Please Enter the Correct User ID and Password!!!")
                print("Thank For Using Our Service. \nPlease take Your Card!!!")
                print("====================================================================")
                print("====================================================================")
                Options()
            Main_Menu()
        except ValueError:
            print("\nPlease Enter Number Only For User ID!!!")
 
def Entry_of_withdraw():
    global Customers_activities
    Dict_of_current_Customer=Customers_activities.get(Entering_User_ID)
    Next_Activity_No=len(Dict_of_current_Customer)
    on_time=dt.datetime.now()                                          
    Current_time=on_time.strftime("%A, %Y-%b-%d   %I:%M:%S%p.")
    New_Activity={Next_Activity_No:{'No':Next_Activity_No,"Time":Current_time,'deposit':00,'withdraw':00,'balance':00}}
    Dic_New_Activity=New_Activity.get(Next_Activity_No) 
    Dic_New_Activity['withdraw']=Amount
    Dic_New_Activity['balance']=Balance

    Dict_of_current_Customer.update(New_Activity)
    List_Customer_activity=list(Dic_New_Activity.values())    
    file=open(f"Customer_{Entering_User_ID}_activities.txt","a")
    file.writelines(f'{List_Customer_activity}\n')
    file.close()

def Entry_of_deposit():
    global Customers_activities
    Dict_of_current_Customer=Customers_activities.get(Entering_User_ID)
    Next_Activity_No=len(Dict_of_current_Customer)
    New_Activity={Next_Activity_No:{'No':Next_Activity_No,"Time":00,'deposit':00,'withdraw':00,'balance':00}}
    Dic_New_Activity=New_Activity.get(Next_Activity_No)    
    Dic_New_Activity['deposit']=Amount
    Dic_New_Activity['balance']=Balance
    if Balance<50000:
        print("\nWarning: Balance below Rs. 5000!")
    on_time=dt.datetime.now()                                          
    Current_time=on_time.strftime("%A, %Y-%b-%d   %I:%M:%S%p.")
    Dic_New_Activity["Time"]=Current_time
    Dict_of_current_Customer.update(New_Activity)
    List_Customer_activity=list(Dic_New_Activity.values())    
    file=open(f"Customer_{Entering_User_ID}_activities.txt","a")
    file.writelines(f'{List_Customer_activity}\n')
    file.close()

def Customer_withdraw():
    global Balance
    global Amount
    while True:
        try:
            Balance_check()
            print("====================================================================")
            print("We didn't give coins,10,20,50Rs.")
            print("So, Please Enter the withdraw money should be as a multiple of 100Rs.")
            print("Eg:SriLankan Rs.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.\n")      #Customers Withdraw purposes     
            Amount_1=int(input("Enter Your Withdraw Amount: ",))
            if Amount_1>0:
                if Balance-505>=Amount_1:    #Bank min balance is 500
                    if Amount_1%100==0:     #Like a ATM withdraw 
                        Balance-=Amount_1+5  # 5Rs for Servise Charge
                        Amount=Amount_1
                        Entry_of_withdraw()
                        print("\nPlease take Your Money: ",Amount_1)                              
                        print("Your New Balance is: ",Balance)
                        break
                    else:
                        print("Your Avaiable Balance is:",Balance-505)
                        print("\nWe didn't give coins,10,20,50Rs.")
                        print("So, Please Enter the withdraw money should be as a multiple of 100Rs.")
                        print("Eg:SriLankan Rs.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.")                   
                    break
                else:
                    print("\nYou Have not Inof Money. \nYour Balance is: ",Balance)
                    print("Your Avaiable Balance is: ",Balance-500)
                break
            else:
                print("Your Withdraw Amount Mustbe A Positive Number")
            break
        except ValueError:
            print("\nPlease Enter Number Only For Withdraw Amount!!!\nIf you want to left from this withdraw option")
            print("Please Enter the withdraw Amount is: 99")

def Customer_Deposit():
    global Amount
    global Balance
    while True:
        try:
            Balance_check()
            print("====================================================================")
            print("We didn't take coins,10,20,50RS.")                                         #customer's deposit
            print("So, Please put your money should be as a multiple of 100Rs.")
            print("Eg:Srilankan RS.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.\n")       
            Amount_1=int(input("(Put Your Money in Hole)Enter Your Deposit Amount: ",))
            if Amount_1>0:
                if Amount_1%100==0:  #like a ATM deposit
                    Balance+=Amount_1-5 # 5Rs for Servise Charge
                    Amount=Amount_1
                    Entry_of_deposit()
                    print("\nYour Deposit Amount is: ",Amount_1)                                        
                    print("Your New Balance is: ",Balance)
                    break
                else:
                    print("\nPlease take your deposit Money!!!\n\nYour Input is None Approved Money or Damaged Money")
                    print("We didn't take coins,10,20,50RS.")
                    print("So, Please put your money should be as a multiple of 100Rs.")
                    print("Eg:Srilankan RS.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.")
                break
            else:
                print("\nPlease Enter Positive Value For Deposit Amount!!!\n\nPlease take your deposit Money!!!")
                print("Your Input is None Approved Money or Damaged Money\nWe didn't take coins,10,20,50RS.") 
                print("So, Please put your money should be as a multiple of 100Rs.")
                print("Eg:Srilankan RS.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.")               
            break
        except ValueError:
            print("\nPlease Enter Number Only For Deposit Amount!!!\n\nPlease take your deposit Money!!!")
            print("Your Input is None Approved Money or Damaged Money\nWe didn't take coins,10,20,50RS.")
            print("So, Please put your money should be as a multiple of 100Rs.")
            print("Eg:Srilankan RS.100,200,300,...,900,1000,1100,1200,....2000,2100,...,3000,ect.")
        break

def Add_Customer():
    global Customers
    global Users
    global Customers_activities
    global Entering_User_ID
    List_of_Customer_Keys=list(Customers.keys())
    Last_User_ID=List_of_Customer_Keys[-1]
    ID = Last_User_ID +1
    Entering_User_ID=ID
    print("====================================================================")
    name=input("Enter the Customer Name: ",)
    age=input("Enter the Customer Age: ",)        
    address=input("Enter the Customer Address: ",)                           #create new accound for new customer 
    NIC_No=input("Enter the Customer NIC Number: ",)                         #only avaiable for admin 
    Contact_No=input("Enter the Customer Mobile Number:",) 
    on_time=dt.datetime.now()                                          
    Current_time=on_time.strftime("%A, %Y-%b-%d   %I:%M:%S%p.")            
    password=str(len(Customers)+11)+age
    New_Customer={ID:{'No':len(Customers),'ID':ID,'name':name,'age':age,'address':address,'NIC_No':NIC_No,'Contact_No':Contact_No}} 
    New_User={ID:{'No':len(Customers),'ID':ID,'password':password}}
    New_Customers_activities={ID:{00:{'No':00,"Time":Current_time,'deposit':00,'withdraw':00,'balance':00}}}
    print(f"\n{name},Your User ID is: ",ID)
    print(f"{name},Your password is:",password)
    Customers.update(New_Customer)
    Users.update(New_User)
    Customers_activities.update(New_Customers_activities)
    print(f"\n{New_Customer}")
    print("\n",New_User)
    print("\n",New_Customers_activities)
    Add_Customer_Detail()
    Add_User() 
    Add_Activity()   
    print("====================================================================")

def Admin_options():
    global Balance
    global Entering_User_ID
    while True:
        try:
            print("====================================================================")
            print("1.Create Account \t\t2.Deposit Money \n3.Withdraw Money \t\t4.Check Balance")
            print("5.Transaction History \t\t6.Edit Customer Details \n7.Change Customer Password \t8.Change Admin Password")
            print("9.Total Number of Customers \t\t10.Customer Account List \n11.customers_without_accounts \t\t12.Exit\n")
            Choice=int(input("Enter Your Choice: ",))
            if Choice==1:
                Admin_Using_time()
                Add_Customer()
                Choice_2()
            elif Choice==2:
                Admin_Using_time()
                Search_User()
                Choice_3()                                            #show to admin what are the service are you can handle
                Deposit()                
            elif Choice==3:
                Admin_Using_time()
                Search_User()
                Choice_3()
                withdraw()
            elif Choice==4:
                Admin_Using_time()
                Search_User()
                Choice_3()
                print("====================================================================")
                Balance_check()
                print("Your Available Balance is:Rs ",Balance)        
            elif Choice==5:
                Admin_Using_time()
                Search_User()
                Choice_3()
                print("====================================================================")
                print("Your Transactions Are blow Here!\n")
                Transactions_History()
            elif Choice==6:
                Admin_Using_time()
                Search_User()
                Choice_3()
                Edit_Customer()
            elif Choice==7:
                Admin_Using_time()
                Search_User()
                Choice_3()
                Change_Customer_Password()
            elif Choice==8:
                Admin_Using_time()
                Change_Admin_Password()
            elif Choice==9:
                Admin_Using_time()
                Total_Users=len(Users)
                Customer_Count=0 
                for key,value in Users.items():
                    User_Details=Users.get(key)
                    PASSWORD=User_Details.get('password_1','It is Not Defined') 
                    if PASSWORD=='It is Not Defined':
                        Customers_Count+=1
                print=("Total Customers: ",Customer_Count)
            elif Choice==10:
                Admin_Using_time()
                try:
                    print("====================================================================")                        
                    Customer_ID=int(input("Please Enter the Customer ID: ",))
                    for key,value in Customers.items():
                        if Customer_ID==key:
                            True                               
                    else:
                        print("\nUser ID is not Defined!!!") 
                except ValueError:
                    print("\nPlease Enter Number Only For the Customer ID!!!")
                for key,value in Users.items():
                    User_Details=Users.get(key)
                    PASSWORD=User_Details.get('password_1','It is Not Defined') 
                    if PASSWORD=='It is Not Defined':
                        Entering_User_ID=key
                        Balance_check()
                        print(f"Account {key}: ",Balance)
            elif Choice==11:
                try:
                    print("====================================================================")                        
                    Customer_ID=int(input("Please Enter the Customer ID: ",))
                    for key,value in Customers.items():
                        if Customer_ID==key:
                            True                               
                    else:
                        print("\nUser ID is not Defined!!!") 
                except ValueError:
                    print("\nPlease Enter Number Only For the Customer ID!!!")
                for key,value in Users.items():
                    User_Details=Users.get(key)
                    PASSWORD=User_Details.get('password_1','It is Not Defined') 
                    if PASSWORD=='It is Not Defined':
                        Dic_Customer=Customers.get(key)
                        Customer_Name=Dic_Customer.get('name')
                        print(f"{key} and {Customer_Name}")
            elif Choice==12:
                print("\nWe want to increase Our Valuable Customers Count.")
                Options()
            else:
                print("\nPlease Enter the Correct Number For Your Choice!!!") 
        except ValueError:
            print("\nPlease Enter Number Only For Your Choice!!!")

def Choice_2():
    while True:
        try:
            print("====================================================================")
            print("1.Add_Customer \t\t\t2.Exit \n")
            Choice_2=int(input("Please Enter Your New Choice: ",))
            if Choice_2==1:
                Admin_Using_time()
                Add_Customer()                      #to quick access to entering new costomers with create accound
            elif Choice_2==2:
                print("\nWe want to increase Our Valuable Customers Count.")               
                Admin_options()
            else:
                print("\nEnter the Correct Number For Your New Choice!!!")
        except ValueError:
            print("\nPlease Enter Number Only For Your New Choice!!!")

def Admin_Using_time():
    global Entering_User_ID
    while True:
        try:
            print("====================================================================")
            User_1=int(input("Enter Your User ID: ",))
            User_1passcode=input("Enter Your Password: ",)
            List_of_Customer_Keys=list(Customers.keys())
            Admin_ID=List_of_Customer_Keys[0]           
            if User_1==Admin_ID :
                Admin_dict =Users.get(Admin_ID)
                Admin_password=Admin_dict.get('password_1')                   
                if User_1passcode==Admin_password: 
                    Entering_User_ID=Admin_ID              
                    print("\nlog in is sucessfull!")                  #Admin Login
                    break 
                else:
                    print("\nYour Password is Incorrect!!!")    
                    print("Please Enter the Correct Password!!!")
                Admin_options()
            else:
                print("\nYour User ID is Incorrect!!!")    
                print("Please Enter the Correct User ID and Password!!!")
            Admin_options()
        except ValueError:
            print("\nPlease Enter Number Only For User ID!!!")

def Balance_check():
    global Balance
    Dict_of_current_user_activities=Customers_activities.get(Entering_User_ID)       #current time using customer's check bank balance
    Last_Activity_No=len(Dict_of_current_user_activities)-1
    Last_Activity=Dict_of_current_user_activities.get(Last_Activity_No)
    Current_user_balance=Last_Activity.get('balance')
    Balance=Current_user_balance

def Options():    
    while True:
        try:
            print("====================================================================")
            print("1.Customer login \t2.Bank Managenment login \n")
            Choice_1=int(input("Enter Your Choice: ",))
            if Choice_1==1:
                User()                                                                  #first page of who is going to use Admin or Customer
            elif Choice_1==2:
                Admin_options()
            else:
                print("\nEnter the Correct Number For Your Choice!!!")
        except ValueError:
            print("\nPlease Enter Number Only For Your Choice!!!")

def Change_Password():
    global Users
    global Entering_User_password
    print("====================================================================")
    Dict_of_current_Customer=Users.get(Entering_User_ID)
    New_Password=input("Enter Your New Password: ",)
    NewPassword=input("Please Enter Your New Password Again: ",)
    if New_Password==NewPassword:
        print("\nYour Password Change SuccessFul!")                #change password for Customer to change themself
        Dict_of_current_Customer['password']=New_Password
        Update_Change_Password()
        Entering_User_password=New_Password
    else:
        print("\nYour Entering Passwords are not Match.\nSo,Your Password is Not Change.\nPlease Try Again")

def Search_User():
    global Entering_User_ID
    try:
        print("====================================================================")                        
        Customer_ID=int(input("Please Enter the Customer ID: ",))
        for key,value in Customers.items():
            if Customer_ID==key:
                Entering_User_ID=key
                Dic_of_User_1=value                             #Admin usage to identfy the customer
                print("\n",value) 
                break                              
        else:
            print("\nUser ID is not Defined!!!") 
            Admin_options()
    except ValueError:
        print("\nPlease Enter Number Only For the Customer ID!!!")

def Edit_Customer():
    global Customers
    print("====================================================================")
    name=input("Enter the Customer Name: ",)
    age=input("Enter the Customer Age: ",)        
    address=input("Enter the Customer Address: ",)                       #to change if had any typing error when created accound 
    NIC_No=input("Enter the Customer NIC Number: ",)
    Contact_No=input("Enter the Customer Mobile Number:",)             
    Edit_Customer={'ID':Entering_User_ID,'name':name,'age':age,'address':address,
                    'NIC_No':NIC_No,'Contact_No':Contact_No}        
    Customers[Entering_User_ID]=Edit_Customer
    print(f"\n{name},Your User ID is: ",Entering_User_ID)
    print(f"\n{Edit_Customer}")
    Update_Change_Customer_Details()
    print("====================================================================")

def Choice_3():
    while True:
        try:
            print("====================================================================")
            print("1.Continue \t2.Exit \n")
            Choice_3=int(input("Please Enter Your New Choice: ",))
            if Choice_3==1:      
                print("Customer is Verified")
                break
            elif Choice_3==2:                                                    #Admin using time if Customer & customer id not match as the time stop purpose
                print("\nWe want to increase Our Valuable Customers Count.")               
                Admin_options()
            else:
                print("\nEnter the Correct Number For Your New Choice!!!")
        except ValueError:
            print("\nPlease Enter Number Only For Your New Choice!!!")

def Change_Customer_Password():
    global Users
    print("====================================================================")
    Dict_of_current_Customer=Users.get(Entering_User_ID)
    New_Password=input("Enter Your New Password :",)
    NewPassword=input("Please Enter Your New Password Again :",)
    if New_Password==NewPassword:                                   #when Customer forgot there passwprs
        Dict_of_current_Customer['password']=New_Password
        print("\nYour Password Change SuccessFul!")
        print("\nCustomer New Password is: ",New_Password)
        Update_Change_Password()
    else:
        print("\nYour Entering Passwords are not Match.\nSo,Your Password is Not Change.\nPlease Try Again")

def Change_Admin_Password():
    global Users
    print("====================================================================")
    Dict_of_Admin=Users.get(Entering_User_ID)
    New_Password=input("Enter Your New Password: ",)
    NewPassword=input("Please Enter Your New Password Again: ",)
    if New_Password==NewPassword:
        Dict_of_Admin['password_1']=New_Password
        print("\nYour Password Change SuccessFul!")                #Admin Change there own password
        Update_Change_Password()
        
    else:
        print("\nYour Entering Passwords are not Match.\nSo,Your Password is Not Change.\nPlease Try Again")

def withdraw():
    global Amount
    global Balance
    while True:        
        try:
            Balance_check()
            print("====================================================================")           
            Amount_1=int(input("Enter the Customer's Needed Amount: ",))
            if Amount_1>0:
                if Balance-500>=Amount_1:    #Bank min balance is 500
                    Balance-=Amount_1+5 # 5Rs for Servise Charge
                    Amount=Amount_1
                    Entry_of_withdraw()
                    print("\nPlease take the Money: ",Amount_1)
                    print("Customer New Balance is: ",Balance)
                    break                                                     #in side of  the bank customers withdraw with Admin Help
                else:
                    print("\nYou Have not Inof Money. \nYour Balance is: ",Balance)
                    print("Your Avaiable Balance is: ",Balance-500)
                break
            else:
                print("Your Withdraw Amount Mustbe A Positive Number")
            break
        except ValueError:
            print("\nPlease Enter Number Only For Customer's Needed Amount!!!")
        break

def Deposit():
    global Balance
    global Amount
    while True:
        try:
            Balance_check()
            print("====================================================================")
            Amount_1=int(input("Enter the Deposit Amount: ",))
            if Amount_1>0:
                Balance+=Amount_1-5 # 5Rs for Servise Charge
                Amount=Amount_1
                Entry_of_deposit()
                print("\nDeposit Amount is: ",Amount_1)           #in side of the bank deposit for Customer With Admin Help
                print("New Balance is: ",Balance)
                break
            else:
                print("\nPlease Enter Positive Value only For Deposit Amount!!!")                
            break
        except ValueError:
            print("\nPlease Enter Number Only For Deposit Amount!!!")
        break

def Transactions_History():
    Dict_of_current_Customer=Customers_activities.get(Entering_User_ID)
    for key,value in Dict_of_current_Customer.items(): 
        print("\n",value)

def Transfer_Amount():
    global Balance
    global Customers_activities
    global Amount
    while True:
        try:
            Balance_check()
            print("====================================================================")           
            Amount_1=int(input("Enter Your Transfer Amount: ",))
            if Balance-505>=Amount_1:            #Bank min balance is 500
                True                   
                try: 
                    Customer_ID=int(input("\nEnter the Customer ID: ",))
                    Customer1_ID=int(input("Please Enter the Customer ID Again: ",))
                    if Customer_ID==Customer1_ID:
                        for key,value in Customers.items():
                            if key==Customer_ID:                                      #for Customer tranfsfer there cash to another accound
                                Dic_of_Customer=value
                                Name_of_Customer=Dic_of_Customer.get('name')
                                while True:
                                    try:
                                        print("====================================================================")
                                        print("Customer Name is: ",Name_of_Customer)                                    
                                        print("\nif this Name is correct please enter to continue")
                                        print("if this Name is incorrect please enter to Exit For left from Transfer Amount Option")
                                        print("1.Continue \t2.Exit \n")
                                        Choice_1=int(input("Enter Your New Choice: ",))
                                        if Choice_1==1:
                                            Balance-=Amount_1+5 # 5Rs for Servise Charge
                                            Amount=Amount_1
                                            Entry_of_withdraw()

                                            Dict_of_Getting_Customer=Customers_activities.get(Customer1_ID)
                                            Next_Activity_No=len(Dict_of_Getting_Customer)
                                            New_Activity={Next_Activity_No:{'No':Next_Activity_No,"Time":00,'deposit':00,'withdraw':00,'balance':00}}
                                            Dic_New_Activity=New_Activity.get(Next_Activity_No)
                                            on_time=dt.datetime.now()                                          
                                            Current_time=on_time.strftime("%A, %Y-%b-%d   %I:%M:%S%p.")
                                            Dic_New_Activity["Time"]=Current_time
                                            Dic_New_Activity['deposit']=Amount_1
                                            Privous_Activity=Dict_of_Getting_Customer.get(Next_Activity_No-1)
                                            Balance_1=Privous_Activity.get('balance')                                                                                           
                                            Balance_1+=Amount_1
                                            Dic_New_Activity['balance']=Balance_1
                                            Dict_of_Getting_Customer.update(New_Activity)                                
                                            List_Customer_activity=list(Dic_New_Activity.values())    
                                            file=open(f"Customer_{Customer1_ID}_activities.txt","a")
                                            file.writelines(f'{List_Customer_activity}\n')
                                            file.close()
                                            print("\nYour Transfer Amount is: ",Amount_1)
                                            print("Your New Balance is: ",Balance) 
                                            break                                                
                                        elif Choice_1==2:
                                            True
                                            break
                                        else:
                                            print("\nEnter the Correct Number for Your New Choice!!!")
                                    except ValueError:
                                        print("\nPlease Enter Number Only for Your New Choice!!!") 
                                break
                        else:
                            print("\nCustomer ID is not Found!!!")
                        break
                    else:
                        print("\nYour Entering Customer User IDs are Not Match") 
                    break     
                except ValueError:
                    print("\nPlease Enter Number Only for Customer ID!!!") 
            else:
                print("\nYou Have not Inof Money. \nYour Balance is: ",Balance)
                print("Your Avaiable Balance is: ",Balance-500)
            break
        except ValueError:
            print("\nPlease Enter Number Only for Transfer Amount!!!")
        break

def Add_Customer_Detail():
    Dic_Customer_Details=Customers[Entering_User_ID]                             #Dic customers --> import recoded data list 
    List_Customer_Details=list(Dic_Customer_Details.values())    
    file=open("Customers_Details.txt","a")
    file.writelines(f'{List_Customer_Details}\n')
    file.close()

def Add_User():
    Dic_User=Users[Entering_User_ID]
    List_User=list(Dic_User.values())
    file=open("Users_Details.txt","a")
    file.writelines(f'{List_User}\n')
    file.close()

def Add_Activity():
    Dic_Customer_activities=Customers_activities[Entering_User_ID]
    Dic_Customer_activity=Dic_Customer_activities[00]
    List_Customer_activity=list(Dic_Customer_activity.values())    
    file=open(f"Customer_{Entering_User_ID}_activities.txt","a")
    file.writelines(f'{List_Customer_activity}\n')
    file.close()

def Update_Customers():
    global Customers
    global Customer
    try:
        with open("Customers_Details.txt","r")as file:
            for line in file:               
                file.readline()
                return Customer
                No=Customer[0]
                ID=Customer[1]
                name=Customer[2]
                age=Customer[3]
                address=Customer[-3]
                NIC_No=Customer[-1]
                Contact_No=Customer[-1]
                New_Customer={ID:{'No':No,'ID':ID,'name':name,'age':age,'address':address,'NIC_No':NIC_No,'Contact_No':Contact_No}} 
                Customers.update(New_Customer)
                Customer.clear()
    except FileNotFoundError:
        print("Update Customers File is Not Found")        

def Update_Users():
    global Users
    global User
    try:        
        file=open("Users_Details.txt","r")        
        for line in file:
            file.readline()
            return User
            ID=User[1]
            No=User[0]
            password=User[2]
            New_User={ID:{'No':No,'ID':ID,'password':password}}
            Users.update(New_User)
            user.clear()
        file.close()
    except FileNotFoundError:
        print("Update User File is Not Found")

def Update_Activity():
    global Customers
    global Customers_activities
    global Activity
    while True:
        try:
            i=0
            with open(f"Customer_{Entering_User_ID+i}_activities.txt","r")as file:                    
                for line in file:
                    file.readline()
                    return Activity
                    ID=Entering_User_ID+i
                    No=Activity[0]
                    Current_time=Activity[1]
                    deposit=Activity[2]
                    withdraw=Activity[-2]
                    balance=Activity[-1]
                    New_Customer_activities={ID:{No:{'No':No,"Time":Current_time,'deposit':deposit,'withdraw':withdraw,'balance':balance}}}
                    Customers_activities.update(New_Customer_activities)
                    Activity.clear()
                i+=1
        except FileNotFoundError:
            print("Update Activity File is Not Found")
        break

def Update_Change_Password():
    global Users
    Dict_of_current_Customer=Users.get(Entering_User_ID)
    List_Users=list(Users.keys())
    Index_current_Customer=List_Users.index(Entering_User_ID)
    List_User_Values=list(Dict_of_current_Customer.values())
    try:
        if Index_current_Customer>0:
            with open("Users_Details.txt","r+")as file:
                file.readlines(Index_current_Customer)
                file.writelines(f'\n{List_User_Values}')
        else:
            with open("Users_Details.txt","w")as file:
                file.writelines(f'{List_User_Values}')
    except FileNotFoundError:
        print("Update Change password Details File is Not Found")

def Update_Change_Customer_Details():
    global Customers
    try:        
        Dict_of_current_Customer=Customers.get(Entering_User_ID)
        List_Customers=list(Customers.keys())
        Index_current_Customer=List_Customers.index(Entering_User_ID)
        List_User_Values=list(Dict_of_current_Customer.values())
        if Index_current_Customer>0:        
            with open("Customers_Details","r+")as file:
                file.readlines(Index_current_Customer)
                file.writelines(f'\n{List_User_Values}')
        else:
            with open("Customers_Details.txt","w")as file:
                file.writelines(f'{List_User_Values}')
    except FileNotFoundError:
        print("Update Change Customer Details File is Not Found")

Update_Customers()
# print(Customers)
Update_Users()
# print(Users)
Update_Activity()
# print(Update_Activity)
Options()