import math

# A function to print all prime factors of 
# a given number n
def primeFactors(n):
    
    # Print the number of two's that divide n
    #this applies a cnocept that smaller if went through wont come again
    while n % 2 == 0:
        print(2),
        n = n / 2
        
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        
        # while i divides n , print i and divide n
        print("sqrt(n))-->itrstion", math.sqrt(n), i)
        while n % i== 0:
            print(i)
            print(i)
            n = n // i
            
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(round(n))

        # Driver Program to test above function

n = int(input("enter the number for which we need prime factor"))
primeFactors(n)
        