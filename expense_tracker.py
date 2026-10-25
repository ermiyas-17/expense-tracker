import json
import cowsay
def main():
    while True:
     print("===== EXPENSE TRACKER =====")
     print("1. Add expense")
     print("2. View all expenses")
     print("3. Search expenses by category")
     print("4. Delete an expense")
     print("5. Exit")

     choose = input("What would you like? ").strip().casefold()

     if choose == "1" or choose == "add expense":
        add_expense()
        break
     elif choose == "2" or choose == "view all expense":
        view_expense()
        break
     elif choose == "3" or choose == "search expense by category":
        search_expense()
        break
     elif choose == "4" or choose == "delete":
        delete()
        break
     elif choose == "5" or choose == "exit":
        cowsay.cow("Goodbye!")
        return
        break
     else:
        print("Invalid input. Please try again.")

def add_expense():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Enter a number.")

    catagory = input("Category: ")
    description = input("Description: ")

    expense = {
        "amount": amount,
        "catagory": catagory,
        "description": description
    }

    try:
        with open("expenses.json", "r") as file:
            ha = json.load(file)
    except FileNotFoundError:
        ha = []
    ha.append(expense)
    with open("expenses.json", "w") as file:
        json.dump(ha, file, indent=4)
    print("Successfully added!")

def view_expense():
  with open("expenses.json") as file:
    ha = json.load(file)
    if not ha:
     print("no expense found")
     return
    for trans in ha:
       print(f"amount = {trans['amount']}")
       print(f"catagory = {trans['catagory']}")

def search_expense():
  search = input("please input which catagory want to see  ").strip().casefold()
  with open("expenses.json") as file:
    ha = json.load(file)
    found = False
    for ser in ha:
      if search == ser['catagory']:
        print(f"amount: {ser['amount']}")
        print(f"catagory: {ser['catagory']}")
        found = True
    if not found:
        print("not found")

def delete():
    delete = input("Which category do you want to erase: ").strip()

    with open("expenses.json") as file:
        ha = json.load(file)

    original_length = len(ha)

    ha = [dele for dele in ha if dele["catagory"].lower() != delete.lower()]

    if len(ha) < original_length:
        with open("expenses.json", "w") as file:
            json.dump(ha, file, indent=4)
        print("Successfully deleted!")
    else:
        print("Catagory not found!")


main()
