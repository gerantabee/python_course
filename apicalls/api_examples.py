# Using an api result
# we're going to import libraries outside of our base python libraries
# Specifically requests, json and pprint (prettyprint)

import pprint as pp
import requests as req

bitcoinprice = req.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
# print(bitcoinprice)

print("Current Bitcoin price:")
pp.pprint(bitcoinprice['bpi']['USD']['rate'])

# The full syntax of a request can be included in a function, and
# we can include error handling to manage different possible responses from the host.
# Let's incorporate the below in a function called get_price():
# 'https://api.coindesk.com/v1/bpi/currentprice.json'

def get_price():
  url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

  try:
    response = req.get(url)

    if response.status_code == 200:
      bitcoin_price = response.json()
      return bitcoin_price
    elif response.status_code == 404:
      print("Error 404: Not Found - double check URL?")
      return None
    else:
      print("Error", response.status_code)
      return None
  except req.exceptions.RequestException as e:
    print("Error:", e)
    return None

# help(req.request)
get_price()