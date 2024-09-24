# Build a banking application locally in python
import random
from enum import Enum
account =   {}

print( f"""
       ______  _______ __   _ _     _ _____ __   _  ______      _______  _____   _____       
       |_____] |_____| | \  | |____/    |   | \  | |  ____      |_____| |_____] |_____]      
 . . . |_____] |     | |  \_| |    \_ __|__ |  \_| |_____|      |     | |       |       . . .
""" )

def create_account(accs:dict,   acct_num, bank, acct_name, state):
    accs[acct_num]  =   {"bank": bank, "name": acct_name, "state": state, "balance":0}
    print(f"Your Account Registration is Successfull ")
    return accs
# =================== #
def bank_info(accs:dict):
    print(f"Account Number   |  Bank Name   |   Account Name    |   State   |   Balance")
    for ac in accs:
        acct_num =   str(ac).ljust(9," ")
        bank =   str(accs[ac]["bank"]).ljust(10," ")
        acct_name = str(accs[ac]["name"]).rjust(10," ")
        acct_state  =   str(accs[ac]["state"]).ljust(10," ")
        acct_amt =   str(accs[ac]["balance"]).ljust(10," ")
        print( f"{acct_num}      {bank}        {acct_name}       {acct_state}   {acct_amt}")
    return accs
# =================== # 

class Operation():
    CREDIT = 1
    DEBIT = 2
def transact(accs:dict,acct_num,amt,operation:Operation):
    msg = Operation
    if accs_exist(account,acct_num):
        current = accs[acct_num]["balance"]
        if operation == Operation.CREDIT:
            msg = "Credit"
            new_bal = current + amt
        else:
            msg = "Debit"
            new_bal = current - amt
        accs[acct_num]["balance"] = new_bal
        print(f"{msg} of {new_bal} Successful")
    return 

def check(accs:dict, acct_num):
    if accs_exist(accs,acct_num):
        current = accs[acct_num]["balance"]
        print(f"Your balance is {current}")
    return
# =================== # 

def accs_exist(accs:dict,acct_num)->bool:
    if acct_num in accs:
        return True
    else:
        print("Account Do Not Exist")
        return False
# =================== # 
while True:
    print("{1}-> Create Bank Account")
    print("{2}-> Bank Information")
    print("{3}-> Deposit")
    print("{4}-> Withdraw")
    print("{5}-> Check Balance")
    print("{0}-> Log out")
    
    user_info   =   int(input("Enter Your Choice:_"))
    
    if user_info    ==  1:
        bank    =   input("Enter Bank Name: ").title()
        acct_number    =   random.randint(12345,54321)
        acct_name    =   input("Enter Your Full Name:   ").title()
        acct_state    =   input("Enter Your State:  ").title()
        create_account(account, acct_number, bank, acct_name, acct_state)
    # =================== #
    elif user_info  ==  2:
        bank_info(account)
    # =================== #
    elif user_info  ==  3:
        account_number  =   int(input("Enter Account To Deposit: "))
        amount  =   float(input("Enter amount: "))
        # deposit(account,account_number,amount)
        transact(account,account_number,amount,Operation.CREDIT)
    # =================== #
    elif user_info == 4:
        account_number  =   int(input("Enter Withdrawal Account Number: "))
        amount  =   float(input("Enter Amount to withdraw: "))
        # withdraw(account,account_number,amount)
        transact(account,account_number,amount,Operation.DEBIT)
    # =================== #
    elif user_info == 5:
        account_number = int(input("Enter Account Number: "))
        check(account,account_number)
    elif user_info  ==  0:
        print("See you next time")
        break
    # =================== #
    else:
        print("INVALID")
    # =================== #