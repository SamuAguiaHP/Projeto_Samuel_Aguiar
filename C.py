class C:
    def __init__(self):
        self._c1 = ""  # String C1
        self._c2 = 0   # Int C2

    # Getters
    def get_c1(self):
        return self._c1

    def get_c2(self):
        return self._c2

    # Setters
    def set_c1(self, value):
        self._c1 = value

    def set_c2(self, value):
        self._c2 = value

    # Métodos
    def MC1(self):
        print("Método MC1()")

    def MC2(self):
        print("Método MC2()")