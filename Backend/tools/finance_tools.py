from crewai.tools import tool
import yfinance as yf

@tool("get_financial_summary")
def get_financial_summary(company_ticker: str) -> str:
    """
        Fetch and return a summary of financial information for the given company ticker using Yahoo Finance.

        This includes company name, sector, market cap, revenue, profit margin, current price,
        52-week high and low values.
    """
    try:
        stock = yf.Ticker(company_ticker)
        info = stock.info
        summary = f"""
        Company: {info.get('longName')}
        Sector: {info.get('sector')}
        Market Cap: {info.get('marketCap')}
        Revenue: {info.get('totalRevenue')}
        Profit Margin: {info.get('profitMargins')}
        Current Price: {info.get('currentPrice')}
        52 Week High: {info.get('fiftyTwoWeekHigh')}
        52 Week Low: {info.get('fiftyTwoWeekLow')}
        """
        return summary.strip()
    except Exception as e:
        return f"Error fetching financial data: {e}"

# print(get_financial_summary("AAPL"))
