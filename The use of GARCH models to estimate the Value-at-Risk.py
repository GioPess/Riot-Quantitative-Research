# The use of GARCH models to estimate the Value-at-Risk

pip install numpy pandas yfinance arch matplotlib

import yfinance as yf

data = yf.download("^GSPC", start = "2018-01-01", end = "2024-01-01")
data = data["Adj Close"]
