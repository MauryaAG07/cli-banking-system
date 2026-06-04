# Python Banking Program
# split into 3 parts
# show balance, deposit, withdraw.
import time # using time to make output more readable - not meant for speed
def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")
def deposit():
    running_deposit = True
    while True:
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Please enter a number above 0")
            else:
                print(f"You have deposited ${amount:.2f}")
                return amount
        except ValueError:
            print("Please enter a number above 0")
    return None
def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds")

            elif amount <= 0:
                print("Please enter a number above 0")

            else:
                print(f"You have withdrawn ${amount:.2f}")
                return amount
        except ValueError:
            print("Please enter a number above 0")
    return None
def main():
    balance = 0
    is_running = True
    while is_running:
        print("#############################")
        print("     Welcome to the Bank     ")
        print("#############################")
        print("Banking Options:")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print()
        choice = (input("Enter your choice, 1-3, or press 4 to Exit: "))
        if choice == "1":
            show_balance(balance)
            time.sleep(0.5)
            print("Back to menu...")
            time.sleep(3)
        elif choice == "2":
            balance += deposit()
            time.sleep(1)
            show_balance(balance)
            time.sleep(0.5)
            print("Back to menu...")
            time.sleep(3)
        elif choice == "3":
            balance -= withdraw(balance)
            time.sleep(1)
            show_balance(balance)
            time.sleep(0.5)
            print("Back to menu...")
            time.sleep(3) # three different time sleeps used, all consistent to what they impede. time.sleep to menu is longer
                          # because the menu will move the output out of frame. time.sleep gives enough time to read
        elif choice == "4":
            is_running = False
        else:
            print("Please enter a valid choice")
            time.sleep(3)
    print("Thank you, have a nice day!")
if __name__ == "__main__":
    main()
