import xlsxwriter
import requests
import json

start = 1
row = 1

crypto_workbook = xlsxwriter.Workbook('cryptocurrencies.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Market Cap')
crypto_sheet.write('D1', 'Price')
crypto_sheet.write('E1', '24H Volume')
crypto_sheet.write('F1', 'Hour Change')
crypto_sheet.write('G1', 'Day Change')
crypto_sheet.write('H1', 'Week Change')

for i in range(10):
    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array&start=' + str(start)
    request = requests.get(ticker_url)
    results = request.json()
    data = results['data']

    for currency in data:
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']
        quotes = currency['quotes']['USD']
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        crypto_sheet.write(row,0,name)
        crypto_sheet.write(row,1,symbol)
        crypto_sheet.write(row,2,str(market_cap))
        crypto_sheet.write(row,3,str(price))
        crypto_sheet.write(row,4,str(volume))
        crypto_sheet.write(row,5,str(hour_change))
        crypto_sheet.write(row,6,str(day_change))
        crypto_sheet.write(row,7,str(week_change))

        row +=1

    start += 100

crypto_workbook.close()
