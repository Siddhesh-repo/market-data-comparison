import pandas as pd

symbols = [
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

PRICE_TOLERANCE = 0.05
VOLUME_TOLERANCE = 1000

summary = []

for symbol in symbols:

    print(f"Comparing {symbol}...")

    yahoo_df = pd.read_csv(f"data/yahoo/{symbol}.csv")
    alpha_df = pd.read_csv(f"data/alpha/{symbol}.csv")

    merged = pd.merge(
        yahoo_df,
        alpha_df,
        on="Date",
        suffixes=("_Yahoo", "_Alpha")
    )

    # Price Differences
    merged["Open_Diff"] = (
        merged["Open_Yahoo"] - merged["Open_Alpha"]
    ).abs()

    merged["High_Diff"] = (
        merged["High_Yahoo"] - merged["High_Alpha"]
    ).abs()

    merged["Low_Diff"] = (
        merged["Low_Yahoo"] - merged["Low_Alpha"]
    ).abs()

    merged["Close_Diff"] = (
        merged["Close_Yahoo"] - merged["Close_Alpha"]
    ).abs()

    merged["Volume_Diff"] = (
        merged["Volume_Yahoo"] - merged["Volume_Alpha"]
    ).abs()

    # Overall Status
    merged["Status"] = "Match"

    merged.loc[
        (merged["Open_Diff"] > PRICE_TOLERANCE) |
        (merged["High_Diff"] > PRICE_TOLERANCE) |
        (merged["Low_Diff"] > PRICE_TOLERANCE) |
        (merged["Close_Diff"] > PRICE_TOLERANCE) |
        (merged["Volume_Diff"] > VOLUME_TOLERANCE),
        "Status"
    ] = "Mismatch"

    # Save complete comparison
    merged.to_csv(
        f"comparison/{symbol}_comparison.csv",
        index=False
    )

    # Only mismatches
    mismatches = merged[
        merged["Status"] == "Mismatch"
    ]

    mismatches.to_csv(
        f"comparison/{symbol}_mismatches.csv",
        index=False
    )

    summary.append({
        "Symbol": symbol,
        "Total Days": len(merged),
        "Matching Days": len(merged[merged["Status"] == "Match"]),
        "Mismatch Days": len(mismatches),
        "Max Open Diff": merged["Open_Diff"].max(),
        "Max High Diff": merged["High_Diff"].max(),
        "Max Low Diff": merged["Low_Diff"].max(),
        "Max Close Diff": merged["Close_Diff"].max(),
        "Max Volume Diff": merged["Volume_Diff"].max()
    })

summary_df = pd.DataFrame(summary)

summary_df.to_csv(
    "report.csv",
    index=False
)

print("\nComparison Finished Successfully!\n")

print(summary_df)