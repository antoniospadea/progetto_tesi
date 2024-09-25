
# Progetto Catasto Microservizio API

Questo progetto implementa un microservizio API che fornisce accesso ai dati catastali. L'API è costruita con **Flask** e utilizza **SQLAlchemy** per interagire con un database SQLite che contiene informazioni su appartamenti, inclusi i dati su riscaldamento, consumo elettrico e isolamento.

## Descrizione del Database

Il database SQLite contiene una tabella chiamata `catasto` con le seguenti colonne:

### Colonne del Database:

- **`codice_appartamento`**: (String) Codice univoco alfanumerico che identifica l'appartamento. Il codice include informazioni sulla città, il quartiere, la via e il numero civico. Ad esempio, `As_Ca_001_1_01` rappresenta un appartamento nella città di Ascoli Piceno, quartiere Campo Parignano, via 001, piano 1, appartamento 01.
  
- **`tipologia_appartamento`**: (String) La tipologia dell'appartamento. Può assumere i seguenti valori:
  - `Residenziale`
  - `Commerciale`
  - `Condominiale`

- **`heating`**: (Float) Consumo di riscaldamento per l'appartamento, espresso in unità di energia (ad es. kWh).

- **`electricity_consumption`**: (Float) Consumo elettrico per l'appartamento, espresso in unità di energia (ad es. kWh).

- **`insulation`**: (Float) Valore che rappresenta l'isolamento dell'appartamento. Un valore più alto indica un isolamento migliore.

- **`piano`**: (Integer) Il piano su cui si trova l'appartamento.

- **`production`**: (Text) Produzione energetica (ad es. da pannelli solari) per l'appartamento. Se il valore è un singolo numero, rappresenta la produzione totale; se è un array (memorizzato come stringa JSON), rappresenta la produzione giornaliera per 365 giorni.

## Installazione e Setup

### Prerequisiti:

- Python 3.x
- Installare le dipendenze necessarie:
  ```bash
  pip install flask sqlalchemy
  ```

### Configurazione del Database

1. Posiziona il file `catasto.db` nella directory `Creazione_DB`.
2. Assicurati che il percorso del database sia corretto nel file `microservice.py`:
   ```python
   db_directory = r'C:\Users\Antonio\Desktop\progetto_tesi\Creazione_DB'
   ```

### Avvio del Microservizio

1. Posiziona il file `microservice.py` nella tua directory di progetto.
2. Avvia il server Flask:
   ```bash
   py microservice.py
   ```

3. L'API sarà disponibile all'indirizzo:
   ```
   http://127.0.0.1:5000
   ```

## Esempi di Query API

### 1. Recuperare tutti gli appartamenti

**Endpoint**: `/appartamenti`

**Metodo**: `GET`

**Descrizione**: Recupera tutti gli appartamenti presenti nel database.

```bash
GET http://127.0.0.1:5000/appartamenti
```

### 2. Recuperare un appartamento specifico tramite `codice_appartamento`

**Endpoint**: `/appartamenti/<codice_appartamento>`

**Metodo**: `GET`

**Descrizione**: Recupera le informazioni di un appartamento specifico.

**Esempio**:

```bash
GET http://127.0.0.1:5000/appartamenti/As_Ca_001_1_01
```

**Risposta**:
```json
{
  "codice_appartamento": "As_Ca_001_1_01",
  "tipologia_appartamento": "Residenziale",
  "heating": 120.5,
  "electricity_consumption": 400.2,
  "insulation": 30.8,
  "piano": 1,
  "production": "0.0"
}
```

### 3. Cercare appartamenti in base alla tipologia

**Endpoint**: `/appartamenti/tipologia/<tipologia_appartamento>`

**Metodo**: `GET`

**Descrizione**: Cerca appartamenti con una specifica tipologia.

**Esempio**:
```bash
GET http://127.0.0.1:5000/appartamenti/tipologia/Condominiale
```

### 4. Eseguire query dinamiche su più colonne

**Endpoint**: `/appartamenti/search`

**Metodo**: `GET`

**Descrizione**: Filtra gli appartamenti in base a parametri multipli. Tutti i parametri sono opzionali, ma possono essere combinati per filtrare su più colonne.

**Parametri supportati**:
- `codice_appartamento`: Filtro parziale sul codice appartamento.
- `tipologia_appartamento`: Tipologia dell'appartamento (ad es. `Residenziale`).
- `heating_min`, `heating_max`: Consumo di riscaldamento minimo e massimo.
- `electricity_min`, `electricity_max`: Consumo elettrico minimo e massimo.
- `insulation_min`, `insulation_max`: Isolamento minimo e massimo.
- `piano`: Piano dell'appartamento.

**Esempio**:

Cercare tutti gli appartamenti residenziali con riscaldamento tra 50 e 150:

```bash
GET http://127.0.0.1:5000/appartamenti/search?tipologia_appartamento=Residenziale&heating_min=50&heating_max=150
```

### 5. Recuperare appartamenti per codice e tipologia

**Esempio**:
Cercare appartamenti nella città di Ascoli Piceno, quartiere Campo Parignano, con tipologia "Condominiale":

```bash
GET http://127.0.0.1:5000/appartamenti/search?codice_appartamento=As_Ca&tipologia_appartamento=Condominiale
```

## Debug e Test

Se il server non si avvia correttamente, verifica i seguenti passaggi:

- Assicurati che il file del database sia posizionato correttamente.
- Controlla che tutte le dipendenze siano installate correttamente.
- Se usi un'altra versione di Python, sostituisci `py` con `python` nei comandi.

## Contributi

Sentiti libero di contribuire a questo progetto facendo un fork del repository e inviando una pull request con i tuoi miglioramenti.

