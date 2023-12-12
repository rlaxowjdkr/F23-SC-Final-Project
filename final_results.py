import matplotlib.pyplot as plt

from csv_processing import ticker_name_dict

"""
This file contains one function, which plots the actual stock price and 
predicted stock price calculated from LSTM model. It inputs list of name of 
companies, and list of dataframe of stock information to return a single 
plot that compares the two values.
"""


def plot_closing_price(comp_list, df_list):
    """
    This function creates a plot that compares actual stock price and
    predicted stock price.
    :param comp_list: List containing names of companies
    :param df_list: List of Dataframes containing actual and predicted
    prices of companies
    """
    # Dynamically adjusts size of the figure depending on number of figures
    total = len(df_list)
    cols = 2
    rows = total // cols
    if total % cols != 0:
        rows += 1
    position = range(1, total + 1)

    fig = plt.figure(1, figsize=(15, 12))
    plt.subplots_adjust(hspace=0.5)
    plt.suptitle("DAILY CLOSING PRICES", fontsize=20, y=0.95)

    # Loops through all dataframes to create a plot
    for k in range(total):
        ax = fig.add_subplot(rows, cols, position[k])
        ax.plot(df_list[k].index, df_list[k]['Close'])
        ax.plot(df_list[k].index, df_list[k]['Predicted Close'])
        ax.set_title(ticker_name_dict().get(comp_list[k]).upper())
        ax.tick_params(axis='x', labelrotation=45)
    plt.show()

    # Saves image of the plot named after company names
    plt.savefig("Plot/" + ''.join(ticker_name_dict().get(comp_list).upper()) + '.png')


if __name__ == '__main__':
    pass
