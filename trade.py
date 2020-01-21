import requests
import time

# this code request for orderbook btse

while 1 < 2 :
    url = "https://api.btse.com/futures/api/v2/trades"
    r = requests.get(url)
    data = r.json()
    for item in data:
        if(item['symbol'] == 'BTCPFC'):
            uri = f"https://script.google.com/macros/s/AKfycbx759-h44OdWLmDvTl-z0PRZH49d7qX0O_migKM7K3wAdbfh6Vv/exec?action=tradebtse&price={item['price']}&size={item['size']}&timestamps={item['timestamp']}&side={item['side']}&serialId={item['serialId']}"
            requests.post(uri)
    