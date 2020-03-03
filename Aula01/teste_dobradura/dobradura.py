class Dobradura:

    def get_dobrar(self, numero_dobradura):
        contador = 2
        if type(numero_dobradura) == int and numero_dobradura > 0:
            for i in range(contador):
                i = contador ** numero_dobradura
                return i
        else:
            return False


a = Dobradura()
print(a.get_dobrar(13))


