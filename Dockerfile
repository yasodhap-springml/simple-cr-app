FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# Open port 8080 for serving the webpage
EXPOSE 8088

# Run app.py when the container launches
CMD ["python3", "app.py"]