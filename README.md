
# 📈 Stock Portfolio Tracker Using Python

## Project Overview

The Stock Portfolio Tracker is a simple Python application that calculates the total investment value of a stock portfolio using predefined stock prices.

Users can enter stock symbols and quantities, view the value of each stock, and calculate the total investment. The application also provides an option to save the portfolio summary to a text file.

This project was developed as part of the CodeAlpha Python Programming Internship.

## Features

- Predefined stock prices stored in a Python dictionary.
- Accepts stock symbols and quantities from the user.
- Calculates the value of each stock.
- Calculates the total portfolio investment.
- Validates stock symbols and quantities.
- Supports adding multiple stocks.
- Option to save the portfolio summary to a text file.
- Simple and user-friendly console interface.

## Technologies Used

- Python 3
- Dictionaries
- Loops and conditional statements
- User input and output
- Basic arithmetic operations
- File handling

## Project Structure

```text
CodeAlpha_StockPortfolioTracker/
│
├── stock_portfolio.py
└── README.md
```

## Stock Prices

The application uses the following sample prices:

| Stock Symbol | Sample Price |
|---|---:|
| AAPL | $180 |
| TSLA | $250 |
| GOOGL | $140 |
| MSFT | $420 |
| AMZN | $190 |

Note: These prices are hardcoded examples for educational purposes and do not represent live market prices.

## Requirements

- Python 3.x
- Any Python-compatible code editor or terminal.

No external libraries are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:

   ```bash
   python stock_portfolio.py
   ```

4. Enter the stock symbol and quantity when prompted.
5. Type `done` to finish entering stocks.
6. View the portfolio summary and choose whether to save it.

## Example

```text
STOCK PORTFOLIO TRACKER

AAPL: $180.00
TSLA: $250.00
GOOGL: $140.00
MSFT: $420.00
AMZN: $190.00

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity: 5

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity: 2

Enter stock symbol (or 'done' to finish): done

PORTFOLIO SUMMARY

Stock     Quantity  Price     Value
AAPL      5         $180.00   $900.00
TSLA      2         $250.00   $500.00

Total Investment: $1400.00
```

## Learning Outcomes

Through this project, I practiced:

- Creating and accessing dictionaries.
- Accepting and validating user input.
- Using loops and conditional statements.
- Performing calculations using stock prices and quantities.
- Handling files in Python.
- Organizing and presenting calculated results.

## Author

Name: YOUR NAME

## Internship

Organization: CodeAlpha

Domain: Python Programming

Task: Stock Portfolio Tracker

