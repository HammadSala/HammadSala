#Change Return Program 
# 1 rupee is 60 paise
# Make everything as in paise ,  x=x*60
# subtract and the divide and displays

#Vairblae declartions

amount = int(input("Enter the amount giv by user \n"))
cost = str(input("Enter the cost of the product \n"))

def main():
    amount_paise=amount*100 #converting given amount in paise, maing them all same unit
    cost_paise=str(cost).split('.') # using string split function and split them, learnt splut, // word.split('delimeter')
    cost_paise_sum = int(cost_paise[0])*100 + int(cost_paise[1]) # converting to paise and summ if any amount paie in bill
    balance_paise= amount_paise - cost_paise_sum #Finding the balance
    bal_rupee = balance_paise/100 # tried devmod didnt do well, so using manaul division
    bal_paise = str(bal_rupee).split('.') #split the string for output formating
    print(f'{"Balance is {0} rupee and {1} paise".format( bal_paise[0],int((bal_paise[1])))}')#printing the result
    a,b= divmod(balance_paise,100) #in last tried a attemo with divmod and it worked :)
    print('---',a,b)


main()
