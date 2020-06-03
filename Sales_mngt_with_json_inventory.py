import json
from vat import discount_purchase, tax_deduction

#inventory = {'Rice':{'price': 50, 'quantity': 100}, 'Bread':{'price': 20, 'quantity': 5}, 'Fish':{'price': 100, 'quantity': 10}}
#Load data from JSON file

with open('inventory.json', 'r', encoding="utf8") as file:
    inventory = json.load(file)


    def process_purchase():
        print('Welcome to Nkatah Grocery Stores')
        counter = 0
        total_amount = 0
        total_after_tax = 0
        total_after_discount = 0
        cart = []
        product_count = int(input('How many products do you want to buy today?: '))

        # aggregate items in cart
        while counter < product_count:
            product = input('Enter the product you want to buy: ')
            if product in inventory:
                qty = int(input('How many do you want?: '))
                cart.append([product, qty])
                counter += 1
            else:
                print('Sorry {} is not currently available'.format(product))
                continue

        print('\n')

        for items in cart:
            amount_purchased = inventory[items[0]]['price'] * items[1]
            total_amount += amount_purchased

            if total_amount < 500:
                total_amount = total_amount
            elif total_amount > 1000:
                total_after_discount += discount_purchase(total_amount)
            elif total_amount > 500 & total_amount < 1000:
                total_after_tax += tax_deduction(total_amount)
            else:
                pass

        # Print purchased reciept
        print('Nkatah Grocery Stores \n\t\t Purchase Receipt \n')
        print('Product Bought \t\t Quantity')
        for cart_item in cart:
            print(cart_item[0], '\t\t\t\t', cart_item[1])
        for cart_item in cart:
            if total_amount < 500:
                print('Total Amount: \t\t{}'.format(total_amount))
            elif total_amount > 1000:
                print('Total Amount: \t\t{}'.format(total_amount))
                print('Total Amount After Discount: \t\t{}'.format(total_after_discount))
            elif total_amount >= 500 & total_amount <= 1000:
                print('Total Amount: \t\t{}'.format(total_amount))
                print('Total Amount After Tax: \t\t{}'.format(total_after_tax))
            else:
                pass



    def update_inventory():
        new_products = []
        counter = 0
        num_products = int(input('How many products do you want to add? '))
        while counter < num_products:
            item = input('Enter a product: ')
            qty = int(input('Enter the quantity: '))
            price = int(input('Enter the price: '))
            product_info = {item:{'price':price, 'quantity':qty}}
            new_products.append(product_info)
            counter += 1
        for i in new_products:
            inventory.update(i)
            with open('inventory.json', 'w', encoding="utf8") as f:
                json.dump(inventory, f)

        print('Updated inventory:')
        for prod in inventory:
            print(prod, '\t\t', inventory[prod]['quantity'])


    #update_inventory()

    process_purchase()