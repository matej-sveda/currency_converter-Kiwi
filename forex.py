# Importing modules
from forex_python.converter import CurrencyRates, CurrencyCodes
import json

# Creating instances of classes from forex-python module
currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

# Loading currencies data
with open('currencies_supported.json') as file:
    data = json.load(file)

# Convert function with arguments input_currency, output currency and amount
def convert(input_currency, output_currency=None, amount=1):
    if output_currency is None:
        for currency in data:
            if currency['symbol'] == input_currency:
                input_currency = currency['cc']
        return currency_rates.get_rates(input_currency)
    else:
        for currency in data:
            if currency['symbol'] == input_currency:
                input_currency = currency['cc']
            if currency['symbol'] == output_currency:
                output_currency = currency['cc']
        return currency_rates.convert(input_currency, output_currency, amount)

print(convert('Skr', 'A$'))