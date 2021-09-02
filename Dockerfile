FROM python:3.8.6-buster
COPY api /api
COPY requirements.txt /requirements.txt
COPY data /data
COPY predict.py /predict.py
#COPY predict.py /predict.py
#COPY Makefile /Makefile
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn api.fast:app --host 0.0.0.0