import json
import requests
from datetime import datetime

currency = 'USD'#'BTC'
global_url = 'https://api.coinmarketcap.com/v2/global/?convert=' + currency

request = requests.get(global_url)
result = request.json()

# jsdump = json.dumps(result, sort_keys=True, indent=4)
# print(jsdump)

active_currency = result['data']['active_cryptocurrencies']
active_market = result['data']['active_markets']
bitcoin_percent = result['data']['bitcoin_percentage_of_market_cap']
last_updated = result['data']['last_updated']
global_cap = int(result['data']['quotes'][currency]['total_market_cap'])
global_vol = int(result['data']['quotes'][currency]['total_volume_24h'])

active_currency_str = '{:,}'.format(active_currency)
active_market_str = '{:,}'.format(active_market)
bitcoin_percent_str = '{:,}'.format(bitcoin_percent)
global_cap_str = '{:,}'.format(global_cap)
global_vol_str = '{:,}'.format(global_vol)


last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

print()
print('There are currently ' + active_currency_str + ' active cryptocurrencies and ' + active_market_str + ' active markets.')
print()
print('The global cap of all cryptos is '+ global_cap_str + ' and the 24h global volume is ' + global_vol_str + '.')
print()
print("Bitcoin's total percentage of the global cap is " + bitcoin_percent_str + '%.')
print()
print('The information was last updated on ' + last_updated_string + '.')
