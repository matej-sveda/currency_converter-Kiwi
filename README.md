# Currency Converter

This project contains API and CLI appliation which converts curencies according to arguments inserted by user.
Supporting 33 most popular world currencies.

## Getting Started

### Prerequisites

Project was build and tested on Ubuntu with Python 3.5.2, using following modules:

- flask 1.0.2
- argparse 1.4.0
- forex-python 1.3
- jq 0.1.6 (not necessary, but comes handy when calling for CLI outputs)
- json (standard python lib)

### Installing

Install all missing modules using pip:
```
pip install flask
pip install argparse
...
```

## How to use

You can choose between using API or CLI. 
Both require 2 arguments, `amount` and `input_currency`, 3rd argument, `input_currency`, is optional. You can choose between inserting arguments as 3 letters currency code (USD, EUR) or as currency symbol (US$, €). 
Please note that due to dupplicity of symbols at some currencies (e.g. AUD - $, CAD - $), these symbols were edited slightly (A$, C$). All supported currencies with their symbols are listed in currencies_supported.json file.

### API examples

```
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD HTTP/1.1
{
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.20, 
    }
}
```

```
GET /currency_converter?amount=10.92&input_currency=£ HTTP/1.1
{
    "input": {
        "amount": 10.92,
        "currency": "GBP"
    },
    "output": {
        "EUR": 14.95,
        "USD": 17.05,
        "CZK": 404.82,
        .
        .
        .
    }
}
```

### CLI examples

```
./cli.py --amount 100.0 --input_currency EUR --output_currency CZK | jq
{
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2707.36, 
    }
}
```
```
./cli.py --amount 0.9 --input_currency ¥ --output_currency AUD | jq
{
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.20, 
    }
}
```
```
./cli.py --amount 10.92 --input_currency £ | jq
{
    "input": {
        "amount": 10.92,
        "currency": "GBP"
    },
    "output": {
        "EUR": 14.95,
        "USD": 17.05,
        "CZK": 404.82,
        .
        .
        .
    }
}
```

## Authors

* **Matej Sveda** - *Initial work* - [matej-sveda](https://github.com/matej-sveda)

See also the list of [contributors](https://github.com/matej-sveda/currency_converter-Kiwi/graphs/contributors)


## Acknowledgments

This project was created as a task for a job application
