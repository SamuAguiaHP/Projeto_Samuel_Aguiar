class A:
    def __init__(self):
        self._a1 = 0    # int A1
        self._a2 = 0.0  # float A2

    # Getters
    def get_a1(self):
        return self._a1

    def get_a2(self):
        return self._a2

    # Setters
    def set_a1(self, value):
        self._a1 = value

    def set_a2(self, value):
        self._a2 = value

    # Métodos
    def MA1(self):
        print("Método MA1()")

    def MA2(self):
        print("Método MA2()")

    def MA3(self): # NOVO MÉTODO
        print("Alteração a classe A partir do clone")