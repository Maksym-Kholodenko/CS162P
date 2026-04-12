class Rock:
    def __init__(self, name, color, hardness):
        self._name = name
        self._color = color
        self._hardness = hardness

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_hardness(self):
        return self._hardness

    def set_hardness(self, hardness):
        self._hardness = hardness

    name = property(get_name, set_name)
    color = property(get_color, set_color)
    hardness = property(get_hardness, set_hardness)
    
    
    