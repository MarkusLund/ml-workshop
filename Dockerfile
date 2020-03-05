FROM python:3.7

WORKDIR /app/
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y graphviz

COPY . ./

CMD ["python", "mnist.py"]
