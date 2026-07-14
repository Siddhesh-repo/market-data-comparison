# 📊 Market Data Comparison using Yahoo Finance & Alpha Vantage

## Overview

This project compares **Daily OHLCV (Open, High, Low, Close, Volume)** market data obtained from two independent financial data providers: **Yahoo Finance** and **Alpha Vantage**.

The objective is to validate the consistency of historical market data by identifying discrepancies between the two sources for the last **100 trading days** across **10 actively traded US stocks**.

---

## Objectives

* Retrieve historical Daily OHLCV data from two free market data providers.
* Clean and standardize the datasets into a common format.
* Compare all five OHLCV attributes on a day-by-day basis.
* Detect and report discrepancies between the two sources.
* Generate detailed comparison reports and an overall summary.

---

## Data Sources

* **Yahoo Finance** (via `yfinance`)
* **Alpha Vantage** (REST API)

---

## Symbols Compared

| Symbol | Company                |
| ------ | ---------------------- |
| AAPL   | Apple Inc.             |
| MSFT   | Microsoft Corporation  |
| GOOGL  | Alphabet Inc.          |
| AMZN   | Amazon.com Inc.        |
| META   | Meta Platforms Inc.    |
| TSLA   | Tesla Inc.             |
| NVDA   | NVIDIA Corporation     |
| AMD    | Advanced Micro Devices |
| NFLX   | Netflix Inc.           |
| INTC   | Intel Corporation      |

---

## Project Workflow

```text
Fetch Yahoo Finance Data
            │
            ▼
Fetch Alpha Vantage Data
            │
            ▼
Data Cleaning & Standardization
            │
            ▼
Merge Datasets on Date
            │
            ▼
Compare OHLCV Attributes
            │
            ▼
Identify Discrepancies
            │
            ▼
Generate Detailed Reports
```

---

## Project Structure

```text
market-data-comparison/
│
├── data/
│   ├── yahoo/
│   └── alpha/
│
├── comparison/
│   ├── AAPL_comparison.csv
│   ├── AAPL_mismatches.csv
│   ├── ...
│   └── comparison_summary.csv
│
├── yahoo_fetch.py
├── alpha_fetch.py
├── compare.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Data Cleaning

Before comparison, both datasets are standardized by:

* Renaming columns to a common schema
* Removing unnecessary columns
* Converting numeric values to appropriate data types
* Parsing dates into a consistent format
* Sorting records chronologically
* Removing duplicate entries
* Keeping the most recent 100 trading days

---

## Comparison Methodology

Each trading day is compared across the following attributes:

* Open
* High
* Low
* Close
* Volume

For each attribute, the absolute difference is calculated.

Example:

```
Open Difference = |Yahoo Open − Alpha Open|
```

A trading day is marked as a **Match** when all OHLCV values fall within the defined tolerance. Otherwise, it is classified as a **Mismatch**.

---

## Technologies Used

* Python 3
* Pandas
* Requests
* yfinance
* Alpha Vantage API

---

## Output

The project generates:

### Detailed Comparison

For every symbol:

* Complete merged dataset
* Absolute difference for each OHLCV field
* Match / Mismatch status

Example:

```
comparison/
├── AAPL_comparison.csv
├── MSFT_comparison.csv
├── ...
```

### Mismatch Report

Contains only records where discrepancies were detected.

Example:

```
comparison/
├── AAPL_mismatches.csv
├── MSFT_mismatches.csv
├── ...
```

### Summary Report

The summary includes:

* Total trading days compared
* Matching days
* Mismatch days
* Maximum Open difference
* Maximum High difference
* Maximum Low difference
* Maximum Close difference
* Maximum Volume difference

---

## Results

### Overall Findings

* Successfully compared **10 US stocks** across **99–100 trading days**.
* Approximately **95% of trading days matched** across both providers.
* Price differences were minimal, with a maximum observed difference of approximately **0.005 USD**.
* Larger discrepancies were observed in trading volume, which is expected due to differences in data aggregation and reporting methodologies between providers.

---

## Key Observations

* Daily **Open, High, Low, and Close** prices from Yahoo Finance and Alpha Vantage are highly consistent.
* Minor price differences are primarily attributable to rounding precision and provider-specific processing.
* Trading volume exhibits greater variation because different market data vendors may aggregate or update volume data differently.
* The overall comparison indicates a high level of consistency between the two data sources for daily OHLC data.

---

## Future Improvements

* Support additional market data providers.
* Compare adjusted prices and corporate actions.
* Generate visual discrepancy reports using charts.
* Automate daily comparisons through scheduled execution.
* Export reports in Excel and PDF formats.
* Build an interactive dashboard for data quality monitoring.

---

## How to Run

### Clone the repository

```bash
git clone https://github.com/<your-username>/market-data-comparison.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Fetch market data

```bash
python yahoo_fetch.py
python alpha_fetch.py
```

### Compare datasets

```bash
python compare.py
```

Generated reports will be available in the `comparison/` directory.

---

## Author

**Siddhesh Pote**

B.Tech Computer Science & Engineering
MIT ADT University

---

## License

This project is intended for educational and learning purposes.
