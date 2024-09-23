import requests
from .config import APE_URL, BIM_URL, METEO_URL, FOTOVOLTAICO_URL

def get_ape_data(building_id):
    response = requests.get(f"{APE_URL}/{building_id}")
    if response.status_code == 200:
        return response.json()  # Simulazione dei dati APE
    return None

def get_bim_data(building_id):
    response = requests.get(f"{BIM_URL}/{building_id}")
    if response.status_code == 200:
        return response.json()  # Simulazione dei dati BIM
    return None

def get_meteo_data(city):
    response = requests.get(f"{METEO_URL}/{city}")
    if response.status_code == 200:
        return response.json()  # Simulazione dei dati meteo
    return None

def get_fotovoltaico_data(building_id):
    response = requests.get(f"{FOTOVOLTAICO_URL}/{building_id}")
    if response.status_code == 200:
        return response.json()  # Simulazione dei dati fotovoltaici
    return None

