# Find e to the Nth Digit
# Formula = (1 + 1 / n)^n when n is infinity
# ===================
#Declaring value for intertions and the euler calculation
# For example, (1 + 1 / 100,000)^100,000 = 2.7182
n=0
eu=int(0)
itr=int(input("Enter the number of iteration to be performed"))

def Euler_calc(itr):
    eu =(1+1/itr)**itr
    return eu



# e=(n+1)^itr
eu = Euler_calc(itr)
print("Eulers value for the iteration number {0} is {1}".format(itr, eu))

