class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"Description: {self.description}\nAmount: ${self.amount:.2f}\nCategory: {self.category}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def display_menu(self):
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Filter by Category")
        print("5. Exit")

    def add_expense(self):
        description = input("Enter description of the expense: ")
        amount = float(input("Enter amount of the expense: "))
        category = input("Enter category of the expense: ")

        expense = Expense(description, amount, category)
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
        else:
            print("\nAll Expenses:")
            for idx, expense in enumerate(self.expenses, start=1):
                print(f"{idx}. {expense}")

    def calculate_total(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

    def filter_by_category(self):
        category = input("Enter the category to filter by: ")
        filtered_expenses = [
            expense
            for expense in self.expenses
            if expense.category.lower() == category.lower()
        ]

        if not filtered_expenses:
            print(f"No expenses found for the '{category}' category.")
        else:
            print(f"\nExpenses for the '{category}' category:")
            for idx, expense in enumerate(filtered_expenses, start=1):
                print(f"{idx}. {expense}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.calculate_total()
            elif choice == "4":
                self.filter_by_category()
            elif choice == "5":
                print(
                    "Thank you for using Personal Expense Tracker!\nExiting the program...\nGoodbye!"
                )
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
