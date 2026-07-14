from pathlib import Path
import pandas as pd

# Folder containing the downloaded Yahoo CSVs
YAHOO_FOLDER = Path("data/yahoo")

# Clean every CSV in the folder
for csv_file in YAHOO_FOLDER.glob("*.csv"):
    print(f"Cleaning {csv_file.name}...")

    # Read the CSV having multiple header rows
    df = pd.read_csv(csv_file, header=[0, 1])

    # Keep only the first header level
    df.columns = df.columns.get_level_values(0)

    # Rename first column to Date
    df.rename(columns={"Price": "Date"}, inplace=True)

    # Remove the extra row containing "Date"
    df = df[df["Date"] != "Date"]

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"])

    # Convert numeric columns
    numeric_cols = ["Open", "High", "Low", "Close", "Volume"]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Round OHLC values
    price_cols = ["Open", "High", "Low", "Close"]
    df[price_cols] = df[price_cols].round(2)

    # Volume should be integer
    df["Volume"] = df["Volume"].astype("Int64")

    # Remove rows with missing values
    df.dropna(inplace=True)

    # Sort by date
    df.sort_values("Date", inplace=True)

    # Save back to the same file
    df.to_csv(csv_file, index=False)

    print(f"{csv_file.name} cleaned successfully.")

print("\nAll Yahoo CSV files cleaned.")