# Prime Factorization - 
# Have the user enter a number and find all Prime Factors (if there are any) and display them.
# ==============
# Get the number for which we need to find the prime number
# Make a function that divdes the quotient in a incremetal fashob until we get 0
# Store the quotient in a list
# When the remider is 1 and the quotient is 0 then we make the prime numbers for the given number
prime_List = []
itr = int(input("Enter the number for which we need to find the prime factor"))
# print("// and /% are",((itr/2),(itr//2),(itr%3)))

def p_finder(a):
    print("value in function a-->",a)
    #breakpoint()
    for i in range(2,a+1):
        num = a
        print("value in for function a-->",a,num)
        if num % i == 0:
            #breakpoint()
            print("before list",prime_List)
            prime_List.append(i)
            print("afer",prime_List)

            print("1st If loop numbr and iterrator an dlist inside-->",num,i)
            if num // i > 1:
                #breakpoint()
                num = num // i
                if num != 0:
                    print(" inside ifs if and value of inter to be apssed to func", num)
                    p_finder(num)
                else:
                    break
                
        elif (num // i) == 1:
            #breakpoint()
            break

p_finder(itr)

print("-=-",prime_List)
