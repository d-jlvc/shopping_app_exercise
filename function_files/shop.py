#--Shop application file
#--This file contains a code to run a shop simulation, will be accessed in main

#--Creating variables for .bin file:
CART_FILE = 'cart.bin'
PRODUCTS_FILE = 'products.bin'

#--Importing function_files:
import function_files
import function_files.shop_functions
import function_files.store_functions

#--File creation:
function_files.create_file(CART_FILE)


#--Main program:
while True:

    #--Initial message:
    print("\n>>. 🏪 WELCOME TO OUR STORE APP! 🏪 .<<")
    print(">>. ❔ - Type 'help' for info! - ❔ .<<")

    #--Input choice:
    user_input = input(">>. PLEASE ENTER DESIRED COMMAND: ")

    if user_input.lower() == 'help':
        print("""
    [1] - View available articles.
    [2] - Add to cart.
    [3] - Remove from cart.
    [4] - View cart.
    [5] - Empty the cart.
    [6] - Get receipt.
    [Q] - Exit.
    """)
    elif user_input.upper() == 'Q':
        print("\n>>. 👋 - Goodbye!")
        import sys
        sys.exit()
    elif user_input == '1':
        function_files.store_functions.display_products(PRODUCTS_FILE)
    elif user_input == '2':
        function_files.shop_functions.add_cart(CART_FILE)
    elif user_input == '3':
        function_files.shop_functions.remove_cart(CART_FILE)
    elif user_input == '4':
        function_files.shop_functions.display_cart(CART_FILE)
    elif user_input == '5':
        function_files.shop_functions.clear_cart(CART_FILE)
    elif user_input == '6':
        function_files.shop_functions.get_receipt(CART_FILE)
    else:
        print(">>. ⚠️ - Unknow command! Please, type 'help' for info.")

