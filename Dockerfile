FROM python:3.7

WORKDIR /app/
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y graphviz
RUN python -c "import keras; from keras.datasets import mnist; mnist.load_data()"

COPY . ./

CMD ["python", "mnist.py"]
