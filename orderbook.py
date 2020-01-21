import requests
import time

# this code request for orderbook btse

while 1 < 2 :
    url = "https://api.btse.com/futures/api/v1/orderbook/BTCPFC"
    r = requests.get(url)
    data = r.json()
    buy = data['buyQuote']
    sell = data['sellQuote']
    dt = data['timestamp']
    for item in buy:
        urlPost = f"https://script.google.com/macros/s/AKfycbx759-h44OdWLmDvTl-z0PRZH49d7qX0O_migKM7K3wAdbfh6Vv/exec?action=orderbookbtse&price={item['price']}&size={item['size']}&timestamps={dt}&side=buy"
        requests.post(urlPost)
    for item in sell:
        urlPost = f"https://script.google.com/macros/s/AKfycbx759-h44OdWLmDvTl-z0PRZH49d7qX0O_migKM7K3wAdbfh6Vv/exec?action=orderbookbtse&price={item['price']}&size={item['size']}&timestamps={dt}&side=sell"
        requests.post(urlPost)
    