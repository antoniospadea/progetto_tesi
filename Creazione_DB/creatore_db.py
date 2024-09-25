import os
from sqlalchemy import Column, String, Float, Integer, create_engine, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import json

# Definizione della base per il modello ORM
Base = declarative_base()

# Definizione della tabella per i dati catastali
class Catasto(Base):
    __tablename__ = 'catasto'

    codice_appartamento = Column(String, primary_key=True)  # Codice Alfanumerico appartamento
    tipologia_appartamento = Column(String)  # Residenziale, Commerciale, Condominiale
    heating = Column(Float)  # Consumo di riscaldamento
    electricity_consumption = Column(Float)  # Consumo elettrico
    insulation = Column(Float)  # Isolamento
    piano = Column(Integer)  # Piano
    production = Column(Text)  # Produzione memorizzata come stringa JSON

# Percorso per la directory Creazione_DB
db_directory = r'C:\Users\Antonio\Desktop\progetto_tesi\Creazione_DB'

# Percorso per salvare il database nella cartella Creazione_DB
db_path = os.path.join(db_directory, 'catasto.db')

# Creazione del motore del database (SQLite in questo caso)
engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)

# Creazione della sessione per le operazioni sul database
Session = sessionmaker(bind=engine)
session = Session()

# Funzione per convertire l'array in JSON, se presente
def converti_in_json(valore):
    """
    Questa funzione prende un valore. Se il valore rappresenta un array, lo converte in JSON.
    Se è un singolo numero, lo restituisce così com'è.
    """
    try:
        if '[' in str(valore) and ']' in str(valore):
            array_valori = [float(x) for x in valore.strip('[]').split(',')]
            return json.dumps(array_valori)  # Convertiamo l'array in JSON
        else:
            return json.dumps(float(valore))  # Convertiamo il singolo valore in JSON
    except Exception as e:
        print(f"Errore nella conversione in JSON: {e}")
        return json.dumps(0)  # In caso di errore, restituiamo 0 come default

# Funzione per popolare il database dal CSV
def popola_db(csv_file):
    # Carichiamo i dati dal CSV
    df = pd.read_csv(csv_file)

    for _, row in df.iterrows():
        # Applichiamo la funzione converti_in_json per il campo production
        production = converti_in_json(row['production'])

        # Creiamo un nuovo record per il database
        nuovo_appartamento = Catasto(
            codice_appartamento=row['codice_appartamento'],
            tipologia_appartamento=row['tipologia_appartamento'],
            heating=row['heating'],
            electricity_consumption=row['electricity_consumption'],
            insulation=row['insulation'],
            piano=row['piano'],
            production=production
        )

        # Aggiungiamo il record alla sessione
        session.add(nuovo_appartamento)

    # Facciamo il commit per salvare tutti i dati nel database
    session.commit()
    print("Dati inseriti nel database con successo.")

# Percorso assoluto del CSV nella stessa directory Creazione_DB
csv_file_path = os.path.join(db_directory, 'dati_catasto.csv')

# Esegui la funzione con il percorso corretto del CSV
popola_db(csv_file_path)

# Conferma finale che il database è stato creato correttamente
print("Database creato correttamente e popolato.")







