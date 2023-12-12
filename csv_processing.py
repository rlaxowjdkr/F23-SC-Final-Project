import pandas as pd
import yfinance as yf

"""
This file processes the csv data that was downloaded online from Korea 
Exchange online database. 
The first function creates a numpy array of Tickers of traded companies in 
the KOSPI market from highest to lowest market capitalization.
The second function creates a dataframe using stock information obtained 
from yahoo finance using yfinance API, and contains information on ticker, 
name of company, market capitalization and the sector it belongs in.
The third function create a dictionary with ticker as the key and name of 
company as the value.
"""


def ticker_list_mc(filename="data_1811_20231129.csv"):
    """
    This function creates array of Tickers of traded companies in KOSPI
    market from highest to lowest market capitalization.

    :param filename: Filename of csv file downloaded from database
    :return: Array of Ticker numbers
    """

    # Ensure the encoding recognizes Korean characters
    df = pd.read_csv(filename, encoding='unicode_escape')
    # Obtain data only from KOSPI market (biggest market in Korea)
    df = df[df.Market == 'KOSPI']
    df_mc = df[['Ticker', 'Market Capitalization']]
    # Sort by highest to lowest market capitalization size
    sorted_df = df_mc.sort_values('Market Capitalization', ascending=False)
    return sorted_df['Ticker'].to_numpy()


def company_info(tick_list):
    """
    This function creates a dataframe using stock information obtained from
    yahoo finance using yfinance API that includes information on ticker,
    name, market capitalization size and sector it belongs to.

    :param tick_list: Array of ticker numbers
    :return: Pandas dataframe
    """

    info = []
    # Loop through each ticker number in the list, for 100 highest market
    # capitalization size companies
    for ticks in tick_list[:100]:
        try:
            comp_info = []
            # Append .KS at the end of ticker number for use in yfinance API
            comp_info.append(ticks + ".KS")
            for i in ['shortName', 'marketCap', 'sector']:
                comp_info.append(yf.Ticker(ticks + ".KS").info[i])
            info.append(comp_info)
        # Yahoo Finance database does not always include all information,
        # so bypass any companies with missing info
        except KeyError:
            pass
    # Create a dataframe that includes all information, assign column names
    info_df = pd.DataFrame(info,
                           columns=['Ticker', "Name", 'Market Capitalization',
                                    "Sector"])
    return info_df


def ticker_name_dict():
    """
    This function creates dictionary with ticker as key and name of company
    as the value for future reference.

    :return: Dictionary with ticker as key and name of company as value
    """

    tn_dict = pd.Series(company_info(ticker_list_mc()).Name.values,
                        company_info(ticker_list_mc()).Ticker.values).to_dict()
    return tn_dict


if __name__ == '__main__':
    pass
