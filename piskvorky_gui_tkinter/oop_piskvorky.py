"""
Hra 1D piškvorky použitá při výuce PyLadies Plzeň

__author__    = u"Tomáš Zítka"
__date__      = u"Date: 2019/05/14 20:07:15"

Změny:
   Oprava ve funkci tah_hrace

"""
from random import randrange


class Hra_piskvorek1D():

    zpravy = {"x": "Vyhral x.",
              "o": "Vyhral o.",
              "!": "Remiza",
              "-": "Hrajeme dal"}

    def __init__(self, rozmer):
        """

        :param rozmer: pocet znaku v hernim poli
        """

        self.herni_pole = rozmer * "-"
        self.rozmer = rozmer

    def vyhodnot(self):
        """
        :return: "x" při výhře x,
                 "o" při výhře o
                 "!" při remíze
                 "-" při otevřené hře
        """
        if "xxx" in self.herni_pole:
            return "x"
        elif "ooo" in self.herni_pole:
            return "o"
        elif not ("-" in self.herni_pole):
            return "!"
        else:
            return "-"

    def _tahni(self, cislo_policka, symbol):
        self.herni_pole = \
           self.herni_pole[0:cislo_policka] + \
           symbol + \
           self.herni_pole[cislo_policka+1:]

    def tah_pocitace(self):
        while True:
            pozice = int(randrange(0, len(self.herni_pole)))
            if self.herni_pole[pozice] == "-":
                self._tahni(pozice, "o")
                return True

    def tah_hrace(self, cislo_policka):
        """

        :param cislo_policka: cislo herniho pole od 1 do self.rozmer vcetne
        :return: none pokud je tah mozny, string pokud ne
        """
        pozice = cislo_policka - 1
        if (0 <= pozice) and (pozice < self.rozmer):
            if self.herni_pole[pozice] == "-":
                self._tahni(pozice, 'x')
                return None
            else:
                return "Pozice je obsazena"
        else:
            return "Hrajte jen v herním poli tj. od 1 do {}".format(self.rozmer)




if __name__ == '__main__':
    hra = Hra_piskvorek1D(20)
    while True:
        cislo_tah_hrace = int(input("Zadejte pozici v rozsahu 1 - {}: ".format(hra.rozmer)))

        chyba = hra.tah_hrace(cislo_tah_hrace)

        if chyba is not None:
            print(chyba)
            continue
        print(hra.herni_pole)
        if hra.vyhodnot() != "-":
            break
        hra.tah_pocitace()

        print(hra.herni_pole)

        if hra.vyhodnot() != "-":
            break

    if hra.vyhodnot() == "!":
        print("Remíza, nikdo nevyhrál.")
    elif hra.vyhodnot() == "x":
        print("Gratuluji vyhráli jste.")
    else:
        print("Ted jsem vyhrál já.")