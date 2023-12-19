from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class KiviPaperiSakset:
    @staticmethod
    def luo_pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def luo_pelaaja_vs_tekoaly():
        return KPSTekoaly()
    
    @staticmethod
    def luo_pelaaja_vs_edistynyt_tekoaly():
        return KPSParempiTekoaly()