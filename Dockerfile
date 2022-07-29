FROM python:3

RUN apt-get update && apt-get install

RUN mkdir /codet
WORKDIR /codet

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./req.txt /codet
RUN pip install -r req.txt
ADD . /codet

EXPOSE 8020
CMD ["python", "manage.py", "runserver", "0.0.0.0:8020"]
