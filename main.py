from datetime import datetime
# Welcoming The User
print("\t \t \t ╔╦╦╦═╦╗╔═╦═╦══╦═╗")
print("\t \t \t ║║║║╩╣╚╣═╣║║║║║╩╣")
print("\t \t \t ╚══╩═╩═╩═╩═╩╩╩╩═╝")

print("----------------------------------------------------------------------------")
print("Welcome to the System. I hope you're doing well")
print("So what would you like do to")
print("----------------------------------------------------------------------------")

while True:
    # Creating a function
    def main():
        print("1. Buy from Manufacturer.")
        print("2. Sell to Customer.")
        print("3. Exit the System.")
        print("________________________________________________________________________")

        while True:

            try:
                user_input = int(input("Enter the option to Continue : "))

                if user_input == 1:
                    from Operations import operation
                    operation(user_input)
                    break

                elif user_input == 2:
                    from Operations import operation
                    operation(user_input)
                    break

                elif user_input == 3:
                    print("Thank you fore using the System , Have a good day")
                    break

                else:
                    print("Please Enter number 1 or 2 or 3 only")
                    print("________________________________________________________________________")

            except:
                print("________________________________________________________________________")
                print("(Invalid Input) Please Enter number 1 or 2 or 3 only")
                print("________________________________________________________________________")

    print(main())

    again = input("Do yo want to Buy or Sell again (Y/N) : ")
    if again.lower() == 'n':
        print("Thank you for using our system. Good Bye")
        break
