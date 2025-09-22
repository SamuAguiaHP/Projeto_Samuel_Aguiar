class D:
    def __init__(self):
        self._d1 = "texto" # String D1
        self._d2 = True    # Boolean D2

    # Getters
    def get_d1(self):
        return self._d1

    def get_d2(self):
        return self._d2

    # Setters
    def set_d1(self, value):
        self._d1 = value

    def set_d2(self, value):
        self._d2 = value

    # Métodos
    def MD1(self):
        print("Método MD1()")

    def MD2(self):
        print("Método MD2()")