import requests

def get_binance_tickers():
    try:
        url = "https://api.binance.com/api/v3/exchangeInfo"
        response = requests.get(url)
        data = response.json()
        tickers = [symbol['symbol'] for symbol in data['symbols']]
        return tickers
    except Exception as ex:
        print(f"Error fetching Binance tickers: {ex}")
        return None

def main():
    binance_tickers = get_binance_tickers()

    if binance_tickers:
        tickers_str = "\n".join(binance_tickers)
        print(f"Available Binance tickers:\n{tickers_str}")
    else:
        print("Failed to fetch Binance tickers.")

if __name__ == "__main__":
    main()
