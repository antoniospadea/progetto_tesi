# Usa una immagine di base con Python 3.9 slim
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /analizzatore-energetico

# Copia il file requirements.txt nella directory di lavoro del container
COPY requirements.txt /analizzatore-energetico/

# Installa le dipendenze di Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il contenuto della cartella analizzatore-energetico nel container
COPY . /analizzatore-energetico

# Esponi la porta 8000 (o un'altra porta se necessario)
EXPOSE 8000

# Imposta la variabile di ambiente per dire a Flask dove si trova l'applicazione
ENV FLASK_APP=app  
# Poiché l'app Flask è in /analizzatore-energetico/app/__init__.py

# Esegui i test
RUN python -m unittest discover -s tests

# Comando per eseguire l'app Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
