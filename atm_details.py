import mysql.connector
import atm_access

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="atm_db"
)

mycursor = mydb.cursor()

print("***** Welcome to the  Deraz ATM System *****")
account_number = int(input("Enter your Account Number: "))
account_pin = int(input("Enter your PIN: "))
   
def main():
      #insert data
      sql = "INSERT INTO atm_maintenance (account_number, account_pin, balance, transactions) VALUES (%s,%s,%s,%s)"
      account_number = input("Enter The Account Number:")
      account_pin =input("Enter The Account Pin:")
      balance=input("Enter The Account Balance:")
      transactions=input("Enter The Account Transaction:")
      val = (account_number, account_pin, balance, transactions)
      mycursor.execute(sql, val)
      mydb.commit()
      print("  ******SUCCESSFULLY UPLOADED*****" )


#check balance

def check_balance():
        sql = "SELECT balance FROM atm_maintenance WHERE account_number = %s AND account_pin = %s"
        val = (account_number, account_pin)
        mycursor.execute(sql, val)
        account_balance = mycursor.fetchone()
        for i in account_balance:
            print(i)
        if  account_balance:
            print("Balance History:")
            print(account_balance[0])
        else:
            print("No transaction history found for this account.")
        var=input("Do You Want To Continue Press Yes: ")
        if var=="yes":
         atm_access.access_function()
        else:
            print(" *** Goodbye! Thank you for using the ATM *** ")

#withdrawal amount

def withdrawal_amount():
    # Get the withdrawal amount from the user
        withdrawal_amount = float(input("Enter the withdrawal amount: "))
        # Check if the account exists and retrieve the current balance
        sql = "SELECT balance FROM atm_maintenance WHERE account_number = %s"
        val = (account_number,)
        mycursor.execute(sql, val)
        account_balance = mycursor.fetchone()

        if account_balance and account_balance[0] >= withdrawal_amount:
            new_balance = account_balance[0] - withdrawal_amount

            # Update the account balance in the database
            sql = "UPDATE atm_maintenance SET balance = %s WHERE account_number = %s"
            val = (new_balance, account_number)
            mycursor.execute(sql, val)

            # Update the transaction history in the database
            transaction = f"Withdrawal of ${withdrawal_amount:.2f}"
            sql = "UPDATE atm_maintenance SET transactions = %s WHERE account_number = %s"
            val = (f"\n{transaction}", account_number)
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"Withdrawal successful. Remaining balance: ${new_balance:.2f}")
        else:
            print("Insufficient balance.")
        var=input("Do You Want To Continue Press Yes: ")
        if var=="yes":
            atm_access.access_function()
        else:
             print(" *** Goodbye! Thank you for using the ATM *** ")

    #deposit amount

def deposit_amount():
        deposit_amount = float(input("Enter the deposit amount: "))
        # Check if the account exists and retrieve the current balance
        sql = "SELECT balance FROM atm_maintenance WHERE account_number = %s"
        val = (account_number,)
        mycursor.execute(sql, val)
        account_balance = mycursor.fetchone()

        if account_balance:
            # Calculate the new balance after deposit
            new_balance = account_balance[0] + deposit_amount

            # Update the account balance in the database
            sql = "UPDATE atm_maintenance SET balance = %s WHERE account_number = %s"
            val = (new_balance, account_number)
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"Deposit successful. New balance: ${new_balance:}")
        else:
            print("Invalid account number. Please try again.")
        var=input("Do You Want To Continue Press Yes: ")
        if var=="yes":
         atm_access.access_function()
        else:
            print(" *** Goodbye! Thank you for using the ATM *** ")

#transaction detail

def view_transaction_history():
        sql = "SELECT transactions FROM atm_maintenance WHERE account_number = %s"
        val = (account_number,)
        mycursor.execute(sql, val)
        transaction_history = mycursor.fetchone()
        for i in transaction_history:
            print(i)
        if  transaction_history:
            print("Transaction History:")
            print(transaction_history[0])
        else:
            print("No transaction history found for this account.")
        var=input("Do You Want To Continue Press Yes: ")
        if var=="yes":
         atm_access.access_function()
        else:
            print(" *** Goodbye! Thank you for using the ATM *** ")

#change pin

def new_pin(): 
        
        new_pin = int(input("Enter your new PIN: "))
        # Update the PIN in the database
        sql = "UPDATE atm_maintenance SET account_pin = %s WHERE account_number = %s"
        val = (new_pin, account_number)
        mycursor.execute(sql, val)
        mydb.commit()
        print("*********** PIN changed successfully ********")
        var=input("Do You Want To Continue Press Yes: ")
        if var=="yes":
         atm_access.access_function()
        else:
            print(" *** Goodbye! Thank you for using the ATM *** ")
      
#exit
    
def exit():
    print(" *** Goodbye! Thank you for using the ATM ***")
    mydb.close()




