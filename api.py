from flask import Flask, jsonify, request
import json
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)

# Creating instances of classes from forex-python module
currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

# Loading currencies data
with open('currencies_supported.json') as file:
    data = json.load(file)

@app.route('/convert', methods=['GET'])
def convert():
    amount = request.args.get('amount', type=float)
    input_currency = request.args.get('input_currency')
    output_currency = request.args.get('output_currency', default=None)

    if output_currency is None:
        for currency in data:
            if currency['symbol'] == input_currency:
                input_currency = currency['cc']
        output =  currency_rates.get_rates(input_currency)
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

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
