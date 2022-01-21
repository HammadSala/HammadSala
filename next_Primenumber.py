# Next Prime Number - 
# Have the program find prime numbers until the user chooses to stop asking for the next one.
# ===============================================

#Getting number from user



from unittest import result


numbers = int(input("Enter the number to which we need the next prime number"))
result1 = False
nos = numbers

def next_Primefinder(nos):
        result = False
        n = nos
        for i in range(2,n):
                # print ("\n",i, n)
                if(n % i) == 0:
                        print("i and n are", i, n, n%i)
                        result=False
                        break
                else: result = True

        return result
while result1 == False:
        result1=next_Primefinder(nos)
        if result1:
                print(result1,nos,"is the next Prime number")
        else:
                nos = nos+1

 


