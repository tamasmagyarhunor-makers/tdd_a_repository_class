class Pokemon():
    def __init__(self, id, name, power_type):
        self.id = id
        self.name = name
        self.power_type = power_type

    def __eq__(self, pokemon):
        return self.__dict__ == pokemon.__dict__