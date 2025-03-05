#--shop_functions file that provides functions for shopping cart management:

#--Importing __init__.py and store_functions.py:
import function_files
import function_files.shop_functions
import function_files.store_functions

#--Display cart function:
def display_cart(file_name):

    #--Loading items (will use 'receipt.bin')
    cart_items = function_files.load_file(file_name)

    if not cart_items:
        print(f"\n>>. 🤷‍♂️ - Your cart is empty!")

    print("~" * 50)
    for item in cart_items:
        print(f">>. 🛒 - '{item['name']}' - {item['quantity']} pcs.")
    print("~" * 50)

#--Add to cart function:
def add_cart(file_name):

    #--Input:
    print("~" * 50)
    product_choice = input(">>. Enter a product you want to purchase: ")
    product_quantity = int(input(">>. How many items? "))
    print("~" * 50)

    #--Loading .bin-s
    products = function_files.load_file('products.bin')
    cart = function_files.load_file(file_name)

    #--Making variable for store items:
    selected_product = None
    for product in products:
        if product['name'].lower() == product_choice.lower():
            selected_product = product
            break

    selected_product['quantity'] = int(selected_product['quantity'])

    if not selected_product:
        print(f">>. ⚠️ - Sorry, '{product_choice}' is unavailable!")
        return
    
    if selected_product['quantity'] < product_quantity:
        print(f">>. ⚠️ - Sorry, '{product_choice}' has only {selected_product['quantity']} pcs. on stock!")
        return
    
    #--Adding to cart:
    cart_items = {
        'name': product_choice,
        'quantity': product_quantity,
        'price': selected_product['price'] * product_quantity
    }
    cart.append(cart_items)
    selected_product['quantity'] -= product_quantity

    #--Saving files:
    function_files.save_files(file_name, cart)
    function_files.save_files('products.bin', products)

    print(f">>. ✅ - '{product_choice} ({product_quantity}) added to cart!")

#--Remove from cart function:
def remove_cart(file_name):

    #--View items in cart:
    function_files.shop_functions.display_cart(file_name)

    #--Load the cart:
    cart = function_files.load_file(file_name)

    if not cart:
        print(">>. 🤷‍♂️ - Your cart is empty!")

    #--Input:
    product_choice = input(">>. Enter a product you want to remove: ")

    #--Finding and removing item 👀:
    for item in cart:
        if item['name'].lower() == product_choice.lower():
            cart.remove(item)
            print(f">>. ✅ - '{item['name']}' removed!")
            break

    else:
        print(f">>. ⚠️ - Sorry, '{product_choice} is not in your cart!")
    
    #--Saving files:
    function_files.save_files(file_name, cart)

#--Clearing cart:
def clear_cart(file_name):

    #--Load the cart:
    cart = function_files.load_file(file_name)

    if not cart:
        print(">>. 🤷‍♂️ - Cart is already empty!")
        return
    
    #--Clearing the cart:
    cart.clear()
    print(">>. ✅ - Cart cleared!")

    #--Saving files:
    function_files.save_files(file_name, cart)

def get_receipt(file_name):

    #--Load the cart:
    cart = function_files.load_file(file_name)

    #--Printing the receipt:
    print("~" * 50)
    print("R E C E I P T : ")
    print("~" * 50)
    print(f"{'Item':<15} {'Pcs':<5} {'Price':<10} {'Total':<10}")
    print("-" * 50)

    total_amount = 0

    for item in cart:
        item_total = item['quantity'] * item['price']
        total_amount += item_total
        print(f"{item['name']:<15} {item['quantity']:<5} ${item['price']:<10.2f} ${item_total:<10.2f}")

    print("-" * 50)
    print(f"{'Grand Total':<25} ${total_amount:<10.2f}")

    print("\n>>. 👋 💖 - Thank you for your purchases! See you soon!")

    cart.clear()
    function_files.save_files(file_name, cart)

    import sys
    sys.exit
