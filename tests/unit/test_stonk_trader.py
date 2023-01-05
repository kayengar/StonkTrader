import unittest
import os
import requests_mock

from main import get_client, get_price, get_median_price, buy_shares, sell_shares

class TestClient(unittest.TestCase):
  def test_get_client(self):
    # Set up mock responses for the API
    with requests_mock.Mocker() as mock:
      # Mock the authentication request
      mock.post(
          "https://api.robinhood.com/api-token-auth/",
          json={"token": "123456"},
      )

      # Mock the price request
      mock.get(
          "https://api.robinhood.com/quotes/AAPL/",
          json={"last_trade_price": "123.45"},
      )

      # Set the environment variables
      os.environ["ROBINHOOD_USERNAME"] = "user"
      os.environ["ROBINHOOD_PASSWORD"] = "pass"

      # Get the client
      client = get_client()

      # Test the client
      assert client.headers["Authorization"] == "Bearer 123456"
      response = client.get("https://api.robinhood.com/quotes/AAPL/")
      assert response.json() == {"last_trade_price": "123.45"}

class TestPrices(unittest.TestCase):
  # ...

  def test_get_median_price(self):
    # Set up mock responses for the API
    with requests_mock.Mocker() as mock:
      # Mock the price request
      mock.get(
          "https://api.robinhood.com/historicals/AAPL/?bounds=2_YEAR&interval=day",
          json={
              "historicals": [
                  {"close_price": "100.00"},
                  {"close_price": "120.00"},
                  {"close_price": "80.00"},
                  {"close_price": "90.00"},
              ]
          },
      )

      # Get the client
      client = get_client()

      # Test the get_median_price function
      assert get_median_price(client, "AAPL") == 95.00

class TestTrades(unittest.TestCase):
  def test_buy_shares(self):
    # Set up mock responses for the API
    with requests_mock.Mocker() as mock:
      # Mock the order request
      mock.post(
          "https://api.robinhood.com/orders/",
          json={"id": "123456"},
      )

      # Set the environment variables
      os.environ["ROBINHOOD_ACCOUNT_URL"] = "https://api.robinhood.com/accounts/123/"
      os.environ["ROBINHOOD_INSTRUMENT_URL"] = "https://api.robinhood.com/instruments/456/"

      # Get the client
      client = get_client()

      # Test the buy_shares function
      assert buy_shares(client, "AAPL", 10, 123.45) == {"id": "123456"}

  def test_sell_shares(self):
    # Set up mock responses for the API
    with requests_mock.Mocker() as mock:
      # Mock the order request
      mock.post(
          "https://api.robinhood.com/orders/",
          json={"id": "123456"},
      )

      # Set the environment variables
      os.environ["ROBINHOOD_ACCOUNT_URL"] = "https://api.robinhood.com/accounts/123/"
      os.environ["ROBINHOOD_INSTRUMENT_URL"] = "https://api.robinhood.com/instruments/456/"

      # Get the client
      client = get_client()

      # Test the sell_shares function
      assert sell_shares(client, "AAPL", 10, 123.45) == {"id": "123456"}
