from datetime import datetime

# Making A dictionary to store the data of txt file
file = open("Laptop.txt", "r")
laptop_dictionary = {}
laptop_id = 1
for line in file:
    line = line.replace("\n", "")
    laptop_dictionary.update({laptop_id: line.split(", ")})
    laptop_id = laptop_id + 1
file.close()


# Updating the Laptop txt file's quantity when Buying
def update_when_buying(buying_laptop_id, buying_laptop_qty):
    # ------------- Taking users input and storing the details in variables ------------------------
    laptop_name = laptop_dictionary[buying_laptop_id][0]
    laptop_brand = laptop_dictionary[buying_laptop_id][1]
    price = laptop_dictionary[buying_laptop_id][2].replace("$", "")
    processor = laptop_dictionary[buying_laptop_id][4]
    gpu = laptop_dictionary[buying_laptop_id][5]
    net_amount = int(price) * buying_laptop_qty
    pur_datetime = datetime.now()
    vat = (13 / 100) * net_amount
    total_amount = net_amount + vat

    laptop_dictionary[buying_laptop_id][3] = int(laptop_dictionary[buying_laptop_id][3]) + int(buying_laptop_qty)
    file = open("Laptop.txt", "w")
    for values in laptop_dictionary.values():
        file.write(str(values[0]) + ", " + str(values[1]) + ", " + str(values[2]) + ", " + str(values[3]) + ", " + str(
            values[4]) + ", " + str(values[5]))
        file.write("\n")
    file.close()

    # Printing the purchase details of the shop from manufacturer
    print("----------------------------------------------------------------------------------------------")
    print("OK here is the details of your purchase from the manufacturer " + str(laptop_brand))
    print("----------------------------------------------------------------------------------------------")
    print("Purchase time   :", pur_datetime)
    print("Laptop Brand    : ", laptop_brand)
    print("Laptop Model    : ", laptop_name)
    print("Processor       : ", processor)
    print("Graphics        : ", gpu)
    print("Price           : $" + price)
    print("Purchased units : ", buying_laptop_qty)
    print("Net Amount      : $" + str(net_amount))
    print("Vat amount      : $" + str(vat))
    print("Total Amount    : $" + str(total_amount))

    buy_bill = open( "buying" + ".txt", "w")
    buy_bill.write("----------------------------------------------------------------------------------------------")
    buy_bill.write("\n")
    buy_bill.write("OK here is the details of your purchase from the manufacturer " + str(laptop_brand))
    buy_bill.write("\n")
    buy_bill.write("----------------------------------------------------------------------------------------------")
    buy_bill.write("\n")
    buy_bill.write("Purchase time   :"+ str(pur_datetime))
    buy_bill.write("\n")
    buy_bill.write("Laptop Brand    : "+ str(laptop_brand))
    buy_bill.write("\n")
    buy_bill.write("Laptop Model    : "+ str(laptop_name))
    buy_bill.write("\n")
    buy_bill.write("Processor       : "+ str(processor))
    buy_bill.write("\n")
    buy_bill.write("Graphics        : "+ str(gpu))
    buy_bill.write("\n")
    buy_bill.write("Price           : $" + str(price))
    buy_bill.write("\n")
    buy_bill.write("Purchased units : "+ str(buying_laptop_qty))
    buy_bill.write("\n")
    buy_bill.write("Net Amount      : $" + str(net_amount))
    buy_bill.write("\n")
    buy_bill.write("Vat amount      : $" + str(vat))
    buy_bill.write("\n")
    buy_bill.write("Total Amount    : $" + str(total_amount))

    buy_bill.close()


# Updating the Laptop txt file when selling to customer and creating a txt file that stores the bill
def update_when_selling(selling_laptop_id, selling_laptop_qty, buyer_name, buyer_number):
    # Updating the Laptop dictionary

    laptop_dictionary[selling_laptop_id][3] = int(laptop_dictionary[selling_laptop_id][3]) - int(selling_laptop_qty)

    # Updating txt file
    file = open("Laptop.txt", "w")
    for values in laptop_dictionary.values():
        file.write(str(values[0]) + ", " + str(values[1]) + ", " + str(values[2]) + ", " + str(values[3]) + ", " + str(
            values[4]) + ", " + str(values[5]))
        file.write("\n")
    file.close()

    # For shipping
    shipping_input = input("Do you want to add shipping charge your laptop (Y/N) : ")
    if shipping_input.lower() == 'y':
        shipping_charge = 5

    elif shipping_input.lower() == 'n':
        shipping_charge = 0

    else:
        print("Invalid Input")

    # Taking users input and storing the details in variables

    laptop_name = laptop_dictionary[selling_laptop_id][0]
    laptop_brand = laptop_dictionary[selling_laptop_id][1]
    price = laptop_dictionary[selling_laptop_id][2].replace("$", "")
    processor = laptop_dictionary[selling_laptop_id][4]
    gpu = laptop_dictionary[selling_laptop_id][5]
    total_shipping = shipping_charge * selling_laptop_qty
    total_price = (int(price) * selling_laptop_qty) + total_shipping
    purchase_datetime = datetime.now()

    # Creating a new txt file that stores the bill

    bill_txt = open(str(buyer_name) + str(buyer_number) + ".txt", "w")

    bill_txt.write("----------------------------------------------------------------------------------------------")
    bill_txt.write("\n")
    bill_txt.write("OK here is the bill for " + str(buyer_name) + "| phone number:" + str(buyer_number))
    bill_txt.write("\n")
    bill_txt.write("----------------------------------------------------------------------------------------------")
    bill_txt.write("\n")
    bill_txt.write("Purchase time   :" + str(purchase_datetime))
    bill_txt.write("\n")
    bill_txt.write("Laptop Brand    : " + str(laptop_brand))
    bill_txt.write("\n")
    bill_txt.write("Laptop Model    : " + str(laptop_name))
    bill_txt.write("\n")
    bill_txt.write("Processor       : " + str(processor))
    bill_txt.write("\n")
    bill_txt.write("Graphics        : " + str(gpu))
    bill_txt.write("\n")
    bill_txt.write("Price           : $" + str(price))
    bill_txt.write("\n")
    bill_txt.write("Purchased units : " + str(selling_laptop_qty))
    bill_txt.write("\n")
    bill_txt.write("Shipping cost   : $" + str(total_shipping))
    bill_txt.write("\n")
    bill_txt.write("Total Amount    : $" + str(total_price))
    bill_txt.write("\n")

    bill_txt.close()

    # Printing the bill that has details of the sale made to the customer
    print("----------------------------------------------------------------------------------------------")
    print("OK here is the bill for ", buyer_name, "| phone number:", buyer_number)
    print("----------------------------------------------------------------------------------------------")

    print("Purchase time   :", purchase_datetime)
    print("Laptop Brand    : ", laptop_brand)
    print("Laptop Model    : ", laptop_name)
    print("Processor       : ", processor)
    print("Graphics        : ", gpu)
    print("Price           : $" + str(price))
    print("Purchased units : ", selling_laptop_qty)
    print("Shipping cost   : $" + str(total_shipping))
    print("Total Amount    : $" + str(total_price))
