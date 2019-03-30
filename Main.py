'''
Created on Mar 29, 2019
@author: shruthi
'''
from Market import *
from Shop import *
market = Market()

def main():
    print("Welcome to Downtown Farmers Market!!!")
    # get choice from user to perform various operations
    flag = True
    while flag:
        choice = str(raw_input("Please Enter your choice : \n1. Farmer \n2. Customer \n3. Quit \n"))
        if choice == '1':
            print("Please check the below details and select your shop")
            print("The total area available for market is 15,000 square feet")
            print("Total number of shops in Market are 10")
            print("Each shop is of 1000 square feet") 
            print('The number of shops available for registrat3ion -->', market.total_availability()) 
            #get the details from user
            flag = False
            while not flag:
                try:
                    inp = int(input("Please select the shop number from above list:"))
                    if int(inp) in market.total_availability():
                        market.add_shop_info(inp)
                        flag = True
                    else:
                        print("Incorrect shop number")
                except:
                    print("Please enter correct number")
            print(market.total_availability())
        # display the details of the shop
        elif choice == '2':
            try:
                market.display_shop_details()
            except:
                flag = False
                print("No shops in market.........Sorry")
                print("Please check after some time")
        # exit the program
        elif choice == '3':
            flag = False
            print("Thank You for visiting Downtown Farmers Market")  
        else:
            print("Invalid option...Please enter again")

main()