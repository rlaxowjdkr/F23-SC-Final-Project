import matplotlib.pyplot as plt
import yfinance as yf

from csv_processing import ticker_list_mc, company_info, ticker_name_dict

"""
This file collects stock price data into dataframe and graph (visualization).

The first function creates a list of tickers that includes n companies with 
highest market capitalization in certain sector (or none) for further analysis.
The second function uses yfinance API to obtain stock data provided by yahoo 
finance and stores into a dataframe. Then multiple dataframes from multiple 
companies are stored into a list of dataframes.
The third function creates plots of the closing prices of stocks in certain 
time period for all companies of interest.
"""


# Creates list of company to analyze
def company_list(n, sector=None):
    """
    This function creates a list of tickers that includes companies in
    certain sector (or none).

    :param n: Integer that represents number of companies of interest in the
    list of high to low market capitalization
    :param sector: String to indicate sector of interest (default is set to
    none, which will include all the sectors)
    :return: List of ticker numbers for companies that will be analyzed
    """

    # Grab dataframe with all stock information
    master_df = company_info(ticker_list_mc())
    # Raise error if number of companies to analyze is invalid
    if n < 1:
        raise Exception("Need at least 1 company to analyze!")
    # Raise error if sector does not exist
    if sector not in ["Technology", "Financial Services", "Healthcare",
                      "Consumer Cyclical", "Industrials",
                      "Communication Services", "Consumer Defensive", "Energy",
                      "Basic Materials", "Real Estate", "Utilities", None]:
        raise Exception("Sector does not exist!")
    # Create list of tickers for n highest market capitalization companies
    # when sector is not specified.
    elif sector is None:
        df_ns = master_df.head(n)
        return df_ns['Ticker'].tolist()
    # Create list of tickers for n highest market capitalization companies
    # when sector IS specified.
    else:
        df_ys = master_df.loc[master_df['Sector'] == sector]
        df_ys2 = df_ys.head(n)
        return df_ys2['Ticker'].tolist()


def get_stock_data(ticker_list, startdate, enddate):
    """
    This function inputs list of ticker numbers of companies to analyze,
    desired start date, and desired end date to obtain a LIST of dataframe
    that includes stock information for all companies of interest.

    :param ticker_list: List of ticker numbers
    :param startdate: String that represents start date in format of
    'YYYY-MM-DD'
    :param enddate: String that represents end date in format of 'YYYY-MM-DD'
    :return: LIST of dataframes where each dataframe includes stock
    information of respective companies
    """

    list_df = []
    # Using yfinance obtain stock information in certain range of dates and
    # store them into dataframe for each company. Then append all dataframes
    # into a single list.
    for ticker in ticker_list:
        data = yf.Ticker(ticker).history(start=startdate, end=enddate)
        list_df.append(data)
    return list_df


def plot_closing_price(company_list, df_list):
    """
    This function creates plots of closing stock prices of companies.

    :param company_list: List of company names to be analyzed
    :param df_list: List of dataframes that includes stock information of
    companies to be analyzed
    """

    total = len(df_list)
    # Dynamically adjusts the figure depending on number of figures
    cols = 2
    rows = total // cols
    if total % cols != 0:
        rows += 1
    position = range(1, total + 1)

    # Creates plots using matplotlib on the closing prices of the companies
    # based on dataframe of stock information provided
    fig = plt.figure(1, figsize=(15, 12))
    plt.subplots_adjust(hspace=0.5)
    plt.suptitle("DAILY CLOSING PRICES", fontsize=20, y=0.95)

    # Loops for all companies
    for k in range(total):
        ax = fig.add_subplot(rows, cols, position[k])
        ax.plot(df_list[k].index, df_list[k]['Close'])
        ax.set_title(ticker_name_dict().get(company_list[k]).upper())
        ax.tick_params(axis='x', labelrotation=45)
        ax.set_xlabel("Date")
        ax.set_ylabel("KR WON")
    plt.show()


if __name__ == '__main__':
    pass
