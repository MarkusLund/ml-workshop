# Machine Learning workshop

In this workshop you will learn how to create an image recognizion machine learning algorithm using Python and Keras.

## Dataset

We will use the MNIST dataset during the workshop.

28x28 pictures of hand written digits.

## Environment

- Python 3.7+
- Keras as Machine Learning framework
- Python requirements can be installed with `pip` and the `requirements.txt` file.

## Tasks

### 1. Setup the environment

```bash
pip install -r requirements.txt
```

## Tips & tricks

- Does the network take a long time to train? What about letting the loss function look at multiple traning examples simultainously?

### Adjust the data

Adjusting and tweaking the data can improve the result as well as make it easier to use.

Built-in functions which will be useful.

- `.reshape()` Can be used on numpy matrices .
- `.astype()` Can be used on numpy matrices .
- You will like this function -> `keras.utils.to_categorical`

### Visualization of the network/model

#### Textual visualization

```python
model.summary()
```

#### Generating a picture

```python
from keras.utils import plot_model
plot_model(model, to_file='model.png', show_shapes=True)
```

PS: Generating an image requires the following packages.

- pydot - `pip install pydot`
- graphviz - `brew install graphviz`
