import requests
import pandas as pd
import time
API_KEY = "U53WNF0XZW1EIPFO"
BASE_URL = "https://www.alphavantage.co/query"

SYMBOLS = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "META",
    "TSLA",
    "NVDA",
    "AMD",
    "NFLX",
    "INTC"
]

def fetch_symbol(symbol):
    """
    Fetch daily OHLCV data for a single symbol.
    Returns a pandas DataFrame.
    """

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    if "Time Series (Daily)" not in data:
        raise Exception(
            f"Unable to fetch {symbol}\nResponse: {data}"
        )

    df = pd.DataFrame.from_dict(
        data["Time Series (Daily)"],
        orient="index"
    )

    df = df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })

    df.index = pd.to_datetime(df.index)
    df.index.name = "Date"

    df = df.astype({
        "Open": float,
        "High": float,
        "Low": float,
        "Close": float,
        "Volume": int
    })

    df = df.sort_index()

    # Keep only last 100 trading days
    df = df.tail(100)

    return df


def save_symbol(symbol):
    """
    Fetch and save CSV for one symbol.
    """

    try:
        print(f"Fetching {symbol}...")

        df = fetch_symbol(symbol)

        df.to_csv(f"data/alpha/{symbol}.csv")

        print(f"✓ Saved data/alpha/{symbol}.csv")

    except Exception as e:
        print(f"✗ Error fetching {symbol}")
        print(e)


def main():

    print("=" * 50)
    print("Alpha Vantage OHLCV Downloader")
    print("=" * 50)

    for i, symbol in enumerate(SYMBOLS, start=1):

        print(f"\n[{i}/{len(SYMBOLS)}]")

        save_symbol(symbol)

        # Avoid hitting Alpha Vantage free API rate limit
        if i != len(SYMBOLS):
            print("Waiting 15 seconds...\n")
            time.sleep(15)

    print("\nDownload Complete.")


if __name__ == "__main__":
    main()
