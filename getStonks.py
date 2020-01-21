import requests
import json


api_key = "" # Add your World Trading Data API Key here inside the quotes
endpoint = "https://api.worldtradingdata.com/api/v1/stock"




api_endpoint = "https://api.polygon.io/v1/last/stocks/"

stonks_list = ["TSLA","^DJI","SPCE","AAPL" ]
length = len(stonks_list)
number_of_fours = int(length/4)
modulus = length%4

stock_string = ""

y=0
for x in range(number_of_fours):
    for x in range(0,4):
        if x == 3 :
            stock_string = stock_string + stonks_list[(4*y)+x]
        else :
            stock_string = stock_string + stonks_list[(4 * y) + x] + ","

    response = requests.get(endpoint, {"api_token": api_key, "symbol": stock_string})
    response_json = response.json()
    for x in range(0,4):
        close_yesterday = response_json["data"][x]["close_yesterday"]
        price = response_json['data'][x]["price"]
        difference = round(float(price) - float(close_yesterday),2)
        symbol = response_json["data"][x]["symbol"]
        if difference > 0:
            print(symbol + " $" + price + " (+" + str(difference) + ")")
        else :
            print(symbol + " $" + price + " (" + str(difference) + ")")
    stock_string = ""
    y = y + 1



for x in range(modulus):
    if x== modulus - 1:
        stock_string = stock_string + stonks_list[(4 * number_of_fours) + x]
    else :
        stock_string = stock_string + stonks_list[(4 * number_of_fours) + x] + ","

response_mod = requests.get(endpoint, {"api_token": api_key, "symbol": stock_string})
response_json_mod = response_mod.json()
for x in range(0,modulus):
    price = response_json_mod['data'][x]["price"]
    symbol = response_json_mod["data"][x]["symbol"]
    close_yesterday = response_json_mod["data"][x]["close_yesterday"]
    difference = round(float(price) - float(close_yesterday), 2)
    if difference > 0:
        print(symbol + " $" + price + " (+" + str(difference) + ")")
    else:
        print(symbol + " $" + price + " (-" + str(difference) + ")")


