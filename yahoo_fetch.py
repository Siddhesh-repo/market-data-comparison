import pandas as pd
import yfinance as yf

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
    Fetch last 100 trading days of daily OHLCV data from Yahoo Finance.
    Returns a pandas DataFrame.
    """

    df = yf.download(
        tickers=symbol,
        period="100d",
        interval="1d",
        auto_adjust=False,
        progress=False
    )

    if df.empty:
        raise Exception(f"No data found for {symbol}")

    # Keep only required columns
    df = df[["Open", "High", "Low", "Close", "Volume"]]

    df.index.name = "Date"

    return df


def save_symbol(symbol):
    """
    Fetch and save CSV for one symbol.
    """

    try:
        print(f"Fetching {symbol}...")

        df = fetch_symbol(symbol)

        df.to_csv(f"data/yahoo/{symbol}.csv")

        print(f"✓ Saved data/yahoo/{symbol}.csv")

    except Exception as e:
        print(f"✗ Error fetching {symbol}")
        print(e)


def main():

    print("=" * 50)
    print("Yahoo Finance OHLCV Downloader")
    print("=" * 50)

    for i, symbol in enumerate(SYMBOLS, start=1):

        print(f"\n[{i}/{len(SYMBOLS)}]")

        save_symbol(symbol)

    print("\nDownload Complete.")


if __name__ == "__main__":
    main()