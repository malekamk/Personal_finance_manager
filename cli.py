import sys
from finance_manager import FinanceManager

def main():
    """
    Main function to run the Personal Finance Manager CLI.
    Provides options to add expenses, generate reports, view monthly summaries, plot expenses, or exit the application.
    """
    manager = FinanceManager()

    while True:
        print("\nPersonal Finance Manager")
        print("1. Add Expense")
        print("2. Generate Report")
        print("3. Monthly Summary")
        print("4. Plot Expenses")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")
                manager.add_expense(amount, category, description)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == '2':
            print("\n" + manager.generate_report())
        elif choice == '3':
            summary = manager.generate_monthly_summary()
            for month, categories in summary.items():
                print(f"\n{month}")
                for category, amount in categories.items():
                    print(f"  {category}: ${amount:.2f}")
        elif choice == '4':
            manager.plot_expenses()
            print("Expense plot saved as 'expenses_by_category.png'.")
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

