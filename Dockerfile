FROM python:3.8

# Set the working directory in the container
WORKDIR /src

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py ./main.py

# Run main.py when the container launches
CMD [ "python", "main.py" ]