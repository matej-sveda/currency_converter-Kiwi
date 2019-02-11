# Currency Converter

This project contains API and CLI appliation which converts curencies according to arguments inserted by user.
Supporting 33 most popular world currencies.

## Getting Started

### Prerequisites

Project was build and tested on Ubuntu 16.04 with Python 3.5.2, using following modules:

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

<<<<<<< HEAD
### API examples

```
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD HTTP/1.1
=======
### API

1. Open your terminal/command line in project directory.
2. Run server by running api.py
```
$ python api.py

```
3. Now you can start sending HTTP GET requests.

- examples

```
GET /currency_converter?amount=100.0&input_currency=EUR&output_currency=CZK HTTP/1.1
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
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD HTTP/1.1
>>>>>>> 150b0f454fd2b1a8bc42718aa1e0f4a0a073a16b
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
<<<<<<< HEAD

```
GET /currency_converter?amount=10.92&input_currency=£ HTTP/1.1
=======
```
GET /currency_converter?amount=10.92&input_currency=£ HTTP/1.1
>>>>>>> 150b0f454fd2b1a8bc42718aa1e0f4a0a073a16b
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

<<<<<<< HEAD
### CLI examples

```
./cli.py --amount 100.0 --input_currency EUR --output_currency CZK | jq
=======
I recommend using Postman tool for sending requests.

### CLI 

1. Open your terminal/command line in project directory.
2. Now you can start sending commands.

- examples

```
$python cli.py --amount 100.0 --input_currency EUR --output_currency CZK | jq
>>>>>>> 150b0f454fd2b1a8bc42718aa1e0f4a0a073a16b
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
<<<<<<< HEAD
./cli.py --amount 0.9 --input_currency ¥ --output_currency AUD | jq
=======
$python cli.py --amount 0.9 --input_currency ¥ --output_currency AUD | jq
>>>>>>> 150b0f454fd2b1a8bc42718aa1e0f4a0a073a16b
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
<<<<<<< HEAD
./cli.py --amount 10.92 --input_currency £ | jq
=======
$python cli.py --amount 10.92 --input_currency £ | jq
>>>>>>> 150b0f454fd2b1a8bc42718aa1e0f4a0a073a16b
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
<<<<<<< HEAD
}
```

## Authors

* **Matej Sveda** - [matej-sveda](https://github.com/matej-sveda)
=======
  
}
```
As mentioned above, I recommend using jq module by installing it and typing "| jq" at the end of the CLI command. Without that, output is not as     structured and intended as a proper JSON should be.

```
python cli.py --amount 10.92 --input_currency £ 

{"input": {"amount": 10.92, "currency": "GBP"}, "output": {"AUD": 1.808, "BGN": 2.2307, "BRL": 4.8065, ...}}
```



## Authors

**Matej Sveda** - [matej-sveda](https://github.com/matej-sveda)
>>>>>>> 150b0f454fd2b1a8bc42718aa1e0f4a0a073a16b

See also the list of [contributors](https://github.com/matej-sveda/currency_converter-Kiwi/graphs/contributors)
