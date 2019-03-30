'''
Created on Mar 29, 2019
@author: shruthi
'''
import json, os

class Shop():
    # constructor
    def __init__(self, title, type, id):
        self.title = title
        self.shoptype = type
        self.id = id 
    
    # stores the details of the shop in Json file
    def shop_details(self):
        data2 = {}
        data2['id'] = self.id
        data2['title'] = self.title
        data2['shop_type'] = self.shoptype
        if not os.path.exists('shop.json'):
            with open('shop.json','w') as f:
                data = {}
                data['shop'] = []
                data['shop'].append(data2)
                json.dump(data,f,indent=2, sort_keys=True)
        else:    
            with open('shop.json','r') as f:
                data = json.load(f)
            with open('shop.json','w') as f:
                data['shop'].append(data2)
                json.dump(data,f,indent=2, sort_keys=True)

    # display the details of the shop fetched from json file
    @staticmethod
    def display_shops():
        with open('shop.json','r') as f:
            data = json.load(f)
            print("Total number of shops in Market are 10")
            print("Shop details are displayed below")
            print(' ')
            for i in data['shop']:
                print('shop number --> ', i['id'])
                print('Title of the shop --> ', i['title'].encode("ascii","replace"))
                print('Shop Type --> ', i['shop_type'].encode("ascii","replace"))
                print("---------------------///////--------------------")