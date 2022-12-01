import pandas as pd

items = []
while True:
    item = {} # define an empty dictionary to record data
    df_items = pd.DataFrame(items) # transform list into dataframe globally
    
    print("=============WELCOME TO THE SSUPERRMARKET=============")
    print("1. Add Item to Buy \n2. Update Item \n3. Delete Item \n4. Review Order \n5. Reset Order \n0. Exit")
    opt = int(input("What would you like to do? Input the number: "))
    
    if opt == 1:
        """
        option 1: to add new item to buy, could only proceed 1 item per-run
        :output: a list of item's name, price, and quantity
        """
        print("-"*25)
        print("ADD ITEM TO BUY")
        print("-"*25)
        def item_detail(item_name, total_item, price_per_item):                            
            print("Your order has been recorded!")
            print(f"You are going to buy: {item_name} with total of {total_item} pcs. The total price for your order is: {total_item*price_per_item}") 
            
            # input all item's detail into a dictionary
            item['name'] = item_name
            item['qty'] = total_item
            item['price_per_item'] = price_per_item
            item['total_price'] = total_item*price_per_item
            items.append(item) # append it to the empty list
            
        item_detail(input("Item name: "), int(input("Total item: ")), int(input("Price per item: ")))
       
    
    elif opt == 2:   
        """
        option 2: to update/change item's detail, could only proceed 1 detail.
        :output the notification that change has been saved."
        """
        print("-"*25)
        print("UPDATE ITEM")
        print("-"*25)
        if len(items) > 0: # the program would be proceed if there is any items on the list
            print("1. Name \n2. Quantity \n3. Price")
            opt_2 = int(input("Input: "))
            
            def upd_item(old_item_detail, update_item_detail):
                """
                Function to update item details, such as: name, quantity, or price.
                The old details that are not listed, won't affect any.
                :param: old item's name/price/quantity, and the new one.
                :return: the change of value in list.
                """
                for x in items:
                    for k, v in x.items():
                        if v == old_item_detail:
                            x[k] = update_item_detail
                        else:
                            pass
                        
            if opt_2 == 1:
                upd_item(input("Old item name: "), input("New item name: "))
                
            elif opt_2 == 2:
                upd_item(int(input("Old item quantity: ")), int(input("New item quantity: ")))
                
            elif opt_2 == 3:
                upd_item(int(input("Old price per item: ")), int(input("New price per item: ")))
                
            else:
                print("Please input a number from 1-3")
            
                
            print("The change has been recorded!")
            
        else:
            print("Please, add item first!")
        
        
    elif opt == 3:
        """
        option 3: to delete items based on item's name.
        :output: deleting item's name with notification that it has been deleted.
        """
        print("-"*25)
        print("DELETE ITEM")
        print("-"*25)
        if len(items) > 0:
            
            del_item_name = input("Input item name: ")
            
            for x in items:
                for k, v in x.items():
                    try:
                        if v == del_item_name:
                            items.remove(x)
                        print("The item has been deleted")
                    except:
                        print("The input can not be proceed.")
            
        else:
            print("Please, add item first!")
      
    
    elif opt == 4:
        """
        option 4: to review all orders and process to payment
        :output: dataframe of bought items and the total payment (including discount rules) and process to payment.
        """
        print("-"*25)
        print("REVIEW ORDER")
        print("-"*25)
        if len(items) > 0:
            sum_price = sum(df_items['total_price'])
            
            # count total price after discount
            if sum_price > 200000:
                sum_price -= (sum_price*0.05)
            elif sum_price > 300000:
                sum_price -= (sum_price*0.08)
            elif sum_price > 500000:
                sum_price -= (sum_price*0.1)
            else:
                sum_price
                
            print(df_items)
            print(f"Total payment: {sum_price}")
            
            # for payment processing
            payment = int(input("Willing to be proceed to payment? 1. Yes / 0. No"))
            if payment == 1:
                items.clear()
                print(f"Your order has been proceed! Have a good day!")
                break # to quit the loop
            elif payment == 0:
                pass # back to main menu
            
        else:
            print("Please, add item first!")
    
   
    elif opt == 5:
        """
        option 5: to clear all items
        :output: all items on the dictionary will be deleted and notification that it has been cleared.
        """
        print("-"*25)
        print("RESET ORDER")
        print("-"*25)
        if len(items) > 0:
            items.clear() # it will delete all items on the list
            print("Your order has been cleared")
        else:
            print("Please, add item first!")
            
    else:
        break # to quit from the loop
    
