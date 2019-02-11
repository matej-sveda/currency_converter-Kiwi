import json
from forex_python.converter import CurrencyRates, CurrencyCodes

# Creates instances of classes from forex-python module
currency_rates = CurrencyRates()
currency_codes = CurrencyCodes()

def error_msg(type, msg):
    err = {type: msg}
    return json.dumps(err)

def local_currency_file():
    with open('currencies_supported.json') as data:
        return json.load(data)

def check_currency(user_input):
    try:
        result = [curr for curr in local_currency_file() if curr['cc'] == user_input or curr['symbol'] == user_input]
        if result != []:
            return result[0]['cc']
        else:
            raise NameError
    except:
        return error_msg('Error', "Entered currency code or symbol not found! Mind the upper casing!")

def convert_to_all(amount, input_currency):
    # Check amount type and value
    try:
        if type(amount) not in [int, float] or amount <= 0:
            raise ValueError
    except:
        return error_msg('Error', "Amount has to be a number greater than zero!")

    input_currency_checked = check_currency(input_currency)

    # If currency 3-letter code not found, return an error message defined in check_currency()
    if len(input_currency_checked) != 3:
         return input_currency_checked
    else:
        # Get rates from API
        try:
            rates = currency_rates.get_rates(input_currency_checked)
        except:
            return error_msg('Error', "Exchange API not responding! Please, check your connection!")

        # Multuplies rate by amount and rounds output
        for key, value in rates.items():
            rates[key] = round(value * amount, 2)

        result = {
            "input": {
                "amount": amount,
                "currency": input_currency_checked
            },

            "output": rates
        }

        # Creates result in json format and returning
        result_json = json.dumps(result, sort_keys=True)

        # Returns json result
        return result_json


def convert_between(amount, input_currency, output_currency):
    # Check amount type and value
    try:
        if type(amount) not in [int, float] or amount <= 0:
            raise ValueError
    except:
        return error_msg('Error', "Amount has to be a number greater than zero!")

    input_currency_checked = check_currency(input_currency)
    output_currency_checked = check_currency(output_currency)

    # If currency 3-letter code not found, return an error message defined in check_currency()
    if len(input_currency_checked) != 3:
        return input_currency_checked
    elif len(output_currency_checked) != 3:
        return output_currency_checked

    else:
        try:
            rate = currency_rates.convert(input_currency_checked, output_currency_checked, amount)
        except:
            return error_msg('Error', "Exchange API not responding! Please, check your connection!")
        rate = round(rate, 2)
        result = {
            "input": {
                "amount": amount,
                "currency": input_currency_checked
            },

            "output": {
                output_currency_checked: rate
            }
        }

        # Creates result in json format and returning
        result_json = json.dumps(result, sort_keys=True)

        # Returns json result
        return result_json

