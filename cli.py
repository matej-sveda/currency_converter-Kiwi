import argparse
from converter import convert

def get(amount, input_currency, output_currency=None):
    # Returns and prints the result of convert function from converter.py
    return print(convert(amount, input_currency, output_currency))

if __name__ == '__main__':
    # Creates parser
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
    # Creates arguments
    parser.add_argument('--amount', action="store", type=float, dest="amount", required=True)
    parser.add_argument('--input_currency', action="store", dest="input_currency", required=True)
    parser.add_argument('--output_currency', action="store", dest="output_currency")

    # Passes the arguments into get function
    arg = parser.parse_args()
    get(arg.amount, arg.input_currency, arg.output_currency)
