FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD req.txt /code/
RUN pip install -r req.txt
COPY . /code/
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "8080"]
