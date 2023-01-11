# FROM python
# ENV PYTHONUNBUFFERED 1
# WORKDIR /code
# ADD requirement.txt requirement.txt
# RUN pip install -r requirement.txt
# COPY . .
# RUN ls
# RUN pwd
# RUN cat env/.env
# EXPOSE 8001
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# CMD ["python", "manage.py", "runserver", "8001"]

FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
ADD requirement.txt requirement.txt
RUN pip install -r requirement.txt
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"
COPY . .
