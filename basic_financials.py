import finnhub
import constants

# Setup client
finnhub_client = finnhub.Client(api_key=constants.key)

# Basic financials
print(finnhub_client.company_basic_financials('AAPL', 'all'))