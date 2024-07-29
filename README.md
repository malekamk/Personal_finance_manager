# Personal Finance Manager

## Overview
This project is a Personal Finance Manager that allows users to add and categorize expenses, summarize expenses by category, generate expense reports, and visualize their spending habits.

## Features
- Add expenses with categories and descriptions.
- Summarize expenses by category and month.
- Generate detailed expense reports.
- Plot expenses by category.
- Simple command-line interface (CLI) for user interaction.

## Usage
1. Clone the repository.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the CLI:
    ```sh
    python cli.py
    ```

## Example
```python
from finance_manager import FinanceManager

manager = FinanceManager()
manager.add_expense(50, 'Food', 'Grocery shopping')
manager.add_expense(20, 'Entertainment', 'Movie ticket')
print(manager.generate_report())
manager.plot_expenses()
