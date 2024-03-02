import requests

def get_crypto_price(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
        response = requests.get(url)
        data = response.json()
        return data['price']
    except Exception as ex:
        print(f"Error fetching data for {symbol}: {ex}")
        return None

def main():
    btc_price = get_crypto_price("BTC")
    matic_price = get_crypto_price("MATIC")

    if btc_price:
        print(f"Bitcoin (BTC) price: ${btc_price}")

    if matic_price:
        print(f"Matic (MATIC) price: ${matic_price}")

if __name__ == "__main__":
    main()
