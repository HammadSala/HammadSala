#A Prodcut Templaate file
import datetime
import time


Productss =[]

class my_Products(dict):
    #init
    def __init__(self):
        self=dict
        global product_name
        global product_id
        global product_value
        global product_dsicount
        global product_availality
        global product_description
        global product_details
        global product_reviews
        product_name = input("Enter the details of Product Name\n")
        product_id = input("Enter the details of ID\n")
        product_value = input("Enter the details of Value\n")
        product_dsicount = input("Enter the details of discount\n")
        product_availality = input("Enter the details of Availablity\n")
        product_description = input("Enter the details of description\n")
        product_details = input("Enter the details of details\n")
        product_reviews = input("Enter the details of reviews\n")
    

    def product_set(self,product_name,product_id,product_value,product_dsicount,product_availality,product_description,product_details,product_reviews):
        self['product_name'] = product_name
        self['product_id']=product_id
        self['product_value']=product_value
        self['product_dsicount']=product_dsicount
        self['product_availality']=product_availality
        self['product_description']=product_description
        self['product_details']=product_details
        self['product_reviews']=product_reviews
        self['timedetail']= datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        
prdt1 = my_Products()
#This will be callled from outside
prdt1.product_set(product_name,product_id,product_value,product_dsicount,product_availality,product_description,product_details,product_reviews)
Productss.append(prdt1)
#This will be a return variable
print("/List", Productss)


