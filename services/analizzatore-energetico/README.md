
# Microservizio: Analizzatore Energetico

Il **microservizio analizzatore energetico** calcola il consumo energetico giornaliero di un edificio utilizzando dati provenienti da vari servizi esterni, come APE (Attestato di Prestazione Energetica), BIM (Building Information Modeling), meteo e fotovoltaico.

## Funzionamento

Il microservizio raccoglie i dati sui consumi e la produzione di energia da diversi servizi esterni per fornire una stima del consumo energetico giornaliero di un edificio.

### Calcoli Principali

1. **Fabbisogno Termico**: Il fabbisogno termico viene calcolato in base alla differenza tra la temperatura interna e quella esterna, tenendo conto del coefficiente di isolamento dell'edificio e del fabbisogno di riscaldamento.
   
   - Formula:
     \
     \[
     	ext{Fabbisogno Termico} = rac{(T_{	ext{interna}} - T_{	ext{esterna}}) 	imes 	ext{Riscaldamento}}{	ext{Isolamento}}
     \]
   
2. **Consumo Netto Elettrico**: Il consumo elettrico netto è dato dalla differenza tra il consumo elettrico totale e l'energia prodotta dall'impianto fotovoltaico.
   
   - Formula:
     \
     \[
     	ext{Consumo Netto Elettrico} = \max(	ext{Consumo Elettrico} - 	ext{Produzione Fotovoltaica}, 0)
     \]

3. **Consumo Giornaliero Totale**: Somma del fabbisogno termico e del consumo netto elettrico.
   
   - Formula:
     \
     \[
     	ext{Consumo Giornaliero Totale} = 	ext{Fabbisogno Termico} + 	ext{Consumo Netto Elettrico}
     \]

## Struttura del Progetto

Il progetto è organizzato nella seguente struttura:

```
analizzatore_energetico/
│
├── app/
│   ├── __init__.py           # Inizializzazione dell'app Flask
│   ├── main.py               # Entry point del microservizio (API Flask)
│   ├── utils.py              # Funzioni di calcolo del consumo energetico
│   ├── config.py             # Configurazioni per i servizi esterni
│   └── service_calls.py      # Chiamate ai servizi esterni (APE, BIM, meteo, fotovoltaico)
│
├── tests/
│   ├── __init__.py           # Inizializzazione dei test
│   └── test_analizzatore.py   # Test del microservizio con mocking
│
├── requirements.txt           # Dipendenze del progetto
└── README.md                  # Documentazione (questo file)
```

## API Endpoints

### `GET /calcola_consumo`

Calcola il consumo energetico giornaliero per un edificio specificato. Utilizza dati simulati da diversi servizi esterni.

#### Parametri:
- `building_id`: Identificativo dell'edificio.
- `city`: Città per ottenere i dati meteorologici.

#### Esempio di richiesta:
```
GET http://127.0.0.1:5000/calcola_consumo?building_id=1&city=Milano
```

#### Esempio di risposta:
```json
{
  "fabbisogno_termico": 5000.0,
  "consumo_netto_elettrico": 300.0,
  "consumo_totale_giornaliero": 5300.0
}
```

## Requisiti

- **Python 3.7+**
- **Flask** (versione specificata nel `requirements.txt`)
- **requests** (versione specificata nel `requirements.txt`)

## Istruzioni per l'Installazione

1. Clonare il repository o scaricare il progetto.
2. Navigare nella cartella principale del progetto.
3. Installare le dipendenze con il seguente comando:

   ```bash
   pip install -r requirements.txt
   ```

## Esecuzione del Microservizio

Per avviare il microservizio, eseguire il comando:

```bash
py -m flask --app app run
```

Questo comando avvierà il server Flask. Il microservizio sarà accessibile all'indirizzo:

```
http://127.0.0.1:5000
```

## Test del Microservizio

Per eseguire i test del microservizio, utilizziamo la libreria `unittest` con **mocking** delle chiamate ai servizi esterni.

### Esecuzione dei test:

```bash
py -m unittest discover -s tests
```

Questo comando eseguirà tutti i test presenti nella cartella `tests/` e verificherà che il microservizio funzioni correttamente utilizzando dati simulati.

### Mock dei Servizi Esterni

I test utilizzano **unittest.mock** per simulare le risposte dei servizi esterni (APE, BIM, meteo, fotovoltaico), evitando così chiamate reali a questi servizi.

Esempio di test eseguito:

```python
@patch('app.main.get_ape_data')
@patch('app.main.get_bim_data')
@patch('app.main.get_meteo_data')
@patch('app.main.get_fotovoltaico_data')
def test_calcola_consumo(self, mock_fotovoltaico, mock_meteo, mock_bim, mock_ape):
    mock_ape.return_value = {'heating': 1000, 'electricity_consumption': 500}
    mock_bim.return_value = {'insulation': 2}
    mock_meteo.return_value = {'temperature': 10}
    mock_fotovoltaico.return_value = {'production': 200}

    response = self.client.get('/calcola_consumo?building_id=1&city=Milano')
    self.assertEqual(response.status_code, 200)
    data = response.get_json()
    self.assertAlmostEqual(data['fabbisogno_termico'], 5000)
    self.assertAlmostEqual(data['consumo_netto_elettrico'], 300)
    self.assertAlmostEqual(data['consumo_totale_giornaliero'], 5300)
```

## Contributi

Se desideri contribuire a questo progetto, segui questi passaggi:

1. Fai un fork del progetto.
2. Crea un nuovo branch (`git checkout -b feature/AmazingFeature`).
3. Committa le tue modifiche (`git commit -m 'Add some AmazingFeature'`).
4. Push delle modifiche (`git push origin feature/AmazingFeature`).
5. Apri una Pull Request.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.
