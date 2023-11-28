KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        lukumaara = 0
        for i in range(0, self.alkioiden_lkm):
            if alkio == self.ljono[i]:
                lukumaara += 1
        return lukumaara > 0
 

    def lisaa(self, alkio):

        if not self.kuuluu(alkio):
            self.ljono[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.ljono):
                self.suurenna_lukujonoa()

            return True

        return False
    
    def suurenna_lukujonoa(self):
        taulukko_old = self.ljono
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.ljono)

    def poista(self, alkio):
        indeksi = self.etsi(alkio)
        if indeksi == -1:
            return False
        self.alkioiden_lkm -= 1
        for i in range(indeksi,self.alkioiden_lkm+1):
            self.ljono[i] = self.ljono[i+1]
        return True

    def etsi(self, alkio):
        for i in range(0,self.alkioiden_lkm):
            if self.ljono[i] == alkio:
                return i
        return -1
        
    def kopioi_lista(self, lista, listb):
        for i in range(0, len(lista)):
            listb[i] = lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = a

        for alkio in b.to_int_list():
            yhdiste.lisaa(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus.lisaa(b_taulu[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = a
        b_taulu = b.to_int_list()

        for alkio in b_taulu:
            erotus.poista(alkio)

        return erotus

    def __str__(self):
        string = ""
        for i in range(0, self.alkioiden_lkm ):
            string += str(self.ljono[i])+ ", "
        if self.alkioiden_lkm > 0:
            string = string[:-2]
        return "{"+ string +"}"
