
class Banker:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Customer:
    def __init__(self, username, password, balance=0.0):
        self.username = username
        self.password = password
        self.balance = balance


# In-memory storage for bankers and customers
bankers = {}
customers = {}

def register_user(user_type):
    username = input(f"Enter {user_type} username: ")
    password = input(f"Enter {user_type} password: ")
    
    if user_type == 'banker':
        if username in bankers:
            print("Banker already exists!")
        else:
            bankers[username] = Banker(username, password)
            print("Banker registered successfully!")
    elif user_type == 'customer':
        if username in customers:
            print("Customer already exists!")
        else:
            customers[username] = Customer(username, password)
            print("Customer registered successfully!")

def login_user(user_type):
    username = input(f"Enter {user_type} username: ")
    password = input(f"Enter {user_type} password: ")
    
    if user_type == 'banker':
        user = bankers.get(username)
    elif user_type == 'customer':
        user = customers.get(username)
    
    if user and user.password == password:
        print(f"{user_type.capitalize()} logged in successfully!")
        return user
    else:
        print("Invalid credentials!")
        return None

def update_customer():
    username = input("Enter customer username to update: ")
    if username in customers:
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        customers[username].username = new_username
        customers[username].password = new_password
        print("Customer updated successfully!")
    else:
        print("Customer not found!")

def view_all_customers():
    print("All Customers:")
    for username, customer in customers.items():
        print(f"Username: {username}, Balance: {customer.balance}")

def delete_customer():
    username = input("Enter customer username to delete: ")
    if username in customers:
        del customers[username]
        print("Customer deleted successfully!")
    else:
        print("Customer not found!")

def withdraw_amount(customer):
    amount = float(input("Enter amount to withdraw: "))
    if customer.balance >= amount:
        customer.balance -= amount
        print("Amount withdrawn successfully!")
    else:
        print("Insufficient balance!")

def deposit_amount(customer):
    amount = float(input("Enter amount to deposit: "))
    customer.balance += amount
    print("Amount deposited successfully!")

def view_balance(customer):
    print(f"Your balance is: {customer.balance}")

def main():
    while True:
        print("\nBanking Application")
        print("1. Banker Register")
        print("2. Banker Login")
        print("3. Customer Register")
        print("4. Customer Login")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register_user('banker')
        elif choice == '2':
            banker = login_user('banker')
            if banker:
                while True:
                    print("\nBanker Menu")
                    print("1. Update Customer")
                    print("2. View All Customers")
                    print("3. Delete Customer")
                    print("4. Logout")
                    
                    banker_choice = input("Enter your choice: ")
                    
                    if banker_choice == '1':
                        update_customer()
                    elif banker_choice == '2':
                        view_all_customers()
                    elif banker_choice == '3':
                        delete_customer()
                    elif banker_choice == '4':
                        break
        elif choice == '3':
            register_user('customer')
        elif choice == '4':
            customer = login_user('customer')
            if customer:
                while True:
                    print("\nCustomer Menu")
                    print("1. Withdraw Amount")
                    print("2. Deposit Amount")
                    print("3. View Balance")
                    print("4. Logout")
                    
                    customer_choice = input("Enter your choice: ")
                    
                    if customer_choice == '1':
                        withdraw_amount(customer)
                    elif customer_choice == '2':
                        deposit_amount(customer)
                    elif customer_choice == '3':
                        view_balance(customer)
                    elif customer_choice == '4':
                        break
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
