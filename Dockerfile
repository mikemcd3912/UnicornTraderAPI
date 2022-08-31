FROM python:3.9.1
ADD . /UnicornTraderAPI
WORKDIR /UnicornTraderAPI
RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python3", "api.py"]