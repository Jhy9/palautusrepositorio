import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 5
        self.varasto_mock = Mock()
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 3
            if tuote_id == 2:
                return 1
            if tuote_id == 3:
                return 0
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1,"tuote1",5)
            if tuote_id == 2:
                return Tuote(2,"tuote2",6)
            if tuote_id == 3:
                return Tuote(3,"tuote3",10)
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(self.varasto_mock,self.pankki_mock,self.viitegeneraattori_mock)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostosten_paatyttya_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("y","123")
        self.pankki_mock.tilisiirto.assert_called_with("y",5,"123","33333-44455",5)


    def test_kahden_saman_tuotteen_ostos_tilisiirto_on_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("y","123")
        self.pankki_mock.tilisiirto.assert_called_with("y",5,"123","33333-44455",10)

    def test_kahden_eri_tuotteen_ostos_tilisiirto_on_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("y","123")
        self.pankki_mock.tilisiirto.assert_called_with("y",5,"123","33333-44455",11)

    def test_kahden_eri_tuotteen_ostos_tilisiirto_on_oikein_kun_toinen_tuote_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("y","123")
        self.pankki_mock.tilisiirto.assert_called_with("y",5,"123","33333-44455",5)

    def test_kauppa_veloittaa_oikein_korin_nollauksen_jalkeen(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.tilimaksu("y","123")
        self.pankki_mock.tilisiirto.assert_called_with("y",5,"123","33333-44455",5)

    def test_kauppa_pyytaa_uuden_viitteen_jokaiselle_maksulle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.tilimaksu("y","123")
        self.pankki_mock.tilisiirto.assert_called_with("y",5,"123","33333-44455",5)
        self.viitegeneraattori_mock.uusi.return_value = 6
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.tilimaksu("y","123")
        self.pankki_mock.tilisiirto.assert_called_with("y",6,"123","33333-44455",5)

    def test_kauppa_veloittaa_oikein_korista_poiston_jalkeen(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("y","123")
        self.pankki_mock.tilisiirto.assert_called_with("y",5,"123","33333-44455",6)