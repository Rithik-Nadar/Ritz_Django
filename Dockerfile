
From python:3.8.10
RUN mkdir Ritz_Django
WORKDIR /Ritz_Django
ADD . /Ritz_Django
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000
