# Machine Learning workshop

In this workshop you will learn how to create an image recognizion machine learning algorithm using Python and Keras.

## Dataset

We will use the MNIST dataset during the workshop.

28x28 pictures of hand written digits.

## Environment

- Python 3.7+
- Keras as Machine Learning framework
- Python requirements can be installed with `pip` and the `requirements.txt` file.

## Setup

### Installing python

Python and pip are preinstalled on MacOS (and Linux?) but those on Windows need to download and install python.

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

You can then run your code using

```bash
python mnist.py
```

### Using Docker

You can use the provided Dockerfile which will run your script in a linux environment with all dependencies installed. This is the easiest way of running your code if you have Docker installed. I do not however know how much Docker will affect performance.

To run your code in Docker first build a image with

```bash
docker build -t mnist .
```

And then run the code with

```bash
docker run mnist
```

### 2. Train a model which recognizes digits

### 3. Improve your model

There are many techniques for improving your artifical neural network.

### 4. GAN

Why not generate your own unique handwritten digits, without drawing? Generative adversarial networks have become increasingly popular lately. And GANs are not too diffucult to create and train using Keras.

[Look at the GAN markdown file which consists images of what GAN contains.](GAN.md)

## Tips & tricks

- Does the network take a long time to train? What about letting the loss function look at multiple traning examples simultainously?

### Keras has it all

Theres is a lot of nice features and functions in Keras.

I would recommend taking a look at `keras.optimizers` or `keras.losses`. You could of course write your own loss function or optimizer, which would be a great exercise!

### Adjust the data

Your data is everything. Adjusting and tweaking the data can improve the result as well as make it easier to use.

Built-in functions which will be useful.

- `.reshape()` Can be used to reshape numpy matrices. [(Link to docs)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html)
- `.astype('float32)` Can be used to change type of values in numpy matrices. (Hint: if python sees an integer divided by an integer, you will not recieve a decimal number.)
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
