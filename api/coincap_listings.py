import json
import requests

listings_url = 'https://api.coinmarketcap.com/v2/listings/'

request = requests.get(listings_url)
result = request.json()

# print(json.dumps(result, sort_keys=True, indent=4))

data = result['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + '({})'.format(symbol))
