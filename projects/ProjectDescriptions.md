# Project Descriptions

  * [A Cryptocurrency Portfolio App](#a-cryptocurrency-portfolio-app)
  * [A Real-Time Price Alert App](#a-real-time-price-alert-app)
  * [A Top 100 Cryptocurrency Ranking App](#a-top-100-cryptocurrency-ranking-app)
  * [Predict The Future Values of the Top 100 Crytocurrencies](#predict-the-future-values-of-the-top-100-cryptocurrencies)
  * [Store Real-Time of 1000 Cryptocurrencies' Information in Excel Using Python](#store-real-time-of-1000-cryptocurrencies-information-in-excel-using-python)

## A Cryptocurrency Portfolio App
Personal crypto assets can be tracked conveniently using this app. Total value of all own crypto assets combined with detailed information are displayed in neat tabular format. Positive and negative values are indicated in green and red color respectively.
#### sample output:
After running `coincap_cryptocurrencyporfolio.py` script from folder `CryptoPorfolio`, we have:
![](/images/portfolio.JPG)
Note that amount of owned assets are stated in `porfolio.txt`.

## A Real-Time Price Alert App
User gets notified when cryptocurrencies hit certain prices in USD. This app can be running in background and the computer will shout things like, 'Litecoin hits $1200!'.
#### sample output:
After running `coincap_cryptoalert.py` script from folder `CryptoAlert`, initally we have:
![](/images/alert2.JPG)
Whenever Litecoin asset hits certain price (70) that specified in `alerts.txt`, we will be notified for first time by computer speaking sound  'Litecoin hits 70' :
![](/images/alert1.JPG)

## A Top 100 Cryptocurrency Ranking App
User can sort the top 100 cryptocurrencies by rank, daily percentage change or daily volume. Positive and negative values are color coated green and red.
#### sample output:
By running `coincap_cryptotop100ranker.py` script from folder `CryptoRanker`, we have:
![](/images/ranker1.JPG)
```
.
.
.
```
![](/images/ranker2.JPG)

## Predict The Future Values of the Top 100 Cryptocurrencies
Predicting the potential future price values of top 100 cryptocurrencies if the global market cap [such as world stock market levels hits certain levels](http://money.visualcapitalist.com/worlds-money-markets-one-visualization-2017/). This is done based on assumptions on the percentage of market cap that each cryptocurrency holds the same
#### sample output:
By running `coincap_cryptofuturevaluetop100.py` script from folder `CryptoFutureValues`, we have:
![](/images/futurevalue.JPG)

## Store Real-Time of 1000 Cryptocurrencies' Information in Excel Using Python
Extract 1000 crytocurrency information and save to an excel file using Python.
#### sample output:
After running `coincap_cryptofuturevaluetop100.py` script from folder `CryptoSaveToExcelFile`, we have  `cryptocurrencies.xlsx` excel file as shown below:
![](/images/save.JPG)
