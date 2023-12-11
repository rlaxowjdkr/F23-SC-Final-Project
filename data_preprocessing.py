import matplotlib.pyplot as plt
import yfinance as yf

from csv_processing import ticker_list_mc, company_info, ticker_name_dict

# Creates list of company to analyze
def company_list(n, sector=None):
    df0 = company_info(ticker_list_mc())
    if sector is None:
        df1 = df0.head(n)
        return df1['Ticker'].tolist()
    else:
        df_s = df0.loc[df0['Sector'] == sector]
        df2 = df_s.head(n)
        return df2['Ticker'].tolist()

# Stores dataframe of stock data into a list
def get_stock_data(list, startdate, enddate):
    list_df = []
    for ticker in list:
        data = yf.Ticker(ticker).history(start=startdate, end=enddate)
        list_df.append(data)
    return list_df

# Plots closing price
def plot_closing_price(df_list):
    total = len(df_list)
    cols = 2
    rows = total // cols
    if total % cols != 0:
        rows += 1
    position = range(1, total + 1)

    fig = plt.figure(1, figsize=(15, 12))
    plt.subplots_adjust(hspace=0.5)
    plt.suptitle("DAILY CLOSING PRICES", fontsize=20, y=0.95)

    for k in range(total):
        ax = fig.add_subplot(rows, cols, position[k])
        ax.plot(df_list[k].index, df_list[k]['Close'])
        ax.set_title(ticker_name_dict().get(company_list(total)[k]).upper())
        ax.tick_params(axis='x', labelrotation=45)
    plt.show()


if __name__ == '__main__':
    df = get_stock_data(company_list(5, "Technology"), '2022-11-01',
                        '2022-12-31')
    plot_closing_price(df)
