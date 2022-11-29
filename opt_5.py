import pandas as pd

items = []
df_items = pd.DataFrame(items)
while True:
    print("=============WELCOME TO THE SSUPERRMARKET=============")
    print("1. Add Item to Buy \n2. Update Item \n3. Delete Item \n4. Review Order \n5. Reset Order \n0. Exit")
    opt = int(input("What would you like to do? Input the number: "))
    if opt == 1:
        item = {}
        print("-"*25)
        print("ADD ITEM TO BUY")
        print("-"*25)
        def item_detail(item_name, total_item, price_per_item):                            
            print("Your order has been recorded!")
            print(f"You are going to buy: {item_name} with total of {total_item} pcs. The total price for your order is: {total_item*price_per_item}")
                
            item['name'] = item_name
            item['qty'] = total_item
            item['price_per_item'] = price_per_item
            item['total_price'] = total_item*price_per_item
            items.append(item)
            
        item_detail(input("Item name: "), int(input("Total item: ")), int(input("Price per item: ")))
        
    elif opt == 2:
        def update_item_name(self, new_item_name):
            item['name'] = 
        def update_item_qty(self, new_total_item):
            item['total_item'] = new_total_item
        def update_item_price(self, new_price_per_item):
            item['price_per_item'] = new_price_per_item
        
        print("-"*25)
        print("UPDATE ITEM")
        print("-"*25)
        print("\n1. Name \n2. Quantity \n3. Price")
        opt = int(input("Input: "))
        if opt == 1:
            update_item_name(input("Update item name: "))
        elif opt == 2:
            update_item_qty(int(input("Update item quantity: ")))
        else:
            update_item_price(int(input("Update item price: ")))
    
        print("The change has been recorded!")
        print(f"You are going to buy: {item_name} with total of {total_item} pcs./nThe total price for this item is: {price_per_item*total_item}")
        
    elif opt == 3:
        print("-"*25)
        print("DELETE ITEM")
        print("-"*25)
        delete_item_name = input("Input item name: ")
        if delete_item_name == df_items['name']:
            item.pop(name)
            print("The item has been deleted")
        else:
            print("The input can not be proceed.")
        print(df_items)
        
    elif opt == 4:
        sum_price = sum(df_items['total_price'])
        if sum_price > 200000:
            sum_price -= (sum_price*0.05)
        elif sum_price > 300000:
            sum_price -= (sum_price*0.08)
        elif sum_price > 500000:
            sum_price -= (sum_price*0.1)
        else:
            sum_price
                
        print("-"*25)
        print("REVIEW ORDER")
        print("-"*25)
        print(df_items)
        print(f"Total payment: {sum_price}")
        payment = int(input("Willing to be proceed to payment? /n1. Yes/n0. No"))
        if payment == 1:
            items.clear()
            print(f"Your order has been paid! Have a good day!")
        elif == 0:
            pass
    
   
    elif opt == 5:
        print("-"*25)
        print("RESET ORDER")
        print("-"*25)
        if len(items) > 0:
            try:
                items.clear()
                print("Your order has been cleared")
            except:
                print("Add items first!")
    else:
        break
    