import pandas as pd
import yfinance as yf


# Creates list of ticker numbers in descending order of Market
# Capitalization (Largest to smallest capital)
def ticker_list_mc(filename="data_1811_20231129.csv"):
    df = pd.read_csv(filename, encoding='unicode_escape')
    df = df[df.Market == 'KOSPI']
    df_mc = df[['Ticker', 'Market Capitalization']]
    sorted_df = df_mc.sort_values('Market Capitalization', ascending=False)
    return sorted_df['Ticker'].to_numpy()


# Creates dataframe that includes information of all companies
def company_info(tick_list):
    info = []
    for ticks in tick_list[:50]:
        try:
            comp_info = []
            comp_info.append(ticks + ".KS")
            for i in ['shortName', 'marketCap', 'sector']:
                comp_info.append(yf.Ticker(ticks + ".KS").info[i])
            info.append(comp_info)
        except KeyError:
            pass
    info_df = pd.DataFrame(info,
                           columns=['Ticker', "Name", 'Market Capitalization',
                                    "Sector"])
    return info_df


# Creates dictionary with tickers as key and company name as values
def ticker_name_dict():
    tnd = pd.Series(company_info(ticker_list_mc()).Name.values,
                    company_info(ticker_list_mc()).Ticker.values).to_dict()
    return tnd


if __name__ == '__main__':
    print(company_info(ticker_list_mc()[:50]).to_string())
    print(ticker_name_dict())
