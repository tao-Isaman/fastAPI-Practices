FROM python:3.9.0a5-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add gcc
RUN mkdir /code
COPY . /code/
WORKDIR /code
RUN mkdir ~/.kube
RUN mv ./config ~/.kube/config
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# CMD ["uvicorn" "main:app"]