import json
from forex_python.converter import CurrencyRates, CurrencyCodes

# Creates instances of classes from forex-python module
currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

# Loads currencies data
with open('data/currencies_supported.json') as file:
    data = json.load(file)

def convert(amount, input_currency, output_currency=None):
    # Case executed without output_currency argument
    if output_currency is None:
        for currency in data:
            if currency['symbol'] == input_currency:
                input_currency = currency['cc']
        output = currency_rates.get_rates(input_currency)

        result = {
            "input": {
                "amount": amount,
                "currency": input_currency
            },

            "output": output
        }
    # Case executed with output_currency argument
    else:
        for currency in data:
            if currency['symbol'] == input_currency:
                input_currency = currency['cc']
            if currency['symbol'] == output_currency:
                output_currency = currency['cc']
        output = currency_rates.convert(input_currency, output_currency, amount)

        result = {
            "input": {
                "amount": amount,
                "currency": input_currency
            },

            "output": {
                output_currency: output
            }
        }

    # Creates result in json format and returning
    result_json = json.dumps(result, sort_keys=True)

    return result_json