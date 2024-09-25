# -*- coding: utf-8 -*-
"""Python_for_Analytics_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Cveoc5GuhSmF6dtlVZmax3KSPO-G2K5v
"""

# Dictionary to store bank account details
accounts = {}

# Function to create a new bank account
def create_account():
    name = input("Enter account holder's name: ")
    account_number = input("Enter account number: ")
    while account_number in accounts:
        print("Account number already exists! Please enter a unique account number.")
        account_number = input("Enter account number: ")

    initial_balance = float(input("Enter initial balance: "))
    accounts[account_number] = {'name': name, 'balance': initial_balance}
    print(f"Account created successfully for {name} with account number {account_number}.")

# Function to deposit money into an account
def deposit(account_number, amount):
    if amount > 0:
        accounts[account_number]['balance'] += amount
        print(f"Deposit successful! New balance: {accounts[account_number]['balance']}")
    else:
        print("Deposit amount must be positive!")

# Function to withdraw money from an account
def withdraw(account_number, amount):
    if amount > 0:
        if accounts[account_number]['balance'] >= amount:
            accounts[account_number]['balance'] -= amount
            print(f"Withdrawal successful! New balance: {accounts[account_number]['balance']}")
        else:
            print("Insufficient balance!")
    else:
        print("Withdrawal amount must be positive!")

# Function to check balance
def check_balance(account_number):
    print(f"Account holder: {accounts[account_number]['name']}")
    print(f"Current balance: {accounts[account_number]['balance']}")

# Main program loop
def main():
    while True:
        print("\nBank Account Management System")
        print("1. Create new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_account()

        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                deposit(account_number, amount)
            else:
                print("Account not found!")

        elif choice == '3':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                withdraw(account_number, amount)
            else:
                print("Account not found!")

        elif choice == '4':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                check_balance(account_number)
            else:
                print("Account not found!")

        elif choice == '5':
            print("Thank you for using the Bank Account Management System!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

# Run the program
if __name__ == "__main__":
    main()