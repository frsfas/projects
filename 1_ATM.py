import datetime
import random

x=datetime.datetime.now()
print("*** Welcome To FAS Bank ATM ***")

def fast_cash():
    print("1 -> 500")
    print("2 -> 1000")
    print("3 -> 5000")
    print("4 -> 10000")
    print("5 -> 15000")
    print("6 -> 20000")
    print("7 -> 25000")
    
    fastcash=int(input("Please Selected a Number:"))
    if fastcash==1:
        print("Please Collected Your Cash ** 500 **")
        print(x)
    elif fastcash==2:
        print("Please Collected Your Cash ** 1000 **")
        print(x)
    elif fastcash==3:
        print("Please Collected Your Cash ** 5000 **")
        print(x)
    elif fastcash==4:
        print("Please Collected Your Cash ** 10000 **")
        print(x)
    elif fastcash==5:
        print("Please Collected Your Cash ** 15000 **")
        print(x)
    elif fastcash==6:
        print("Please Collected Your Cash ** 20000 **")
        print(x)
    elif fastcash==7:
        print("Please Collected Your Cash ** 25000 **")
        print(x)
    else:
        print("Please Selected the Valid Number")

    exit1=input("Are You Continued This Session *** Type = Y *** : ")
    if exit1=="Y":
        main_page()
    else:
        print("Thanks For Using FAS Bank ATM")

def withdrawal():
    drawn=int(input("Please Enter the Amount:"))
    if drawn%100==0:
        print(f"Please Collected your{drawn} Cash")
        print(x)
    else:
        print("Please Enter the Valid Amount Multiply of 100")
    
    exit2=input("Are You Continued This Session *** Type = Y *** : ")
    if exit2=="Y":
        main_page()
    else:
        print("Thanks For Using FAS Bank ATM")

def balance():    
    available_balance=250000
    print(f"Your Available balance {available_balance}") 
    print(x)
    exit3=input("Are You Continued This Session *** Type = Y *** : ")
    if exit3=="Y":
        main_page()
    else:
        print("Thanks For Using FAS Bank ATM")
        
def more():
    f=open("fas_bank.txt","r")
    print(f.read())
    exit4=input("Are You Continued This Session *** Type = Y *** : ")
    if exit4=="Y":
        main_page()
    else:
        print("Thanks For Using FAS Bank ATM")
def contact():
    print(" Please Reached Out in FAS Bank (044-789456)")
    exit6=input("Are You Continued This Session *** Type = Y *** : ")
    if exit6=="Y":
        main_page()
    else:
        print("Thanks For Using FAS Bank ATM")

def main_page():
    
    a=[123456,234567,345678,456789,567890,678901,789012,890123,901234]
    acc_no=int(input("Please Enter Your Six Digit Accoumt Number:"))
    if acc_no in a:
        print("OTP Sended Successfully")
        otp_no=random.randint(0000,9999)
        print(f"****Your OTP is {otp_no}*****")
        validate=int(input("Enter Your OTP Number:"))
        if otp_no==validate:
            print("OTP Verified Seccessfully....")     
            print("1 -> Fast Cash")
            print("2 -> Withdrawal")
            print("3 -> Balance")
            print("4 -> More Info")
            print("5 -> Contact ATM")
            user=int(input("Select the Number:"))
            if user==1:
                fast_cash()
            elif user==2:                             
                withdrawal()
            elif user==3:
                balance()
            elif user==4:
                more()
            elif user==5:
                contact()
            else:
                print("Select the Valid Number")
        else:
            print("Invalid OTP")
    else:
        print("Sorry.. Invalid Account Number, Please Contact Your Branch.")
main_page()
    
       