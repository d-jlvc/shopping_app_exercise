#--__init__ file for basic operations:

#--Importing: 'os' for file creation, 'pickle' for binary file creation
import os
import pickle

#--File creation def (Creates a file if it doesn't exist):
def create_file(file_name):

    if not os.path.exists(file_name):
        with open(file_name, 'wb') as f:
            pickle.dump([], f)

#--File loading def (Returns the list of stored products):
def load_file(file_name):

    with open(file_name, 'rb') as f:
        return pickle.load(f)   #--Return is needed to get some information back!

#--File saving def (Saves products on file // Ensures files are saved PERMANENTLY):
def save_files(file_name, products):

    with open(file_name, 'wb') as f:
        pickle.dump(products, f)

#--Find product index def (Finds an index of a product in list by it's ID):
def find_product_index(products, product_id):

    for i in range(len(products)):
        if products[i]['id'] == product_id:
            return i
        return -1
    
