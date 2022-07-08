from flask import Flask, redirect, url_for, render_template, request #Using the flask framework
import cryptocompare
import json

#FLASK_DEBUG=1 flask run
#return "BTC : " + str(data['BTC']['USD'])
cryptocompare.cryptocompare._set_api_key_parameter("957a2b674995bd6f8d09041c82c895638066c604af40687291ca7f7f35447801") #100k calls/month



app = Flask(__name__)

class CryptoClass:

    def __init__(self, cfrom, cto):
        self.cfrom = cfrom #price from i.e Btc
        self.cto   = cto #price to i.e Eth
        

    def priceConverter(self):
        dic = cryptocompare.get_price([self.cfrom],[self.cto])
        return [self.cfrom,self.cto,dic[self.cfrom][self.cto]]






@app.route('/', methods=["GET", "POST"])
def home():




    btcUS = cryptocompare.get_price(['BTC'],['USD'])
    ethUS = cryptocompare.get_price(['ETH'],['USD'])
    dogeUS = cryptocompare.get_price(['DOGE'],['USD'])
    bnbUS = cryptocompare.get_price(['BNB'],['USD'])
    adaUS = cryptocompare.get_price(['ADA'],['USD'])
    dotUS = cryptocompare.get_price(['DOT'],['USD'])

    


    btcUSprice = "BTC : " + str(btcUS['BTC']['USD'])
    ethUSprice = "ETH : " + str(ethUS['ETH']['USD'])
    dogeUSprice= "DOGE : " + str(dogeUS['DOGE']['USD'])
    bnbUSprice= "BNB : " + str(bnbUS['BNB']['USD'])
    adaUSprice= "ADA : " + str(adaUS['ADA']['USD'])
    dotUSprice= "DOT : " + str(dotUS['DOT']['USD'])
    



    return render_template("index.html", btcprice = btcUSprice + " USD", ethprice = ethUSprice + " USD", dogeprice = dogeUSprice + " USD", bnbprice=bnbUSprice + " USD", adaprice=adaUSprice + " USD", dotprice=dotUSprice + " USD")

@app.route('/convert', methods=["GET","POST"])

def converter():
        
        
    try:

        A = str(request.form.get("FROM"))
        B = str(request.form.get("TO"))
        C = float(request.form.get("AMOUNT"))
        
        if A!="" and B!="":
            price1 = CryptoClass(A.upper(),B.upper())
            a = price1.priceConverter()

            D = C*float(a[2])
            return render_template("converter.html", fromResult = a[0] +" = ", amountResult = a[0], toResult = a[2],toResultName = a[1], resultAmount =  D, coefAmount = C)
        else:
            return render_template("converter.html", invalid = "") 
        
    except :
        
        return render_template("converter.html") 



       
        

        
      
@app.route('/swap')

def swap():
    return render_template("swap.html")



@app.route('/map')

def map():
    return render_template("map.html")

@app.route('/donate')

def donate():
    return render_template("donate.html")

@app.route('/contact')

def contact():
    return render_template("contact.html")

@app.route('/charts')
def charts():
    
    return render_template("charts.html")


if __name__ == "__main__":
    app.run(debug=True)




    #Evolution du btc/other graph 
