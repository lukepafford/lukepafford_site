FROM python:3.7

WORKDIR /

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

CMD [ "gunicorn", "lukepafford_blog.wsgi" ]
