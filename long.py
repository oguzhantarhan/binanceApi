from binance.client import Client
import requests


symbol='OPUSDT'

api_key="apiKey"
api_secret="secretKey"
api="https://fapi.binance.com/fapi/v1/ticker/24hr?symbol=OPUSDT"
client = Client(api_key=api_key, api_secret=api_secret,testnet = False)


balance=float( client.futures_account_balance()[5]["availableBalance"])

data=requests.get(api).json()
price=float(data["lastPrice"])
quantity=int(balance*20/price)-3
print(quantity)

buy=client.futures_create_order(symbol=symbol,side='BUY',type='MARKET',quantity=quantity)
position=client.futures_position_information(symbol="OPUSDT")
entryPrice=float(position[0]["entryPrice"])
tp=round(entryPrice*1.002,4)
sl=round(entryPrice*0.997,4)
stop_loss_order = client.futures_create_order(symbol=symbol,side='SELL', type='STOP', stopPrice = sl, quantity = quantity, price = sl)
take_profit_order = client.futures_create_order(symbol=symbol,side='SELL', type='TAKE_PROFIT', stopPrice = tp, quantity = quantity, price = tp)