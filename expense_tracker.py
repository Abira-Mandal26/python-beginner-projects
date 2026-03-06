import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


# Add expense
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, etc): ")
    note = input("Enter note: ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])

    print("Expense added successfully!")


# Show monthly report
def monthly_report():
    month = input("Enter month (YYYY-MM): ")

    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                date, amount, category, note = row

                if date.startswith(month):
                    print(f"{date} | {category} | ₹{amount} | {note}")
                    total += float(amount)

        print("\nTotal spending:", total)

    except FileNotFoundError:
        print("No expenses recorded yet.")


# Menu
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Monthly Report")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        monthly_report()

    elif choice == "3":
        break

    else:
        print("Invalid choice")