#--Store application file
#--This file contains a code to run a store simulation

#--Creating a variable for a .bin file:
PRODUCTS_FILE = 'products.bin'

#--Importing functions from 'functions' folder // __init__.py
import function_files
import function_files.store_functions as Functions

#--File creation:
function_files.create_file(PRODUCTS_FILE)



#--MAIN PROGRAM:
while True:

    #--Welcome message:
    print("\n>>. 💻 - WELCOME TO VIRTUAL SHOP ASSISTANT! Type 'help' for info.")

    #--User input:
    user_input = input("\n>>. PLEASE ENTER DESIRED COMMAND: ")

    #--Main program:
    if user_input.lower() == 'help':
        print("""
    [1] - Products overview.
    [2] - Products input.
    [3] - Products deletion.
    [4] - Products update.
    [S] - Start shop app.
    [Q] - Quit the application.
    """)    
    elif user_input.upper() == 'Q':
        print("\n\n>>. 👋 - Good Bye!")
        import sys
        sys.exit()
    elif user_input == '1':
        Functions.display_products(PRODUCTS_FILE)   
    elif user_input == '2':
        Functions.add_product(PRODUCTS_FILE)
    elif user_input == '3':
        Functions.remove_product(PRODUCTS_FILE)
    elif user_input == '4':
        Functions.update_products(PRODUCTS_FILE)
    elif user_input.upper() == 'S':
        import function_files.shop
    else:
        print(">>. ⚠️ - Unknow command! Please, type 'help' for info.")
