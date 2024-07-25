# using Python 3.10 image
FROM python:3.10-slim

# working path
WORKDIR /app


COPY requirements requirements.txt

 
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


CMD ["python", "app/app.py"]
