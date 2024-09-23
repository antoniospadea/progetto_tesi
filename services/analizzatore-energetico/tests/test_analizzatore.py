import unittest
from unittest.mock import patch
from app import create_app

class TestAnalizzatoreEnergetico(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    @patch('app.main.get_ape_data')
    @patch('app.main.get_bim_data')
    @patch('app.main.get_meteo_data')
    @patch('app.main.get_fotovoltaico_data')
    def test_calcola_consumo(self, mock_fotovoltaico, mock_meteo, mock_bim, mock_ape):
        # Simulare i dati di ritorno
        mock_ape.return_value = {'heating': 1000, 'electricity_consumption': 500}
        mock_bim.return_value = {'insulation': 2}
        mock_meteo.return_value = {'temperature': 10}
        mock_fotovoltaico.return_value = {'production': 200}

        # Chiamata all'API
        response = self.client.get('/calcola_consumo?building_id=1&city=Milano')
        data = response.get_json()

        # Controllo del risultato
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(data['fabbisogno_termico'], 5000)
        self.assertAlmostEqual(data['consumo_netto_elettrico'], 300)
        self.assertAlmostEqual(data['consumo_totale_giornaliero'], 5300)

if __name__ == '__main__':
    unittest.main()


