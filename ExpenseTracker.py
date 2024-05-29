expenses = {}  # Main data store for expenses (dictionary)
current_id = 0  # Counter for unique expense IDs

def add_expense():
  global current_id

  date = input("Enter expense date (YYYY-MM-DD): ")
  amount = float(input("Enter expense amount: "))
  category = input("Enter expense category: ")
  description = input("Enter expense description (optional): ")

  current_id += 1
  expense_data = {
    "id": current_id,
    "date": date,
    "amount": amount,
    "category": category,
    "description": description if description else ""
  }
  expenses[current_id] = expense_data
  print("Expense added successfully!")

def view_expenses():
  if not expenses:
    print("No expenses found.")
    return

  for expense_id, expense in expenses.items():
    print(f"\n** Expense ID: {expense_id} **")
    print(f"  Date: {expense['date']}")
    print(f"  Amount: {expense['amount']:.2f}")
    print(f"  Category: {expense['category']}")
    if expense["description"]:
      print(f"  Description: {expense['description']}")

def main():
  while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      add_expense()
    elif choice == '2':
      view_expenses()
    elif choice == '3':
      break
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()
