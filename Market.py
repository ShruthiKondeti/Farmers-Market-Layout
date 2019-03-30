from Shop import *

class Market:

    global num_of_shops 
    # list of shops
    num_of_shops = [1,2,3,4,5,6,7,8,9,10]
    
    # check the availability of shops
    @classmethod
    def check_availability(self):
        if num_of_shops:
            return True
        else:
            return False

    # return the available shops
    @classmethod
    def total_availability(self):
        chk = self.check_availability()
        if chk:
            return num_of_shops
        else:
            return 0
    
    #remove the shop, once selected by the farmer
    @classmethod
    def remove_shop(self,inp):
            num_of_shops.remove(inp)
    
    #add shop details
    def add_shop_info(self, inp):
        print("Enter Shop Details.....")
        shop_num = inp
        title = str(raw_input("Please enter the title of the shop --> "))
        print("We can accomodate four different types of shops")
        print("1. vegetables \n2. Fruits \n3. Meat \n4. Food and Beverages")

        while True:
            shop_type = str(raw_input("Please enter the your shop type --> "))
            if shop_type == '1':
                shp = Shop(str(title),'vegetables',shop_num) 
                break   
            elif shop_type == '2':
                shp = Shop(str(title),'Fruits',shop_num)   
                break
            elif shop_type == '3':
                shp = Shop(str(title),'Meat',shop_num)  
                break 
            elif shop_type == '4':
                shp = Shop(str(title),'Food and Beverages',shop_num)  
                break  
            else:
                print("Please enter valid choice")
        Market.remove_shop(inp)
        Shop.shop_details(shp)
    
    # display the deatils of the shop to customer
    def display_shop_details(self):
        Shop.display_shops()
        