# List of symbols

import finnhub

import constants

finnhub_client = finnhub.Client(api_key=constants.key)

print(finnhub_client.stock_symbols('US'))