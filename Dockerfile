FROM python:3.10-alpine

COPY . /src
WORKDIR /src
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
CMD ["gunicorn", "--chdir", "/src", "wsgi:app", "--bind", "0.0.0.0:5001"]