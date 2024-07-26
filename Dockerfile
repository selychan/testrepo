
FROM python:3.10-slim


WORKDIR C:\Users\Thinkpad\testrepo


COPY requirements.txt /app


RUN pip install --no-cache-dir -r requirements.txt


COPY . /app


CMD ["python", "app.py"]
