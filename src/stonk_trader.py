import os
import requests
import json

# Set up the Robinhood API client
def get_client():
  # Get the Robinhood account credentials from environment variables
  username = os.environ["ROBINHOOD_USERNAME"]
  password = os.environ["ROBINHOOD_PASSWORD"]

  # Authenticate with the Robinhood API
  auth_response = requests.post(
      "https://api.robinhood.com/api-token-auth/",
      data={"username": username, "password": password}
  )
  auth_response.raise_for_status()
  access_token = auth_response.json()["token"]

  # Create the API client
  client = requests.Session()
  client.headers = {
      "Authorization": f"Bearer {access_token}",
  }
  return client

# Get the current price of a stock
def get_price(client, stock):
  response = client.get(
      f"https://api.robinhood.com/quotes/{stock}/",
  )
  response.raise_for_status()
  return float(response.json()["last_trade_price"])

# Get the median price of a stock over the past 2 years
def get_median_price(client, stock):
  response = client.get(
      f"https://api.robinhood.com/historicals/{stock}/?bounds=2_YEAR&interval=day",
  )
  response.raise_for_status()
  prices = [day["close_price"] for day in response.json()["historicals"]]
  return float(median(prices))

# Buy shares of a stock
def buy_shares(client, stock, quantity, price):
  # Get the account URL and instrument URL from environment variables
  account_url = os.environ["ROBINHOOD_ACCOUNT_URL"]
  instrument_url = os.environ["ROBINHOOD_INSTRUMENT_URL"]

  data = {
      "account": account_url,
      "instrument": instrument_url,
      "price": str(price),
      "symbol": stock,
      "type": "market",
      "time_in_force": "gtc",
      "trigger": "immediate",
      "side": "buy",
      "quantity": str(quantity),
  }
  response = client.post(
      "https://api.robinhood.com/orders/",
      data=data,
  )
  response.raise_for_status()
  return response.json()

# Sell shares of a stock
def sell_shares(client, stock, quantity, price):
  # Get the account URL and instrument URL from environment variables
  account_url = os.environ["ROBINHOOD_ACCOUNT_URL"]
  instrument_url = os.environ["ROBINHOOD_INSTRUMENT_URL"]

  data = {
      "account": account_url,
      "instrument": instrument_url,
      "price": str(price),
      "symbol": stock,
      "type": "market",
      "time_in_force": "gtc",
      "trigger": "immediate",
      "side": "sell",
      "quantity": str(quantity),
  }
  response = client.post(
      "https://api.robinhood.com/orders/",
      data=data,
  )
  response.raise_for_status()
  return response.json()

# Main function
def main(stocks):
  # Set up the API client
  client = get_client()

  # For each stock in the list
  for stock in stocks:
    # Get the current price of the stock
    price = get_price(client, stock)

    # Get the median price of the stock over the past 2 years
    median_price = get_median_price(client, stock)

    # Calculate the number of shares to buy/sell based on the $1000 target
    quantity = int(1000 / price)

    # If the current price is more than 1/3 below the median price
    if price < median_price / 3:
        # Buy the calculated number of shares of the stock
        buy_response = buy_shares(client, stock, quantity, price)
        print(f"Bought {quantity} shares of {stock} at ${price}")

    # If the current price is more than 2/3 above the median price
    elif price > median_price * 2 / 3:
        # Sell the calculated number of shares of the stock
        sell_response = sell_shares(client, stock, quantity, price)
        print(f"Sold {quantity} shares of {stock} at ${price}")

    # Call the main function
    if __name__ == "__main__":
    stocks = ["GDDY", "ADBE", "AMZN", "TSLA", "MSFT", "META", "GOOGL"]  # Replace this with a list of stocks you want to trade
    main(stocks)
