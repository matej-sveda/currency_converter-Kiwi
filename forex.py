# Importing modules
from forex_python.converter import CurrencyRates, CurrencyCodes

# Creating instances
currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

# Testing basic forex-python module functions
#print(currency_rates.get_rates('CZK'))
#print(currency_rates.get_rate('EUR', 'CZK'))
#print(currency_rates.convert('EUR', 'CZK', 100))

#print(currency_codes.get_symbol('NOK'))

# Convert function with arguments input_currency, output currency and amount
def convert(input_currency, output_currency=None, amount=1):
    if output_currency is None:
        return currency_rates.get_rates(input_currency)
    else:
        return currency_rates.convert(input_currency, output_currency, amount)

print(convert('EUR',))