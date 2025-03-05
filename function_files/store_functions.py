#--store_functions file that provides functions for store management and handling:

#--Importing __init__.py and store_functions.py:
import function_files
import function_files.store_functions

#--Function for viewing products (.load_file loads the .bin file with product list)
def display_products(file_name):

    products_list = function_files.load_file(file_name)

    if not products_list:
        print("\n>>. ⚠️ - Sorry, our product list is empty!")
    
    print("-" * 50)
    for product in products_list:
        print(f">>. 📃 - ID: {product['id']} | '{product['name']}' | {product['quantity']} pcs. | ${product['price']}")
    print("-" * 50)

#--Function for adding products (.load_file loads the .bin file with product list)
def add_product(file_name):

    print("-" * 50)
    product_name = input(">>. Enter product name: ")
    product_quantity = input(">>. Enter the quantity: ")
    product_price = input(">>. Enter product price: ")
    print("-" * 50)
    
    #--Adding product list:
    products = function_files.load_file(file_name)

    #--Generating new product ID:
    new_id = len(products)
    if new_id == 0:
        product_id = 1
    else:
        product_id = products[-1]['id'] + 1

    #--Creating a new product:
    product = {
        'id': int(product_id),
        'name': product_name,
        'quantity': int(product_quantity),
        'price': float(product_price)
    }
    #--Adding a product to the list:
    products.append(product)
    print(f">>. ✅ - '{product['name']}' added!")

    #--Saving a product in .bin file:
    function_files.save_files(file_name, products)

#--Function for removing products
def remove_product(file_name):

    #--Prints the product list:
    function_files.store_functions.display_products(file_name)
    
    #--Input the ID of the product you want to delete:
    print("-" * 50)
    delete_product_id = int(input(">>. Please enter ID of the product you want to remove: "))

    #--Loading the products:
    products = function_files.load_file(file_name)
    product_index = function_files.find_product_index(file_name, delete_product_id)

    if product_index > -1:
        del products[product_index]
        print(f">>. ✅ - Product {products['name']} deleted!")
    else:
        print(f">>. ⚠️ - Error! The product with ID:{delete_product_id} does not exist!")

#--Function for updating products
def update_products(file_name):

    #--Prints the product list:
    function_files.store_functions.display_products(file_name)
    #--Input the ID of the product:
    print("-" * 50)
    update_product_id = input(">>. Please enter ID of the product you want to change: ")

    #--Loading the products:
    products = function_files.load_file(file_name)
    product_index = function_files.find_product_index(file_name, update_product_id)

    #--Checking if product exists:
    if product_index > -1:
        print(f">>. You are updating a product with ID:{update_product_id}:")

        product_name = input(f">>. Changing the name of {products['name']}: ")
        product_quantity = input(f">>. Changing the quantity (old: {products['quantity']})")
        product_price = input(f">>. Changing the price (old: {products['price']})")

        if product_name.strip():
            products['name'] = product_name
        if product_quantity.strip():
            products['quantity'] = int(product_quantity)
        if product_price.strip():
            products['price'] = float(product_price)

        function_files.save_files(file_name, products)
        print("\n>>. 🎉 - Update succesful!")  
    else:
        print(f">>. ⚠️ - Error! The product with ID:{update_product_id} does not exist!")
