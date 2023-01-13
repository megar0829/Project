import requests

def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/BTC_KRW"

    res = requests.get(url=url).json()
    data = res["data"]
    prev_closing_price = data["prev_closing_price"]

    return prev_closing_price

if __name__ == "__main__":
    print(get_btc_krw())

# curl --request GET \
#      --url https://api.bithumb.com/public/ticker/BTC_KRW \
#      --header 'accept: application/json'