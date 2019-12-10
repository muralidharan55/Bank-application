bal=50000
while True:
	name=input("enter the name:")
	if name.isdigit()==False:
		break
	else:
		print("!!!enter name correctly!!!")
		continue
while True:
	ac=input("enter the account number:")
	len_ac=len(ac)
	if len_ac!=14:
		print("!!!enter correct account number!!!")
		continue
	else:
		break
while True:
	pwd=input("enter the password")
	len_pwd=len(pwd)
	if len_pwd!=4:
		print("!!!enter correct password!!!")
		continue
	else:
		print("Deposit","Withdraw","Balance")
		break
				
def deposit():
	dep_amount=int(input("Enter the deposit amount:"))
	bal1=dep_amount+bal
	print("The amount has been deposited")
	print(bal1)
	
def withdraw():
	withdraw_amount=int(input("Enter the withdrawl amount:"))
	if withdraw_amount>bal:
		print("!!!Your account has not enough balance!!!")
	else:
		print("collect your cash")
		bal2=bal-withdraw_amount
		print("your account balance is:")
		print(bal2)

def balance():
	print("Your Account Balance is:")
	print(bal)
	print("Thanks for visiting")
	
options=int(input("select your option"))
if options==1:
	deposit()
if options==2:
	withdraw()
if options==3:
	balance()
if options>3:
	print("!!!Select a valid option!!!")
	
