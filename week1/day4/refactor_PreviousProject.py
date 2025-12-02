import csv
import os

class ExpenseTracker:
     def add_expense(self, expense_id, amount, category, item):
      with open('expenses.csv', 'a') as f:
        f.write(f"{expense_id},{amount},{category},{item}\n")
     print("Expense added successfully.")

     def delete_expense(self, expense_id):
       with open('expenses.csv', 'r') as f:
        expenses = f.readlines()
        new_expenses = [line for line in expenses if line.split(',')[0] != str(expense_id)]
        if len(new_expenses) == len(expenses):
          print("Expense ID not found.")
          return
        with open('expenses.csv', 'w') as f:
          f.writelines(new_expenses)
        print("Expense deleted successfully.")

     def update_expense(self, expense_id, amount=None, category=None, item=None):
       updated = False
       with open('expenses.csv', 'r') as f:
        expenses = f.readlines()

       for i, line in enumerate(expenses):
        parts = line.strip().split(',')
        if parts[0] == str(expense_id):
            if amount is not None:
                parts[1] = str(amount)
            if category is not None:
                parts[2] = category
            if item is not None:
                parts[3] = item
            expenses[i] = ','.join(parts) + '\n'
            updated = True
            break

        if not updated:
         print("Expense ID not found.")
         return

        with open('expenses.csv', 'w') as f:
          f.writelines(expenses)
        print("Expense updated successfully.")

     def view_expenses(self):
      with open('expenses.csv', 'r') as f:
        expense = f.readlines()
        finalreviw= list(expense)
      for e in finalreviw:
        print(e.strip())


if __name__ == "__main__":
   tracker = ExpenseTracker()
   while True:
    print("\nWelcome to the Expense Tracker!")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Update Expense")
    print("4. View Expenses")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        expense_id = input("Enter expense_id: ")
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        item = input("Enter item name: ")
        tracker.add_expense(expense_id, amount, category, item)

    elif choice == '2':
        expense_id = input("Enter expense ID to delete: ")
        tracker.delete_expense(expense_id)

    elif choice == '3':
        expense_id = input("Enter expense ID to update: ")
        amount_input = input("Enter new amount (leave blank to keep same): ")
        category_input = input("Enter new category (leave blank to keep same): ")
        item_input = input("Enter new item (leave blank to keep same): ")

        amount = float(amount_input) if amount_input else None
        category = category_input if category_input else None
        item = item_input if item_input else None

        tracker.update_expense(expense_id, amount, category, item)

    elif choice == '4':
        tracker.view_expenses()

    elif choice == '5':
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

