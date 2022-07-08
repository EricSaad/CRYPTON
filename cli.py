import argparse
import cryptocompare
from datetime import datetime
cryptocompare.cryptocompare._set_api_key_parameter("957a2b674995bd6f8d09041c82c895638066c604af40687291ca7f7f35447801")



parser = argparse.ArgumentParser()
parser.add_argument("cryptoFrom", help="Choose a crypto you want to know the price of")
parser.add_argument("cryptoTo", help="Choose a reference crypto")
args = parser.parse_args()

Cfroms = args.cryptoFrom
Ctos = args.cryptoTo



class CryptoClass:

    def __init__(self, cryptoFrom, cryptoTo):
        self.cryptoFrom = cryptoFrom #price from i.e Btc
        self.cryptoTo  = cryptoTo #price to i.e Eth

    def converter(self):
        a = cryptocompare.get_price([self.cryptoFrom],[self.cryptoTo])
        return a[self.cryptoFrom][self.cryptoTo]


price = CryptoClass(Cfroms.upper(),Ctos.upper())
res = price.converter()

print("One ", Cfroms, " is worth ",res , Ctos)




