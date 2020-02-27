from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

num_classes = 10
epochs = 1

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(10, input_shape=(784,)))
model.add(Dense(num_classes, activation='softmax'))

model.summary()
from keras.utils import plot_model
plot_model(model, to_file='model.png', show_shapes=True)

model.compile(loss=keras.losses.mean_squared_error,
              optimizer=SGD(learning_rate=0.1),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    epochs=epochs,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])