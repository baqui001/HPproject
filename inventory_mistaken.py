
import code
from itertools import product
from tokenize import ContStr
from wsgiref import headers


class Shoes:#create new Shoes class
    def __init__(self, country, code, product, cost, quantity):#create constructor to initialise the class
        self.country = country#call variables
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
  
    def get_cost(self):#function to return cost
        return self.cost
 
    def get_quantity(self):#function to retunr quantity
        return self.quantity

    def __str__(self):#Return the string of the class/objects
        return self.country + ", " + self.code + ", "+self.product + ", " + str(self.cost) + ", "+ str(self.quantity)

shoes = []#create empty list to manage data from file

def read_shoes_data():#open the file and add the file content into our new list
    try:#Error  handeling in case we dont find the file
        lineNo = 0 #start count lines file
        with open("inventory.txt", 'r') as shoe_file:#open file
            for line in shoe_file:#iterate through file lines
                if lineNo != 0:
                    (country, code, product, cost, quantity) = line.rstrip('\n').strip().split(',')#split data from file
                    shoes.append(Shoes(country,code,product,int(cost),int(quantity)))#add data to list shoes as objects, quantity and cost cast to int
                lineNo += 1#to iterate each line unti the end of txt file
        print("Read info from inventory.txt file")
    except IOError:#Error handling
        print("File ", "inventory.txt", " not accessible")

def capture_shoes():#add new shoe-object to my list
    s_country = input("Enter country: ")#Ask user to insert properties
    s_code = input("Enter code: ")
    s_product = input("Enter product: ")
    s_cost = int(input("Enter cost: "))
    s_quantity = int(input("Enter quantity: "))

    shoe = Shoes(s_country, s_code, s_product, s_cost, s_quantity)#with inputs we create a new object
    shoes.append(shoe) #And add to my list shoes
    for shoe in shoes:
        print(str(shoe))

def view_all():#print list
    for shoe in shoes:
        print(str(shoe))


def re_stock():#function to get the lowest quantity and ask user to update quantity
    lowest_quantity = shoes[0]#lowest quantity in line 0
    for shoe in shoes:#iterate list to find lowest quantity
        if shoe.get_quantity() < lowest_quantity.get_quantity():
            lowest_quantity = shoe
    print("The lowest quantity is\n"+str(lowest_quantity))

    quantity_update = input("Would you like to change the quantity(yes/no)? ")
    if quantity_update.lower() == "yes":
        quantity_to_update = int(input("Enter new quantity to add to current stock: "))
        lowest_quantity.quantity = lowest_quantity.get_quantity() + quantity_to_update
    
    else:
        print("No need to restock")

def search_shoe(code):#find shoe with code
    for shoe in shoes:
        if shoe.code == code:
            return shoe#return object from code

def value_per_item():#calculate value shoes
    value = 0
    for shoe in shoes:#iterate list
        value = shoe.get_cost() * shoe.get_quantity()#multiply cost per quantity
        print(str(shoe) +"\tValue: " + str(value)) #print value per shoes
    return value#return value


def highest_quantity():
    highest_quantity_shoe = shoes[0]
    print(shoes[0])
    for shoe in shoes:# iterate through the list
        if shoe.get_quanty() > highest_quantity_shoe.get_quanty():#check highest quantity
            highest_quantity_shoe = shoe
    print(str(highest_quantity_shoe))#print result

# This function will iterate through the list of shoe objects and find the shoe object with the highest quantity.
def highest_qty () :
    index_shoe = 0
    highest_qty = shoes[index_shoe].get_quantity()
    for index, dataLine in enumerate(shoes):
        if int(dataLine.get_quantity()) > int(highest_qty):
            highest_qty = dataLine.get_quantity()
            index_shoe = index
    print(f"\nThe shoe object with the Highest Quanity is:\n{shoes[index_shoe]}")
    print(f"This shoe is for sale!\n")


if __name__ == '__main__':
    choice = 0
    while True:
        print("1. Read shoes data")
        print("2. Capture shoes")
        print("3. View all Shoes")
        print("4. Restock Shoes")
        print("5. Get the highest quantity in stock for sale")
        print("6. Search Shoe")
        print("7. Get Total value of Stock")
        print("8. Quit")

        # get choice from user
        choice = int(input("Enter choice: "))

        # based on user choice call appropriate functions
        if choice == 1:
            read_shoes_data()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            view_all()
        elif choice == 4:
            re_stock()
        elif choice == 5:
            highest_qty()
        elif choice == 6:
            code = input("Enter code to be searched? ")
            print(str(search_shoe(code)))
        elif choice == 7:
            value_per_item()
        elif choice == 8:
            print("Thank you.")
            break
        else:
            print("Invalid choice")



# Country,Code,Product,Cost,Quantity
# South Africa,SKU44386,Air Max 90,2300,20
# China,SKU90000,Jordan 1,3200,50
# Vietnam,SKU63221,Blazer,1700,19
# United States,SKU29077,Cortez,970,60
# Russia,SKU89999,Air Force 1,2000,43
# Australia,SKU57443,Waffle Racer,2700,4
# Canada,SKU68677,Air Max 97,3600,13
# Egypt,SKU19888,Dunk SB,1500,26
# Britain,SKU76000,Kobe 4,3400,32
# France,SKU84500,Pegasus,2490,28
# Zimbabwe,SKU20207,Air Presto,2999,7
# Morocco,SKU77744,Challenge Court,1450,11
# Israel,SKU29888,Air Zoom Generation,2680,6
# Uganda,SKU33000,Flyknit Racer,4900,9
# Pakistan,SKU77999,Air Yeezy 2,4389,67
# Brazil,SKU44600,Air Jordan 11,3870,24
# Columbia,SKU87500,Air Huarache,2683,8
# India,SKU38773,Air Max 1,1900,29
# Vietnam,SKU95000,Air Mag,2000,2
# Israel,SKU79084,Air Foamposite,2430,4
# China,SKU93222,Air Stab,1630,10
# South Korea,SKU66734,Hyperdunk,1899,7
# Australia,SKU71827,Zoom Hyperfuse,1400,15
# France,SKU20394,Eric Koston 1,2322,17