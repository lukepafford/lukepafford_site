FROM python:3.7

WORKDIR /

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "gunicorn", "-b", "0.0.0.0:9000", "lukepafford_blog.wsgi" ]
