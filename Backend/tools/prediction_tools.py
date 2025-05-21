# from langchain.tools import tool
from crewai.tools import tool
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime


@tool("trend_predictor_tool")
def trend_predictor_tool(ticker: str) -> str:
    """
    Analyzes stock price trend and financials to predict growth potential.

    Args:
        ticker (str): Ticker symbol (e.g., "AAPL")

    Returns:
        str: Trend analysis report
    """
    try:
        stock = yf.Ticker(ticker)

        # Step 1: Stock Price Trend Analysis (1-Year)
        hist = stock.history(period="2y")
        if hist.empty:
            return "No historical price data available for this ticker."

        hist = hist.reset_index()
        hist['Date_ordinal'] = hist['Date'].map(datetime.toordinal)
        X = hist[['Date_ordinal']]
        y = hist['Close']
        model = LinearRegression()
        model.fit(X, y)

        # Predict 30 days ahead
        future_date = pd.Timestamp.today() + pd.Timedelta(days=30)
        future_ordinal = np.array([[future_date.toordinal()]])
        future_price = model.predict(future_ordinal)[0]
        current_price = y.iloc[-1]
        growth_pct = (future_price - current_price) / current_price * 100

        trend_msg = (
            f"Stock Trend → Current: ${current_price:.2f}, "
            f"Predicted (30d): ${future_price:.2f} ({growth_pct:.2f}%).\n"
        )

        # Step 2: Financial Analysis from Income Statement
        fin = stock.financials
        if fin.empty:
            return trend_msg + "Financial data not available to strengthen prediction."

        revenue = fin.loc["Total Revenue"].dropna()
        net_income = fin.loc["Net Income"].dropna()

        # Revenue growth (last year vs previous)
        if len(revenue) >= 2 and len(net_income) >= 2:
            rev_growth = ((revenue[0] - revenue[1]) / revenue[1]) * 100
            profit_growth = ((net_income[0] - net_income[1]) / abs(net_income[1])) * 100

            fin_msg = (
                f"Revenue Growth (YoY): {rev_growth:.2f}%\n"
                f"Net Income Growth (YoY): {profit_growth:.2f}%\n"
            )

            if growth_pct > 5 and rev_growth > 5 and profit_growth > 5:
                outlook = "📈 Strong positive trend based on both stock and financials."
            elif growth_pct > 0 and rev_growth > 0:
                outlook = "📊 Moderate growth potential."
            else:
                outlook = "📉 Weak or uncertain growth trend."
        else:
            fin_msg = "Not enough financial history for revenue/profit comparison.\n"
            outlook = "📊 Partial analysis based only on stock trend."

        return trend_msg + fin_msg + outlook

    except Exception as e:
        return f"Error during analysis: {str(e)}"

# print(trend_predictor_tool("AAPL"))