# CodeAlpha Stock Portfolio Tracker

## 📌 Project Description

This project is a console-based Stock Portfolio Tracker developed in Python as part of the CodeAlpha Python Programming Internship.

The program allows users to select stocks, enter quantities, calculate individual investment values, add multiple stocks to a portfolio, calculate the total investment, and save the portfolio details to a text file.

The investment is calculated using:

Investment = Stock Price × Quantity

---

## 🚀 Features

- Displays available stocks and their prices.
- Accepts stock name from the user.
- Accepts the quantity of shares.
- Validates stock names.
- Validates stock quantities.
- Handles non-numeric quantity input.
- Prevents zero or negative quantities.
- Calculates individual investment value.
- Allows multiple stocks to be added to the portfolio.
- Stores stock, quantity, price, and investment details.
- Displays a complete portfolio summary.
- Calculates total portfolio investment.
- Validates yes/no input when adding another stock.
- Saves portfolio details to portfolio.txt.

---

## 🛠️ Technologies Used

- Python
- Dictionaries
- Lists
- Tuples
- input() and print()
- Conditional statements
- while and for loops
- try-except exception handling
- Arithmetic operations
- File handling
- String methods

---

## 📂 Project Structure

CodeAlpha_StockPortfolio/
│
├── stock_portfolio.py
├── portfolio.txt
└── README.md

---

## 💻 Available Stocks

The program currently contains the following sample stock prices:

| Stock | Price |
|-------|------:|
| AAPL  | $180  |
| TSLA  | $250  |
| GOOGL | $150  |
| AMZN  | $180  |
| MSFT  | $420  |

These are sample/static prices used for the internship project and are not live market prices.

---

## ▶️ How to Run

### 1. Open the project folder

Open the project folder in VS Code or a terminal.

### 2. Run the Python program

python stock_portfolio.py

### 3. Follow the instructions

Enter the stock name and quantity when prompted.

The program will calculate the investment and allow you to add another stock.

---

## 🧮 Example

===================================
      STOCK PORTFOLIO TRACKER
===================================

Available Stocks:
AAPL → $ 180
TSLA → $ 250
GOOGL → $ 150
AMZN → $ 180
MSFT → $ 420

Enter stock name: AAPL
Stock found!
Enter quantity: 5

Investment value: $ 900

Do you want to add another stock? (yes/no): yes

Enter stock name: TSLA
Stock found!
Enter quantity: 2

Investment value: $ 500

Do you want to add another stock? (yes/no): no

=============================================
           PORTFOLIO SUMMARY
=============================================

Stock   Quantity   Price   Value
AAPL    5          $180    $900
TSLA    2          $250    $500

Total Investment: $ 1400
=============================================

---

## ⚠️ Input Validation

The program handles different invalid inputs.

### Invalid Stock

Enter stock name: ABC

Stock not found.

### Invalid Quantity

Enter quantity: abc

Please enter a valid number.

### Zero or Negative Quantity

Enter quantity: -5

Quantity must be greater than 0.

### Invalid Yes/No Input

Do you want to add another stock? (yes/no): maybe

Please enter yes or no.

---

## 💾 File Handling

The program saves the portfolio information in portfolio.txt.

The saved file contains:

- Stock name
- Quantity
- Stock price
- Individual investment value
- Total investment

### Example

STOCK PORTFOLIO
====================

Stock   Quantity   Price   Value
--------------------------------
AAPL    5          $180    $900
TSLA    2          $250    $500

Total Investment: $1400

This allows the portfolio information to remain available after the program is closed.

---

## 📚 Concepts Used

This project demonstrates basic Python programming concepts such as:

- Variables
- Dictionaries
- Lists
- Tuples
- User input
- String methods
- Conditional statements
- for loops
- while loops
- Exception handling
- Arithmetic operations
- Type conversion
- File handling

---

## 🎯 Learning Objectives

Through this project, I practiced:

- Working with Python dictionaries.
- Taking and validating user input.
- Performing calculations using stored data.
- Working with lists and tuples.
- Using loops and conditional statements.
- Handling errors using try-except.
- Building a console-based application.
- Storing data in a text file.
- Creating a portfolio summary.

---

## 🔮 Future Enhancements

The project can be improved in the future by adding:

- Buy and sell functionality.
- Profit and loss calculation.
- Portfolio editing and deletion.
- Live stock prices using an API.
- Portfolio history.
- Database storage.
- Graphical user interface.
- More advanced portfolio analytics.

---

## 👩‍💻 Internship

Developed as part of the CodeAlpha Python Programming Internship.

Task: Stock Portfolio Tracker

Language: Python

Project Type: Console-Based Application

---

## 📄 License

This project is created for educational and internship purposes.