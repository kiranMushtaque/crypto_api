import requests

class CryptoCurrencyAPI:
    BASE_URL = "https://api.binance.com/api/v3/ticker"

    def get_all_coins(self):
        """Fetch real-time prices for all available coins"""
        url = f"{self.BASE_URL}/price"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_coin_by_symbol(self, symbol):
        """Fetch real-time price for a specific coin symbol (e.g., BTCUSDT)"""
        url = f"{self.BASE_URL}/price?symbol={symbol.upper()}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

if __name__ == "__main__":
    api = CryptoCurrencyAPI()

    # Get all coins
    all_coins = api.get_all_coins()
    print("All Coins:\n", all_coins[:5])  # Print first 5 for brevity

    # Get a specific coin by symbol
    btc_price = api.get_coin_by_symbol("BTCUSDT")
    print("\nBTCUSDT Price:\n", btc_price)
