#binary to decimal 

#declare and intialising binary number

from ast import While


binaryno = '101101'

lengthofno = len(binaryno)
# print(lengthofno)

# print(binaryno[3])

def main():
    l =lengthofno
    basno = 0
    while l != 0:
        print(2**(int(l)))
        basno= (2**l)-1 + int(binaryno[l-1])
        # print("\n",basno)
        # print("\n",int(binaryno[l-1]))
        l=l-1
    print(basno)



    pass

main()