import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

"""
This file applies machine learning model, long short-term memory (LSTM) 
model, a type of artificial recurrent neutral network used in deep learning, 
for stock market predictions.

The only function RNN_LSTM, inputs dataframe that includes all stock data, 
user defined timestep, and  to output a dataframe with two columns that 
actual stock data and predicted stock data using the ML model. 
"""


def RNN_LSTM(df, timestep=60, ep=50):
    """
    This function inputs dataframe containing time series stock data and
    timestep used in the model, and epochs (set at 50 initially) to put
    another dataframe that contains two information: actual price of the
    test set data and predicted price of test set data.

    :param df: Dataframe that contains single column of timeseries data
    :param timestep: Integer for timestep in the model
    :param ep: Integer for epochs in the model
    :return: Dataframe that contains two column of test data: First column
    represents the actual stock price value from the market, Second column
    represents the predicted stock price value using the train set data.
    """

    # Scale down data so that it can be trained efficiently using function
    # from sklearn
    scaler = MinMaxScaler(feature_range=(0, 1))

    # Set the number that separates training set and test set
    # 80% of the data as training set and 20% of the data as testing set
    train80 = int(df.shape[0] * 0.8)
    test80 = df.shape[0] - train80

    # Create separate dictionaries with train set data and test set data
    df_train80 = df[:train80]
    df_test20 = df[train80:]

    # Create dictionary with just the "Close" stock price data
    df_close = df.iloc[:, 3:4]

    # Create list of "Close" stock prices, separated into training and
    # testing set
    training_set = df_close.iloc[:train80, :].values
    testing_set = df_close.iloc[train80:, :].values

    # Scale the training set
    training_set_scaled = scaler.fit_transform(training_set)

    x_train = []
    y_train = []

    # 3D array is needed for application of LSTM
    # Create x_train that includes stock data with according timestep in 2D
    # list
    for i in range(timestep, train80):
        x_train.append(training_set_scaled[i - timestep:i, 0])
        y_train.append(training_set_scaled[i, 0])

    # Convert to array
    x_train, y_train = np.array(x_train), np.array(y_train)

    # Reshape train data into 3D Data (stock values, time steps, 1D output)
    # so that it can be used in LSTM model
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Initialize RNN
    model = Sequential()

    # Use 100 neurons and 5 hidden layers for LSTM model
    # Return sequences is True if the sequences are going to be continued to
    # be used for LSTM to fit the dimensions
    # Drop out layer included to prevent over-fitting
    model.add(
        LSTM(units=100, return_sequences=True,
             input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(rate=0.2))
    model.add(
        LSTM(units=100, return_sequences=True))
    model.add(Dropout(rate=0.2))
    model.add(
        LSTM(units=100, return_sequences=True))
    model.add(Dropout(rate=0.2))
    model.add(
        LSTM(units=100, return_sequences=True))
    model.add(Dropout(rate=0.2))
    model.add(
        LSTM(units=100))
    model.add(Dropout(rate=0.2))

    # Assign 1 neuron to predict stock price
    model.add(Dense(1))

    # Compile by calculating loss as mean squared error and use adam optimizer
    model.compile(loss="mean_squared_error", optimizer='adam')

    # Print model summary
    model.summary()

    # Fit model to training set, running for certain number of epochs (
    # running through entire training set) with batch size of 64
    model.fit(x_train, y_train, epochs=ep, batch_size=64)

    # Reshape and process test data similar to training data
    combined_data = pd.concat([df_train80['Close'], df_test20['Close']],
                              axis=0)
    test_entry = combined_data[
                 len(combined_data) - len(df_test20) - timestep:].values
    test_entry = test_entry.reshape(-1, 1)
    test_entry = scaler.transform(test_entry)

    x_test = []
    for i in range(timestep, timestep + test80):
        x_test.append(test_entry[i - timestep:i, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    # Predict stock price using test data using the model and transform
    # scaled values back to normal stock values
    test_predicted = model.predict(x_test)
    test_predicted = scaler.inverse_transform(test_predicted)

    # Create a dataframe that places actual stock prices and predicted stock
    # prices from test data
    new_data = pd.concat([df_close.iloc[train80:, :].copy(),
                          pd.DataFrame(test_predicted,
                                       columns=['Predicted Close'],
                                       index=df_close.iloc[train80:,
                                             :].index)], axis=1)

    return new_data


if __name__ == '__main__':
    pass
