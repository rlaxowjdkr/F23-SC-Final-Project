from LSTM_Model import RNN_LSTM
from final_results import plot_closing_price
from stock_data import company_list, get_stock_data

"""
This file runs the program to plot the figures of actual and predicted stock 
prices.
"""

if __name__ == '__main__':
    ###########################################################################
    # INPUTS
    # Number of companies interested
    n = 4

    # Sector of interest (can be none, which will not specify a sector)
    sector = 'Technology'

    # Specifies start and end date for period of interest
    # In 'YYYY-MM-DD' format
    start_date = '2020-12-01'
    end_date = '2023-12-01'

    ###########################################################################

    # Running the program from inputs
    df = get_stock_data(company_list(n, sector), start_date, end_date)
    data = []
    for i in range(n):
        data.append(RNN_LSTM(df[i]))
    plot_closing_price(company_list(n, sector), data)
