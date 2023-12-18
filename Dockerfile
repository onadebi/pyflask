FROM python:3.10-slim

WORKDIR /app
EXPOSE 5000

#COpy current contents into app directory
COPY . /app

#Install needed dependencies
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

RUN pwd

# ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]

ENTRYPOINT ["gunicorn","-b",":5000","main:app"]