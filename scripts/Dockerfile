FROM python:3.7

WORKDIR /

COPY requirements.txt ./
RUN pip3 install -U --no-cache-dir -r requirements.txt
RUN mkdir /data

CMD [ "gunicorn", "-w", "2", "--bind=0.0.0.0:9000", "lukepafford_blog.wsgi" ]
