def Reading_file():
    ID = 1
    file = open("Laptop.txt", "r")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("S.N.  \tLaptop Name         Company Name     Price      Quantity    Processor            Graphics")
    print("-----------------------------------------------------------------------------------------------------------------------")

    for line in file:
        data = line.strip().split(",")
        print(f"{ID}\t{data[0]:<20}{data[1]:<16}{data[2]:<12}{data[3]:<12}{data[4]:<20}{data[5]}")
        ID += 1
    file.close()

Reading_file()
