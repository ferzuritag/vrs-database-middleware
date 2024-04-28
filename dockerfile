# Usa la imagen base mongo:7.0
FROM mongo:7.0

# Copiar el proyecto a la carpeta /app
COPY . /app

WORKDIR /app

# Instala Python 3 y pip
RUN apt-get update && apt-get install -y python3 python3-pip && pip install -r requirements.txt

CMD ["uvicorn main:app --port 80"]

EXPOSE 80