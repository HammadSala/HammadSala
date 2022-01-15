#Formula to claculate PI , X =4/1-4/3+4/5-4/7+...

#DEclare the varaibles
K=1
s=0

it =int(input("Enter the number of iteeration to be repeated to calculate PI"))

for i in range (it):
    if(i%2==0):
        s = s + 4/K
    elif(i%2!=0):
        s = s - 4/K
    #Incrementing K by 2 for each iteration as per the formula
    K+=2



print("Value of PI for the iternatoin{0} is {1} ".format(it,s))


