from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer, Text
import os

# Creazione dell'app Flask
app = Flask(__name__)

# Definizione della base per il modello ORM
Base = declarative_base()

# Definizione della tabella per i dati catastali
class Catasto(Base):
    __tablename__ = 'catasto'

    codice_appartamento = Column(String, primary_key=True)
    tipologia_appartamento = Column(String)
    heating = Column(Float)
    electricity_consumption = Column(Float)
    insulation = Column(Float)
    piano = Column(Integer)
    production = Column(Text)

# Percorso per la directory Creazione_DB
db_directory = r'C:\Users\Antonio\Desktop\progetto_tesi\Creazione_DB'
db_path = os.path.join(db_directory, 'catasto.db')

# Creazione del motore del database (SQLite in questo caso)
engine = create_engine(f'sqlite:///{db_path}')
SessionLocal = sessionmaker(bind=engine)

# Funzione per gestire le sessioni del database
def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Endpoint di base per testare il funzionamento
@app.route('/')
def home():
    return jsonify({'message': 'API di catasto funzionante!'})

# 1. Endpoint per recuperare tutti gli appartamenti
@app.route('/appartamenti', methods=['GET'])
def get_appartamenti():
    session = next(get_db_session())
    appartamenti = session.query(Catasto).all()
    result = []
    for appartamento in appartamenti:
        result.append({
            'codice_appartamento': appartamento.codice_appartamento,
            'tipologia_appartamento': appartamento.tipologia_appartamento,
            'heating': appartamento.heating,
            'electricity_consumption': appartamento.electricity_consumption,
            'insulation': appartamento.insulation,
            'piano': appartamento.piano,
            'production': appartamento.production
        })
    return jsonify(result)

# 2. Endpoint per cercare un appartamento tramite codice_appartamento
@app.route('/appartamenti/<codice_appartamento>', methods=['GET'])
def get_appartamento_by_codice(codice_appartamento):
    session = next(get_db_session())
    appartamento = session.query(Catasto).filter(Catasto.codice_appartamento == codice_appartamento).first()
    if appartamento:
        return jsonify({
            'codice_appartamento': appartamento.codice_appartamento,
            'tipologia_appartamento': appartamento.tipologia_appartamento,
            'heating': appartamento.heating,
            'electricity_consumption': appartamento.electricity_consumption,
            'insulation': appartamento.insulation,
            'piano': appartamento.piano,
            'production': appartamento.production
        })
    else:
        return jsonify({'message': 'Appartamento non trovato'}), 404

# 3. Endpoint per cercare appartamenti in base alla tipologia
@app.route('/appartamenti/tipologia/<tipologia_appartamento>', methods=['GET'])
def get_appartamenti_by_tipologia(tipologia_appartamento):
    session = next(get_db_session())
    appartamenti = session.query(Catasto).filter(Catasto.tipologia_appartamento == tipologia_appartamento).all()
    if appartamenti:
        result = []
        for appartamento in appartamenti:
            result.append({
                'codice_appartamento': appartamento.codice_appartamento,
                'tipologia_appartamento': appartamento.tipologia_appartamento,
                'heating': appartamento.heating,
                'electricity_consumption': appartamento.electricity_consumption,
                'insulation': appartamento.insulation,
                'piano': appartamento.piano,
                'production': appartamento.production
            })
        return jsonify(result)
    else:
        return jsonify({'message': 'Nessun appartamento trovato'}), 404

# 4. Endpoint generico per cercare appartamenti con query su tutte le colonne
@app.route('/appartamenti/search', methods=['GET'])
def search_appartamenti():
    session = next(get_db_session())

    # Prendere i parametri dalla richiesta (ognuno può essere opzionale)
    codice_appartamento = request.args.get('codice_appartamento', None)
    tipologia_appartamento = request.args.get('tipologia_appartamento', None)
    heating_min = request.args.get('heating_min', None)
    heating_max = request.args.get('heating_max', None)
    electricity_min = request.args.get('electricity_min', None)
    electricity_max = request.args.get('electricity_max', None)
    insulation_min = request.args.get('insulation_min', None)
    insulation_max = request.args.get('insulation_max', None)
    piano = request.args.get('piano', None)

    # Iniziare la query
    query = session.query(Catasto)

    # Filtrare in base ai parametri forniti
    if codice_appartamento:
        query = query.filter(Catasto.codice_appartamento.like(f'%{codice_appartamento}%'))
    
    if tipologia_appartamento:
        query = query.filter(Catasto.tipologia_appartamento == tipologia_appartamento)

    if heating_min:
        query = query.filter(Catasto.heating >= float(heating_min))

    if heating_max:
        query = query.filter(Catasto.heating <= float(heating_max))

    if electricity_min:
        query = query.filter(Catasto.electricity_consumption >= float(electricity_min))

    if electricity_max:
        query = query.filter(Catasto.electricity_consumption <= float(electricity_max))

    if insulation_min:
        query = query.filter(Catasto.insulation >= float(insulation_min))

    if insulation_max:
        query = query.filter(Catasto.insulation <= float(insulation_max))

    if piano:
        query = query.filter(Catasto.piano == int(piano))

    # Eseguire la query e restituire i risultati
    appartamenti = query.all()

    result = []
    for appartamento in appartamenti:
        result.append({
            'codice_appartamento': appartamento.codice_appartamento,
            'tipologia_appartamento': appartamento.tipologia_appartamento,
            'heating': appartamento.heating,
            'electricity_consumption': appartamento.electricity_consumption,
            'insulation': appartamento.insulation,
            'piano': appartamento.piano,
            'production': appartamento.production
        })

    # Verificare se sono stati trovati appartamenti
    if result:
        return jsonify(result)
    else:
        return jsonify({'message': 'Nessun appartamento trovato con i criteri forniti'}), 404

# Avvio del server Flask
if __name__ == '__main__':
    app.run(debug=True)
