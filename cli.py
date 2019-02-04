import argparse
import json
from forex_python.converter import CurrencyRates, CurrencyCodes

# Creating instances of classes from forex-python module
currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

# Loading currencies data
with open('currencies_supported.json') as file:
    data = json.load(file)

def convert(amount, input_currency, output_currency=None):
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

    result_json = json.dumps(result, sort_keys=True)
    print(result_json)
    return result_json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Currency Converter',
                                     description='''
                                     --------------------
                                     DESCRIPTION:
                                     This tool works good
                                     --------------------
                                     ''',
                                     epilog="Copyrights @MatejSveda",
                                     add_help=True
                                     )
    parser.add_argument('--amount', action="store", type=float, dest="amount", required=True)
    parser.add_argument('--input_currency', action="store", dest="input_currency", required=True)
    parser.add_argument('--output_currency', action="store", dest="output_currency")

    arg = parser.parse_args()
    convert(arg.amount, arg.input_currency, arg.output_currency)
