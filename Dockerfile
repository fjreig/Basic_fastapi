FROM python:3.10-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
 

CMD ["uvicorn", "fastapiredis.application:app", "--host", "0.0.0.0", "--port", "80"]
