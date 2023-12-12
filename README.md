# Stock Market Predictions using LSTM Models
Written by TJ Kim for Fall 2023 Software Carpentry Final Project
## Project Background
Stock market prediction is gaining more attention as machine learning models are getting developed to higher levels. Stock market data usually includes timeseries data, where the values (such as opening prices or closing prices) change every day. A common model to predict stock market prices is Long Short-Term Memory model, or LSTM in short.

![Visualization of LSTM Model](https://media.geeksforgeeks.org/wp-content/uploads/newContent1.png)

### About LSTM
LSTM is a improved version of recurrent neural network (RNN) model. LSTM is good for sequence prediction tasks and excels in capturing long-term dependencies. Traditional RNNs have single hidden state passed through time, making it difficult for the network to learn long-term dependencies. Compared to RNNs, LSTM includes a memory cell, which can contain information for a longer period. This makes LSTM appropriate for applications such as time-series forecasting. The long-term dependency of the LSTM model is controlled by three gates; intput gate which decides what input is added to the memory cell, forget gate which decides what information is removed from the memory cell, and output gate which decides what output leaves the memory cell.

### LSTM Model used in this program
LSTM model is established in **LSTM_Model.py**. 

## Required Module/API
There are several modules that are used for this program. Installation may be required depending on user environment.
- numpy: Used to create numpy arrays
- pandas: Used to create and process dataframes
- matplotlib.pyplot: Used to visualize data and create relevant graphs
- sklearn.preprocessing: Uses MinMaxScaler() module to scale stock price data for ML processing
- tensorflow.keras: API to develop deeplearning models
- [yfinance](https://pypi.org/project/yfinance/): API to scrape stock data from [Yahoo Finance](https://finance.yahoo.com/)
## Code Structure and Running the Program
### Code Structure
#### csv_processing.py
This file processes the csv data that was downloaded from [Korea Exchange Market Database](http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd?locale=en). The csv file was downloaded on November 29, 2023 for use in the project. Raw csv file is also included in the github.

#### stock_data.py
This file collects stock price data from Yahoo Finance using yfinance API to create a dataframe and includes function to visualize the closing price of companies 

#### LSTM_Model.py
This file includes function that develops LSTM model for stock market predictions.

#### final_results.py
This file contains function to plot actual stock price and predicted stock price calculated from LSTM model.

#### run_program.py
This file contains main block where user can input relevant parameters which include number of companies, sector of interest, and start/end date of interest to create a final graph that includes plots of actual price and LSTM model predicted price.

### Running the Program
Running the program is simple as user only needs to access the run_program.py. In the main block of run_program.py, the code is structured as following with in two lines of hashtags:
```python
n = 4
sector = None
start_date = '2020-12-01'
end_date = '2023-12-01'
```

Input Categories:
- n (int): number of companies to analyze that is obtained from high to low market capitalization size
- sector (string): sector of interest; sectors (as listed from Yahoo Finance) include "Technology", "Financial Services", "Healthcare", "Consumer Cyclical", "Industrials", "Communication Services", "Consumer Defensive", "Energy", "Basic Materials", "Real Estate", "Utilities". None can be typed if no sector needs to be specified.
- start_date/end_date = String of start date and end date in the format of 'YYYY-MM-DD'.

After appropriate inputs are recorded the user just needs to simply run run_program.py to create plots that include actual stock data and predicted stock data.

For **4 companies** (`n = 4`) with **unspecified sector** (`sector = None`) with **start date as December 1st, 2020** (`start_date = '2020-12-01'`) and **end date as December 1st, 2023** (`end_date = '2023-12-01'`), the figure is as following! 
![n4sNone2020120120231201](https://github.com/rlaxowjdkr/F23-SC-Final-Project/blob/main/Plots/4_None.png)
## References

