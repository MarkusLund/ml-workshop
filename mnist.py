import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense

# Split data in training and test set
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

model = Sequential()
model.add(Dense(10, input_shape=(784,), activation='softmax'))

model.compile(loss=None,
              optimizer=None,
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    epochs=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])