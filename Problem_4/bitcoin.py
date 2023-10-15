import sys
import requests
import json


response = requests.get(
    " https://api.coindesk.com/v1/bpi/currentprice.json").json()

price = response["bpi"]["USD"]["rate_float"]
to_buy = float(sys.argv[1])

try:
    float(sys.argv[1])
except IndexError:
    sys.exit("missing command-line argument")
except ValueError:
    sys.exit("command-line argument is not a number")

print(f"{to_buy * price:,.4f}")
