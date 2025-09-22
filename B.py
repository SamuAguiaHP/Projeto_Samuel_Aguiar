class B:
    def __init__(self):
        self._b1 = 0    # int B1
        self._b2 = 0.0  # float B2

    # Getters
    def get_b1(self):
        return self._b1

    def get_b2(self):
        return self._b2

    # Setters
    def set_b1(self, value):
        self._b1 = value

    def set_b2(self, value):
        self._b2 = value

    # Métodos
    def MB1(self):
        print("Método MB1()")

    def MB2(self):
        print("Método MB2()")