# The Shoes class is a blueprint for creating objects. An object created from the Shoes class will have the attributes country, code, product, cost, and quantity.
class Shoes():#create class
    def __init__ (self, country, code, product, cost, quantity ):#class variables (initialization)
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # The function `get_cost` takes no arguments and returns the cost of the shoe
    def get_cost (self) : 
        return self.cost

    # The function get_quanty() prints the quantity of the shoe.
    def get_quantity (self) :
        return self.quantity

    def set_quantity(self, newQuant):
        self.quantity = newQuant

    def __str__(self):#return object string
        return f"""Country: {self.country}
Code : {self.code}
Product : {self.product}
Shoe Price: {self.cost}
Quantity: {self.quantity}
"""
    # The __repr__ function returns a string representation of the object.
    def __repr__(self):
        return f"""\nCountry: {self.country}
Code : {self.code}
Product : {self.product}
Shoe Price: {self.cost}
Quantity: {self.quantity}
"""

# Shoe_list is a list that will hold the objects created from the Shoes class.
shoe_list = []

def update_file():#update the txt file
    with open("inventory.txt","w+") as inventory_file :
        inventory_file.write("Country,Code,Product,Cost,Quantity")
        for shoe in shoe_list:
            shoe_string_repr = f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}"
            inventory_file.write(shoe_string_repr)

# This function reads the data from the inventory.txt file and creates a list of Shoes objects
def read_shoes_data () :
    inventory_file = None

    # This is a try and except block. The try block will try to open the file. 
    try:
        with open("inventory.txt","r") as inventory_file :
            for data in inventory_file.readlines()[1:]:
                inventory_file = data.strip("\n").split(",")
                temp_shoe = Shoes(inventory_file[0], inventory_file[1], inventory_file[2], float(inventory_file[3]), int(inventory_file[4]))
                shoe_list.append(temp_shoe)

    # If the file does not exist, the except block will execute.
    except FileNotFoundError :
        print("The file that you are trying to open does not exist")

# This function captures the user input and creates a new instance of the Shoes class.
def capture_shoes ():
    country_input = input("Please enter the Country: ")
    code_input = input("Please enter the Code: ")
    product_input = input("PLease enter the Product: ")
    cost_input = float(input("Please enter the Cost: "))
    quanity_input = int(input("Please enter the Quanity: "))
    capture_shoeList = Shoes(country_input,code_input,product_input,cost_input,quanity_input)
    shoe_list.append(capture_shoeList)
    print(f"\nThank You! Shoe has been captured.\n")
    update_file()

# This function prints all the data in the shoe_list.
def view_all ():
    for data in shoe_list :
        print(data)

# The above function finds the shoe with the lowest quantity.
def re_stock () :
    index_shoe = 0
    lowest_qty = shoe_list[index_shoe].get_quantity()
    for index, dataLine in enumerate(shoe_list):
        if int(dataLine.get_quantity()) < int(lowest_qty):
            lowest_qty = dataLine.get_quantity()
            index_shoe = index
    print(f"\nThe shoe object with the Lowest Quanity is:\n{shoe_list[index_shoe]}")

    # This is a function that is asking the user if they would like to update the quantity of the shoe with the lowest quantity.
    quantity_update = input("Would you like to update the Quanitity(Yes/No): ").lower()
    if quantity_update == "yes" :
        new_quantity = int(input("Please enter the new Quantity: "))
        shoe_list[index_shoe].set_quantity(new_quantity)
        print("\nThank you! The quantity has been updated.")
        print(f"{shoe_list[index_shoe]}")

    elif quantity_update == "no" :
        print("\nThank you! The quantity will remain the same.\n")
    
    else:
        print("invalid entry")

    update_file()

# This function asks the user to input a code, and then searches the shoe_list for a shoe with that code. If it finds one, it prints the shoe
def search_shoe () :
    code_input = input("Please enter the code of the shoe you are looking for: ")
    for data in shoe_list : 
        if data.code == code_input:
            print(data)

# This function will print the total value of each item in the shoe_list.           
def value_per_item () :
    for data in shoe_list :
        total_cost = data.get_cost() * data.get_quantity() 
        print(f"\n{data}Total Value: {total_cost}\n")

# This function will iterate through the list of shoe objects and find the shoe object with the highest quantity.
def highest_qty () :
    index_shoe = 0
    highest_qty = shoe_list[index_shoe].get_quantity()
    for index, dataLine in enumerate(shoe_list):
        if int(dataLine.get_quantity()) > int(highest_qty):
            highest_qty = dataLine.get_quantity()
            index_shoe = index
    print(f"\nThe shoe object with the Highest Quanity is:\n{shoe_list[index_shoe]}")
    print(f"This shoe is for sale!\n")

#==== Menu Section ====#
# This is a menu that is displayed to the user to select one of the options.
read_shoes_data()
while True:
    
    menu = input('''Select one of the following Options below:
c  - capture shoes 
va - view-all 
rs - re-stock
s  - seach shoe
v  - value per-item
hq - highest qauntiy
e  - exit
: ''').lower()

    # Menu that allows the user to select from a list of options.
    if menu == 'ca':
        capture_shoes ()

    elif menu == 'va':
        view_all ()
    
    elif menu == 'rs':
        re_stock ()
    
    elif menu == 's' :
        search_shoe () 
    
    elif menu == 'v' :
        value_per_item ()
    
    elif menu == 'hq':
        highest_qty () 

    elif menu == 'e':
        print('\nGoodbye!!!\n')

    else:
        print("\nInvalid Entry! Please read the menu carefully and Try again\n")
