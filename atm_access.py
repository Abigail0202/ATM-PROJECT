import atm_details

def access_function():
    print("Main Menu:")          
    print("1-> Check Balance")           
    print("2-> Withdraw Cash")           
    print("3-> Deposit Cash")
    print("4-> View Transaction History")
    print("5-> Change PIN")
    print("6-> Exit")
   
    option = int(input("Select an option: "))
    try:
        if option == 1:
            atm_details.check_balance()
        elif option == 2:
             atm_details.withdrawal_amount()
        elif option == 3:
             atm_details.deposit_amount()
        elif option == 4:
             atm_details.view_transaction_history()
        elif option == 5:
             atm_details.new_pin()
        elif option == 6:
             atm_details.exit()
        else:
            print(" Please Type 1, 2, 3, 4 ,5 or 6 only ")
    except ValueError:
        print("Type Number Only")

access_function()
