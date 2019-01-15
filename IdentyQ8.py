#Question8
import numpy as np
import pandas
from keras.models import Sequential
from keras.layers import Dense
Y=np.random.rand(10)
X=np.random.rand(10)
Z = X*0.12 + Y*0.45

model = Sequential()
model.add(Dense(units=200, input_dim=1))
model.add(Activation('relu'))
model.add(Dense(units=45))
model.add(Activation('relu'))
model.add(Dense(units=1))

model.compile(loss='mean_squared_error',
              optimizer='rmsprop')

model.fit(X, Y, Z, epochs=10, batch_size=50, verbose=1)

