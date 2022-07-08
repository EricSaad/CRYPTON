# CRYPTON

CRYPTON is a web-based interface allowing you to check the price of verious cryptocurrencies, to find the relative price of a specific cryptocurrency compared to an other one, and to swap your coins using your Metamask wallet.


To run the code:
<sub>
pip3 install flask
pip3 install cryptocompare
Run app.py
Enter the following address into your browser's search bar: http://127.0.0.1:5000/
<sub>

** CLI Usage **
```
app.py _priceFrom_ _priceTo_

Example:
app.py ETH BTC
=> One ETH is worth X BTC (X being the actual value fetched from CRYPTOCOMPARE using their API)
```
