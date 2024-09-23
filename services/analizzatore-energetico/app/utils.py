# Funzioni utilitarie per possibili estensioni future
def calcola_fabbisogno_termico(temp_interna, temp_esterna, riscaldamento, isolamento):
    return (temp_interna - temp_esterna) * riscaldamento / isolamento

def calcola_consumo_netto_elettrico(consumo_elettrico, produzione_fotovoltaica):
    return max(consumo_elettrico - produzione_fotovoltaica, 0)

def calcola_consumo_totale_giornaliero(fabbisogno_termico, consumo_netto_elettrico):
    return fabbisogno_termico + consumo_netto_elettrico
