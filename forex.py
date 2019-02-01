from forex_python.converter import CurrencyRates, CurrencyCodes


currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

print(currency_rates.get_rates('CZK'))
print(currency_rates.get_rate('NOK', 'CZK'))

print(currency_codes.get_symbol('NOK'))

