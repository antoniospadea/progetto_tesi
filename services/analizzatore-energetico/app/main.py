from flask import Blueprint, jsonify, request
from .utils import calcola_fabbisogno_termico, calcola_consumo_netto_elettrico, calcola_consumo_totale_giornaliero
from .service_calls import get_ape_data, get_bim_data, get_meteo_data, get_fotovoltaico_data

api = Blueprint('api', __name__)

@api.route('/calcola_consumo', methods=['GET'])
def calcola_consumo():
    building_id = request.args.get('building_id')
    city = request.args.get('city')

    # Ottenere i dati dai servizi esterni
    ape_data = get_ape_data(building_id)
    bim_data = get_bim_data(building_id)
    meteo_data = get_meteo_data(city)
    fotovoltaico_data = get_fotovoltaico_data(building_id)

    if not all([ape_data, bim_data, meteo_data, fotovoltaico_data]):
        return jsonify({'error': 'Could not fetch all necessary data'}), 500

    # Dati simulati
    temp_esterna = meteo_data['temperature']
    isolamento = bim_data['insulation']
    riscaldamento = ape_data['heating']
    consumo_elettrico = ape_data['electricity_consumption']
    produzione_fotovoltaica = fotovoltaico_data['production']

    # Calcoli
    fabbisogno_termico = calcola_fabbisogno_termico(20, temp_esterna, riscaldamento, isolamento)
    consumo_netto_elettrico = calcola_consumo_netto_elettrico(consumo_elettrico, produzione_fotovoltaica)
    consumo_totale = calcola_consumo_totale_giornaliero(fabbisogno_termico, consumo_netto_elettrico)

    return jsonify({
        'fabbisogno_termico': fabbisogno_termico,
        'consumo_netto_elettrico': consumo_netto_elettrico,
        'consumo_totale_giornaliero': consumo_totale
    })
