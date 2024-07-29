# Personal Finance Manager

## Overview

Personal Finance Manager is a command-line application that helps you track, manage, and visualize your expenses. It allows you to add expenses, generate reports, view monthly summaries, and plot expense data. This tool is designed to help you manage your finances effectively by providing insightful summaries and visualizations of your spending patterns.

![Expense Visualization](expenses_by_category.png)  <!-- Image added here -->

## Features

- **Add Expense**: Record your expenses with details like amount, category, and description.
- **Generate Report**: Create a detailed report of your expenses by category.
- **Monthly Summary**: View a summary of expenses broken down by month and category.
- **Plot Expenses**: Visualize your expenses with a bar chart, saved as a PNG image file using the `GTK3Agg` backend.

## Getting Started

To get started with the Personal Finance Manager, follow these steps:

### Prerequisites

- Python 3.x
- `matplotlib` library
- `json` library (included with Python standard library)

### Installation

1. **Clone the Repository:**

git clone https://github.com/malekamk/Personal_finance_manager.git



### Example

Here’s an example of how to add expenses and generate a report:

```python
from finance_manager import FinanceManager

manager = FinanceManager()
manager.add_expense(1200, 'Food', 'Grocery shopping')
manager.add_expense(3000, 'Garments', 'sneakers')
print(manager.generate_report())
manager.plot_expenses()
