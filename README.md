# Progetto Analizzatore Energetico

Questo progetto si occupa di calcolare il consumo energetico di un edificio, basandosi su dati catastali, APE (Attestato di Prestazione Energetica), BIM (Building Information Modeling), dati meteorologici e informazioni sulla produzione fotovoltaica. L'architettura è composta da vari microservizi containerizzati con Docker e orchestrati tramite Kubernetes.

## Struttura del Progetto

```plaintext
project-root/
│
├── services/
│   ├── analizzatore-energetico/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py               # Entry point del microservizio analizzatore energetico (Flask API)
│   │   │   ├── utils.py              # Funzioni utilitarie per calcolare i consumi energetici
│   │   │   ├── config.py             # Configurazione (es. URL per servizi interni)
│   │   │   └── service_calls.py      # Chiamate ai servizi interni ed esterni
│   │   ├── tests/                    # Test del microservizio
│   │   │   ├── test_analizzatore.py
│   │   ├── Dockerfile                # Docker per il microservizio
│   │   ├── requirements.txt          # Dipendenze
│   │   └── README.md                 # Documentazione
│   │
│   ├── servizio-catastale/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py               # Gestisce chiamate per dati catastali (chiama servizio esterno del comune)
│   │   │   └── service_calls.py      # Chiamate esterne al sito www.comune-ascolipiceno-service.it
│   │   ├── Dockerfile                # Docker per servizio catastale
│   │   ├── requirements.txt          # Dipendenze
│   │   └── README.md                 # Documentazione
│   │
│   ├── servizio-ape/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py               # Gestisce chiamate per i dati APE (chiama servizio esterno del comune)
│   │   │   └── service_calls.py      # Chiamate esterne al sito www.comune-ascolipiceno-service.it
│   │   ├── Dockerfile                # Docker per servizio APE
│   │   ├── requirements.txt          # Dipendenze
│   │   └── README.md                 # Documentazione
│   │
│   ├── servizio-bim/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py               # Gestisce chiamate per i dati BIM (chiama servizio esterno del comune)
│   │   │   └── service_calls.py      # Chiamate esterne al sito www.comune-ascolipiceno-service.it
│   │   ├── Dockerfile                # Docker per servizio BIM
│   │   ├── requirements.txt          # Dipendenze
│   │   └── README.md                 # Documentazione
│   │
│   ├── servizio-meteo/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py               # Gestisce chiamate per i dati meteo (chiama www.meteo.it)
│   │   │   └── service_calls.py      # Chiamate esterne al sito www.meteo.it
│   │   ├── Dockerfile                # Docker per servizio meteo
│   │   ├── requirements.txt          # Dipendenze
│   │   └── README.md                 # Documentazione
│   │
│   ├── servizio-fotovoltaico/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py               # Dati interni per impianto fotovoltaico basati sui dati BIM
│   │   │   └── fotovoltaico_utils.py # Funzioni per ottenere le specifiche dell'impianto dal servizio BIM
│   │   ├── Dockerfile                # Docker per servizio fotovoltaico
│   │   ├── requirements.txt          # Dipendenze
│   │   └── README.md                 # Documentazione
│
├── kubernetes/
│   ├── analizzatore-energetico-deployment.yaml  # Configurazione Kubernetes per il servizio analizzatore energetico
│   ├── servizio-catastale-deployment.yaml       # Configurazione Kubernetes per il servizio catastale
│   ├── servizio-ape-deployment.yaml             # Configurazione Kubernetes per il servizio APE
│   ├── servizio-bim-deployment.yaml             # Configurazione Kubernetes per il servizio BIM
│   ├── servizio-meteo-deployment.yaml           # Configurazione Kubernetes per il servizio meteo
│   ├── servizio-fotovoltaico-deployment.yaml    # Configurazione Kubernetes per il servizio fotovoltaico
│   └── service.yaml                             # Configurazione per bilanciamento del carico
│
├── scripts/
│   ├── deploy.sh                # Script per il deployment dei servizi
│   └── build_docker_images.sh   # Script per costruire le immagini Docker
│
├── .env                         # Variabili d'ambiente globali
├── docker-compose.yml            # Docker Compose per eseguire localmente i microservizi
└── README.md                     # Documentazione principale del progetto
