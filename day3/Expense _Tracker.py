# CLI Expense Tracker — add, delete, update, categorize
  
def add_expense(expense_id,amount, category, item):
    with open('expenses.csv', 'a') as f:
        f.write(f"{expense_id},{amount},{category},{item}\n")
print("Expense added successfully.")

def delete_expense(expense_id):
    with open('expenses.csv', 'r') as f:
        expenses = f.readlines()
    with open('expenses.csv', 'w') as f:
        for i, expense in enumerate(expenses):
            if i != expense_id:
                f.write(expense)
    print("Expense deleted successfully.")

def update_expense(expense_id, amount=None, category=None, date=None):
    with open('expenses.csv', 'r') as f:
        expenses = f.readlines()

    # Check if expense_id is valid
    if expense_id < 0 or expense_id >= len(expenses):
        print("Invalid expense ID.")
        return

    # Split the selected expense into parts
    parts = expenses[expense_id].strip().split(',')
    
    # Update fields if new values are provided
    if amount is not None:
        parts[0] = str(amount)
    if category is not None:
        parts[1] = category
    if item is not None:
        parts[2] = item

    # Join back and save
    expenses[expense_id] = ','.join(parts) + '\n'

    with open('expenses.csv', 'w') as f:
        f.writelines(expenses)

    print("Expense updated successfully.")




def view_expenses():
    with open('expenses.csv', 'r') as f:
        expense = f.readlines()
        finalreviw= list(expense)
    for e in finalreviw:
        print(e.strip())



import csv

while True:
    print("Welcome to the Expense Tracker!")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Update Expense")
    print("4. View Expenses")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        expense_id= int(input("Enter expense_id: "))
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        item = input("Enter item name: ")
        add_expense(expense_id,amount, category, item)

    elif choice == '2':
        expense_id = int(input("Enter expense ID to delete: "))
        delete_expense(expense_id)

    elif choice == '3':
        expense_id = int(input("Enter expense ID to update: "))

    # Ask for new values; leave blank if no change
        amount_input = input("Enter new amount (leave blank to keep same): ")
        category_input = input("Enter new category (leave blank to keep same): ")
        item_input = input("Enter new item (leave blank to keep same): ")

    # Convert amount to float if provided, else None
        amount = float(amount_input) if amount_input else None
        category = category_input if category_input else None
        item = item_input if item_input else None

    # Call update function
        update_expense(expense_id, amount, category, item)
       
    elif choice == '4':
        view_expenses()
    elif choice == '5':
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
