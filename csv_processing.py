import pandas as pd
import numpy as np
import yfinance as yf

# File downloaded from Korean Stock Exchange

def ticker_list_mc(filename):
    df = pd.read_csv(filename, encoding='unicode_escape')
    df_mc = df[['Ticker', 'Market Capitalization']]
    sorted_df = df_mc.sort_values('Market Capitalization', ascending=False)
    return sorted_df['Ticker'].to_numpy()





if __name__ == '__main__':
    print(ticker_list_mc("data_1811_20231129.csv"))