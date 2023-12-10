import pandas as pd
import numpy as np
import yfinance as yf

# File downloaded from Korean Stock Exchange

filename = "data_1811_20231129.csv"


def ticker_list_mc(filename):
    df = pd.read_csv(filename, encoding='unicode_escape')
    df = df[df.Market == 'KOSPI']
    df_mc = df[['Ticker', 'Market Capitalization']]
    sorted_df = df_mc.sort_values('Market Capitalization', ascending=False)
    return sorted_df['Ticker'].to_numpy()



def company_info(tick_list):
    info = []
    for ticks in tick_list:
        try:
            comp_info = []
            comp_info.append(ticks)
            for i in ['shortName', 'industry', 'sector']:
                comp_info.append(yf.Ticker(ticks + ".KS").info[i])
            info.append(comp_info)
        except KeyError:
            pass
    info_df = pd.DataFrame(info, columns = ["Ticker", "Name", "Industry", "Sector"])
    return info_df



if __name__ == '__main__':
    tick_list = ticker_list_mc(filename)
    print(company_info(tick_list))