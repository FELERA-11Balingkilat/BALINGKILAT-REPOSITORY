class Glassware:
    def __init__(self, capacity_ml: float = 250.0):
        self.capacity_ml = capacity_ml


class Beaker(Glassware):
    def __init__(self, capacity_ml: float = 250.0, is_graduated: bool = True):
        super().__init__(capacity_ml)
        self.is_graduated = is_graduated


class Tray:
    def __init__(self):
        self.beakers = [Beaker() for _ in range(5)]
