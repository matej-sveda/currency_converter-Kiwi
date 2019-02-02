# Importing modules
from forex_python.converter import CurrencyRates, CurrencyCodes
import json

# Creating instances
currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

# Testing basic forex-python module functions
#print(currency_rates.get_rates('CZK'))
#print(currency_rates.get_rate('EUR', 'CZK'))
#print(currency_rates.convert('EUR', 'CZK', 100))

#print(currency_codes.get_symbol('NOK'))

# Loading currencies data (used for getting symbols only)
with open('currencies.json') as file:
    data = json.load(file)

# Convert function, using forex-python package
def convert(input_currency, output_currency=None, amount=1):
    if output_currency is None:
        return currency_rates.get_rates(input_currency)
    else:
        for currency in data:
            if currency['symbol'] == input_currency:
                input_currency = currency['cc']
            if currency['symbol'] == output_currency:
                output_currency = currency['cc']
        return currency_rates.convert(input_currency, output_currency, amount)

print(convert('€', 'CZK', 100))


