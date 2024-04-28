# Using mongo 7.0 image
FROM mongo:7.0

WORKDIR /app

# Copy the folder on /app
COPY . .

# Install python 3
RUN apt-get update && apt-get install -y python3 python3-pip && pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--port 80", "--host 0.0.0.0"]