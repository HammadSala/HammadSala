#Module to append complext list

#DEclare Dictionary Subject with Class

class my_Orders(dict):
    #init
    def __init__(self):
        self=dict
    #Function to add Key value
    def addvalue(self, key1, value1,key2,  value2):
        self[key1]=value1
        self[key2]=value2

#Call the Diction object Main function
dct_Obj = my_Orders()
Iteration_count=int(input("Enter the number of orders to be added"))

def add_orders():
    dct_Obj.key1= input("Enter OrderName")
    dct_Obj.value1= input("Enter Name of order")
    dct_Obj.key2= input("Enter Count")
    dct_Obj.value2= input("Enter Count of Order")
    dct_Obj.addvalue(dct_Obj.key1,dct_Obj.value1,dct_Obj.key2,dct_Obj.value2)

for x in range((Iteration_count)):
    add_orders()

print("Dictionary", dct_Obj)