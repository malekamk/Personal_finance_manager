import json
from datetime import datetime
from collections import defaultdict
import matplotlib
matplotlib.use('GTK3Agg')  # Set the backend to GTK3Agg for rendering
import matplotlib.pyplot as plt

class FinanceManager:
    """
    A class to manage personal finances, including adding expenses, 
    summarizing them, generating reports, and plotting expense categories.
    """
    def __init__(self, data_file='expenses.json'):
        """
        Initializes the FinanceManager with the given data file.

        Args:
            data_file (str): Path to the JSON file where expenses are stored.
        """
        self.data_file = data_file
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """
        Loads expenses from the JSON file into the expenses list.
        """
        try:
            with open(self.data_file, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        """
        Saves the current expenses to the JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description=''):
        """
        Adds a new expense to the list and saves it to the JSON file.

        Args:
            amount (float): The amount of the expense.
            category (str): The category of the expense.
            description (str): A description of the expense (optional).
        """
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.expenses.append(expense)
        self.save_expenses()

    def summarize_expenses(self):
        """
        Summarizes expenses by category.

        Returns:
            dict: A dictionary with categories as keys and total amounts as values.
        """
        summary = defaultdict(float)
        for expense in self.expenses:
            summary[expense['category']] += expense['amount']
        return dict(summary)

    def generate_report(self):
        """
        Generates a text report of the summarized expenses.

        Returns:
            str: A formatted string containing the expense report.
        """
        summary = self.summarize_expenses()
        report = "Expense Report\n"
        report += "--------------\n"
        total = 0
        for category, amount in summary.items():
            report += f"{category}: ${amount:.2f}\n"
            total += amount
        report += "--------------\n"
        report += f"Total: ${total:.2f}\n"
        return report

    def generate_monthly_summary(self):
        """
        Generates a monthly summary of expenses.

        Returns:
            dict: A nested dictionary with months as keys and categories as sub-keys.
        """
        monthly_summary = defaultdict(lambda: defaultdict(float))
        for expense in self.expenses:
            date = datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S')
            month_year = date.strftime('%Y-%m')
            monthly_summary[month_year][expense['category']] += expense['amount']
        return dict(monthly_summary)

    def plot_expenses(self):
        """
        Plots the expenses by category and saves the plot as an image file.
        """
        summary = self.summarize_expenses()
        categories = list(summary.keys())
        amounts = list(summary.values())

        plt.figure(figsize=(10, 5))
        plt.bar(categories, amounts, color='skyblue')
        plt.xlabel('Category')
        plt.ylabel('Amount ($)')
        plt.title('Expenses by Category')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('expenses_by_category.png')
        plt.show()

if __name__ == '__main__':
    manager = FinanceManager()
    manager.add_expense(50, 'Food', 'Grocery shopping')
    manager.add_expense(20, 'Entertainment', 'Movie ticket')
    print(manager.generate_report())
    manager.plot_expenses()

