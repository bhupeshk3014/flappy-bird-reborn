"""
The design of this comes from here:
http://outlace.com/Reinforcement-Learning-Part-3/
"""

from keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import Callback

class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

def neural_net(num_sensors, params, load=''):
    model = Sequential()

    # First layer
    model.add(Dense(params[0], kernel_initializer='lecun_uniform', input_shape=(num_sensors,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    # Second layer
    model.add(Dense(params[1], kernel_initializer='lecun_uniform'))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    # Output layer
    model.add(Dense(2, kernel_initializer='lecun_uniform'))
    model.add(Activation('linear'))

    # Compile Model
    rms = RMSprop()
    model.compile(loss='mse', optimizer=rms)

    # Load Pre-trained Model (if provided)
    if load:
        model.load_weights(load)

    return model
