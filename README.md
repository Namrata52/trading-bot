# Binance Futures Testnet Trading Bot

A Python command-line application that places **Market** and **Limit** orders on the **Binance USDT-M Futures Testnet**. The application is built with a clean, modular structure and includes input validation, logging, and exception handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL orders
- Command-line interface (CLI) using argparse
- Input validation
- API request and response logging
- Error handling for invalid input and API failures
- Modular project structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading_bot.log
│
├── main.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet Account
- Binance Testnet API Key
- Binance Testnet Secret Key

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Namrata52/trading-bot.git
cd trading-bot
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=your_binance_api_key
API_SECRET=your_binance_api_secret
BASE_URL=https://testnet.binancefuture.com
```

---

## Running the Application

### Market Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### Limit Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 90000
```

---

## Example Output

```
========================================
ORDER SUMMARY
========================================
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.002
========================================

ORDER PLACED SUCCESSFULLY

Order ID         : 123456789
Status           : FILLED
Executed Qty     : 0.002
```

---

## Logging

All API requests, responses, and errors are recorded in:

```
logs/trading_bot.log
```

---

## Validation

The application validates:

- Trading symbol
- BUY / SELL side
- MARKET / LIMIT order type
- Positive quantity
- Price required for LIMIT orders
- Price not allowed for MARKET orders

---

## Error Handling

The application handles:

- Invalid CLI input
- Validation errors
- Binance API errors
- Network exceptions

---

## Assumptions

- The application uses the Binance USDT-M Futures Testnet.
- Users must provide valid API credentials.
- The order quantity should satisfy Binance's minimum notional requirements.
- Internet connectivity is required for API communication.

---

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- argparse
- logging
