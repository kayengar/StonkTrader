# Stock Trading Bot

This is a Python program that automates the buying and selling of stocks on the Robinhood brokerage platform. It takes a list of stocks as input and buys or sells them based on the following criteria:

If the current price of the stock is more than 1/3 below its median price over the past 2 years, the program will buy $1000 worth of the stock.

If the current price of the stock is more than 2/3 above its median price over the past 2 years, the program will sell $1000 worth of the stock.

## Prerequisites

To use this program, you will need the following:

1. A Robinhood account
2. Your Robinhood account credentials (username and password)
3. The URL of your Robinhood account and the URL of the instrument corresponding to the stock you want to trade
4. An API token for the Robinhood API (you can get this by going to the API token page in your Robinhood account settings)

## Setup

To set up the program, follow these steps:

1. Clone this repository to your local machine.
2. Create a file called .env in the root directory of the repository.
3. Add the following variables to the .env file, replacing the placeholder values with your own Robinhood account credentials and URLs:
   ```shell
   ROBINHOOD_USERNAME=your_username
   ROBINHOOD_PASSWORD=your_password
   ROBINHOOD_API_TOKEN=your_api_token
   ROBINHOOD_ACCOUNT_URL=your_account_url
   ROBINHOOD_INSTRUMENT_URL=your_instrument_url
   ```

4. Install the required libraries by running the following command in the root directory of the repository:
    ```shell
    pip install -r requirements.txt
    ```

## Usage

To use the program, modify the stocks list in the main function to include the stocks you want to trade. Then, run the program by executing the following command in the root directory of the repository:
   ```shell
   python trading_bot.py
   ```
