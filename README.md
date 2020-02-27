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

### 2.

## Tips og triks

- Tar det lang tid å trene nettverket? Hva med å se på flere treningsekempler på en gang.
-

### Visualiering av nettverket/modellen

#### Med tekst

```python
model.summary()
```

#### Som bilde

```python
from keras.utils import plot_model
plot_model(model, to_file='model.png', show_shapes=True)
```

PS: Generering av bilde krever:

- pydot - `pip install pydot`)
- graphviz - `brew install graphviz`
