# Progetto Analizzatore Energetico

Questo progetto si occupa di calcolare il consumo energetico di un edificio, basandosi su dati catastali, APE (Attestato di Prestazione Energetica), BIM (Building Information Modeling), dati meteorologici e informazioni sulla produzione fotovoltaica. L'architettura è composta da vari microservizi containerizzati con Docker e orchestrati tramite Kubernetes.

## Struttura del Progetto

```plaintext
project-root/
│
├── orchestrator/                  # Orchestrazione generale delle città e attivazione dei microservizi dinamici
│   ├── city_service/               # Servizio che gestisce le città e attiva i servizi per i quartieri
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # API per la gestione delle città e l'attivazione dei servizi quartiere
│   │   │   └── service_calls.py    # Chiamate per avviare/fermare i servizi quartiere e altri servizi globali
│   │   ├── Dockerfile              # Dockerfile per il servizio città
│   │   ├── requirements.txt        # Dipendenze del servizio città
│   │   └── README.md
│   │
│   ├── neighborhood_service/       # Servizio che gestisce i quartieri e attiva i servizi per le vie
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # API per la gestione dei quartieri e l'attivazione dei servizi via
│   │   │   └── service_calls.py    # Chiamate per avviare/fermare i servizi delle vie
│   │   ├── Dockerfile              # Dockerfile per il servizio quartiere
│   │   ├── requirements.txt        # Dipendenze del servizio quartiere
│   │   └── README.md
│   │
│   ├── street_service/             # Servizio che gestisce le vie e attiva i servizi per i palazzi
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # API per la gestione delle vie e l'attivazione dei servizi palazzo
│   │   │   └── service_calls.py    # Chiamate per avviare/fermare i servizi dei palazzi
│   │   ├── Dockerfile              # Dockerfile per il servizio via
│   │   ├── requirements.txt        # Dipendenze del servizio via
│   │   └── README.md
│   │
│   ├── building_service/           # Servizio che gestisce i palazzi e avvia più istanze di analizzatore-energetico
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # API per la gestione dei palazzi e l'attivazione di più istanze del servizio analizzatore
│   │   │   └── service_calls.py    # Chiamate per avviare/fermare il servizio analizzatore energetico
│   │   ├── Dockerfile              # Dockerfile per il servizio palazzo
│   │   ├── requirements.txt        # Dipendenze del servizio palazzo
│   │   └── README.md
│
├── services/                       # Microservizi specifici che verranno scalati dinamicamente
│   ├── analizzatore-energetico/     # Microservizio per l'analisi energetica
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # Entry point del microservizio analizzatore energetico (Flask API)
│   │   │   ├── utils.py            # Funzioni utilitarie per calcolare i consumi energetici
│   │   │   ├── config.py           # Configurazione degli URL dei microservizi interni (ad esempio, meteo, catastale, etc.)
│   │   │   └── service_calls.py    # Chiamate ai microservizi interni (meteo, ape, bim, catastale)
│   │   ├── tests/
│   │   │   ├── test_analizzatore.py
│   │   ├── Dockerfile              # Dockerfile per il microservizio analizzatore energetico
│   │   ├── requirements.txt        # Dipendenze del microservizio analizzatore energetico
│   │   └── README.md
│   │
│   ├── servizio-catastale/          # Microservizio per gestire i dati catastali
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # Entry point del microservizio catastale
│   │   │   ├── config.py           # Configurazione degli URL per comunicare con altri servizi
│   │   │   └── service_calls.py    # Chiamate ai microservizi interni o esterni per ottenere i dati catastali
│   │   ├── tests/
│   │   │   ├── test_servizio_catastale.py
│   │   ├── Dockerfile              # Dockerfile per il microservizio catastale
│   │   ├── requirements.txt        # Dipendenze del microservizio catastale
│   │   └── README.md
│   │
│   ├── servizio-ape/                # Microservizio per i dati APE
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # Entry point del microservizio APE
│   │   │   ├── config.py           # Configurazione degli URL per comunicare con altri servizi
│   │   │   └── service_calls.py    # Chiamate ai microservizi interni o esterni per ottenere i dati APE
│   │   ├── tests/
│   │   │   ├── test_servizio_ape.py
│   │   ├── Dockerfile              # Dockerfile per il microservizio APE
│   │   ├── requirements.txt        # Dipendenze del microservizio APE
│   │   └── README.md
│   │
│   ├── servizio-bim/                # Microservizio per i dati BIM
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # Entry point del microservizio BIM
│   │   │   ├── config.py           # Configurazione degli URL per comunicare con altri servizi
│   │   │   └── service_calls.py    # Chiamate ai microservizi interni o esterni per ottenere i dati BIM
│   │   ├── tests/
│   │   │   ├── test_servizio_bim.py
│   │   ├── Dockerfile              # Dockerfile per il microservizio BIM
│   │   ├── requirements.txt        # Dipendenze del microservizio BIM
│   │   └── README.md
│   │
│   ├── servizio-meteo/              # Microservizio per i dati meteo
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # Entry point del microservizio meteo
│   │   │   ├── config.py           # Configurazione degli URL per comunicare con altri servizi
│   │   │   └── service_calls.py    # Chiamate ai microservizi interni o esterni per ottenere i dati meteo
│   │   ├── tests/
│   │   │   ├── test_servizio_meteo.py
│   │   ├── Dockerfile              # Dockerfile per il microservizio meteo
│   │   ├── requirements.txt        # Dipendenze del microservizio meteo
│   │   └── README.md
│   │
│   ├── servizio-fotovoltaico/       # Microservizio per impianti fotovoltaici
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py             # Entry point del microservizio fotovoltaico
│   │   │   ├── fotovoltaico_utils.py # Funzioni utilitarie per il calcolo dell'impianto fotovoltaico
│   │   │   ├── config.py           # Configurazione degli URL per comunicare con altri servizi
│   │   │   └── service_calls.py    # Chiamate ai microservizi interni o esterni per ottenere i dati fotovoltaici
│   │   ├── tests/
│   │   │   ├── test_servizio_fotovoltaico.py
│   │   ├── Dockerfile              # Dockerfile per il microservizio fotovoltaico
│   │   ├── requirements.txt        # Dipendenze del microservizio fotovoltaico
│   │   └── README.md
│
├── kubernetes/                      # Configurazioni Kubernetes per la scalabilità e il deployment dei servizi
│   ├── city-service-deployment.yaml
│   ├── neighborhood-service-deployment.yaml
│   ├── street-service-deployment.yaml
│   ├── building-service-deployment.yaml
│   ├── analizzatore-energetico-deployment.yaml  # Configurazione Kubernetes per il microservizio analizzatore energetico
│   ├── servizio-catastale-deployment.yaml       # Configurazione Kubernetes per il microservizio catastale
│   ├── servizio-ape-deployment.yaml             # Configurazione Kubernetes per il microservizio APE
│   ├── servizio-bim-deployment.yaml             # Configurazione Kubernetes per il microservizio BIM
│   ├── servizio-meteo-deployment.yaml           # Configurazione Kubernetes per il microservizio meteo
│   ├── servizio-fotovoltaico-deployment.yaml    # Configurazione Kubernetes per il microservizio fotovoltaico
│   └── service.yaml                             # Configurazione per bilanciare il carico e gestione del traffico
│
├── scripts/                         # Script per il deployment e la gestione del progetto
│   ├── deploy.sh                    # Script per il deployment dei servizi in Kubernetes o Docker
│   └── build_docker_images.sh       # Script per costruire le immagini Docker
│
├── .env                             # Variabili d'ambiente per configurare i microservizi
├── docker-compose.yml               # Docker Compose per eseguire localmente i microservizi
└── README.md                        # Documentazione principale del progetto
