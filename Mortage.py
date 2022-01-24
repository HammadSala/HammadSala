#Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
# Also figure out how long it will take the user to pay back the loan. 
#For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually)

#Declaring the Fixed variables
Interestrate = int(7.3)
# noof_Premium = int(12)


#Declare the interactie user variable and fethc the vlaues from users
amount = int(input("Enter the Loan amount"))
premium = int(input("Enter the Monthly Premium amount"))
total_amnt = amount + (amount*(Interestrate/100))

def print_Line():
    tline = '-'*40
    print(tline)

def loan_Summary():
    print_Line()
    total_Amount = amount + (amount*(Interestrate/100))
    total_Interest = amount*(Interestrate/100)
    Monthly_Interest = total_Interest/premium   
    noofterms = total_Amount / premium
    print(f"Loan Sumamry\nBorrowed amonunt is :\t\t\t\t\t{amount:<1} ")
    # print(f"{amount:>20}")
    print(f"Loan Fixed ineters percentage is :\t\t\t{Interestrate:<1}%")
    print(f"Amunt after INterest is :\t\t\t\t{total_Amount:<1}")
    print(f"Monthly Premium is :\t\t\t\t\t{premium:<1}")
    print(f"Monthly Interest is :\t\t\t\t\t{round(Monthly_Interest):<1}")
    print(f"Total number of terms takes to complete the loan :\t{round(noofterms+1):<1}")
    print_Line()
    one_function()
    
    


def monthly_compund_calc():
    print_Line()
    month_toknow =int(input("Enter the month for which we need details ?"))
    paidamount = total_amnt -(premium *month_toknow)
    print("At month {0} total amount paid is {1} and balance amount is {2}".format(month_toknow,premium *month_toknow,paidamount))
    print("\n You have {0} pending to closue with month premium {1}".format(total_amnt-paidamount,12-month_toknow))
    print_Line()
    one_function()

def user_Switch(i):
    print_Line()
    print("insideswithc")
    switcher={
        0: lambda: loan_Summary(),
        1: lambda: monthly_compund_calc(),
        2: lambda: exit()
    }
    print_Line()
    return switcher.get(i,lambda:'Print the correct choice')()


def one_function():
    print_Line()
    choice_current=int(input("Enter the option below\n0)Acccount Summary\n1)Current Month Statement\n2)Exit"))
    print(choice_current)
    user_Switch(choice_current)    


def main():
    one_function()
 

    

main()






