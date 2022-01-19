# Next Prime Number - 
# Have the program find prime numbers until the user chooses to stop asking for the next one.
# ===============================================

#Getting number from user
nos = int(input("Enter the number to which we need the next prime number"))
prime_no = nos  #initialising the reul pime number with the assinged number -21
cond = True  #Setting initial conditon as true to have the loop run infintyly until it finds next number -true
while cond is True: #Using the condition set
        prime_no +=1  # 21+1=22
        ref_no = prime_no+1 #=22
        # print("1+ prime_no", prime_no)
        #breakpoint()# Starting with the next number
        for i in range(2,ref_no,1): # i=2, 21, 1, 22
            status = prime_no % i # 21 % 1=>0, 
            status1 = prime_no / i # =11
            print(" \nNumber -->", prime_no)
            print(" \n incrementro 1 -->", i)
            print(" \n Mod is -->", status)
            print(" \n Div is -->", status1)


            #breakpoint()
            # print("status, prime_no and i ", prime_no,status, i)
            if (status == 0) and (ref_no-1 == i):
                print("Prime number is ---===>",ref_no-1)
                cond = False
                break
        break

                # cond = False
                # print("next nearest prime number is",prime_no)

                
