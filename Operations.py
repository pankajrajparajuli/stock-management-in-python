from datetime import datetime

# Making A dictionary to store the data of txt file
file = open("Laptop.txt","r")
laptop_dictionary = {}
laptop_id = 1
for line in file:
    line = line.replace("\n","")
    laptop_dictionary.update({laptop_id: line.split(", ")})
    laptop_id = laptop_id + 1
file.close()

def operation(user_input):
        # If the user wants to Buy from Manufacturer
        if user_input == 1:

            while True:
                from Reading import Reading_file
                try:
                    buying_laptop_id = int(input("Enter the ID of the Laptop you want to purchase : "))
                    buying_laptop_qty = int(input("Enter the quantity of the Laptop you want to purchase : "))

                    if buying_laptop_id in laptop_dictionary:

                        from Writing import update_when_buying
                        update_when_buying(buying_laptop_id,buying_laptop_qty)
                        break

                    else:
                        Reading_file()
                        print("----------------------------------------------------------------------------------------")
                        print("Sorry the ID you entered is not present")
                        print("Please read the list of laptops properly and enter again")
                        print("----------------------------------------------------------------------------------------")

                except ValueError:
                    print("----------------------------------------------------------------------------------------")
                    print("(Invalid Input) Please Enter in int format only")
                    print("----------------------------------------------------------------------------------------")

        # If the user wants to sell to the Customer
        elif user_input == 2:
            # Showing User the list of available laptops to sell


            while True:
                from Reading import Reading_file

                try:
                    # Asking the user for inputs to Determine what and how many laptos he wants to sell to his customers and the details of the customer

                    selling_laptop_id = int(input("Please Enter the ID of the Laptop you want to sell : "))
                    selling_laptop_qty = int(input("Please Enter the number of Laptops you want to sell : "))
                    buyer_name = input("Please Enter the name of the Customer : ")
                    buyer_number = int(input("Please Enter the phone number of the buyer : "))

                    if selling_laptop_id in laptop_dictionary:

                        if selling_laptop_qty <= int(laptop_dictionary[selling_laptop_id][3]) and selling_laptop_qty > 0 :

                            from Writing import update_when_selling
                            update_when_selling(selling_laptop_id,selling_laptop_qty,buyer_name,buyer_number)
                            break

                        else:
                            Reading_file()
                            print("Quantity not available")
                            print("Please read the list properly and enter the Available ID and Quantity only")

                    else:
                        print("----------------------------------------------------------------------------------------")
                        print("Sorry,ID you entered is wrong ")
                        print("-----------------------------------------------------------------------------------------")
                        Reading_file()
                        print("Please read the list properly and enter the Available ID and Quantity only")


                except:
                    print("________________________________________________________________________")
                    print("(Invalid Input) Please Enter in int format only")
                    print("________________________________________________________________________")


        else:
            print("Invali Input")

