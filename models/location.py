class Location():

    def __init__(self, id, name, address = ""):
        self.id = id
        self.name = name 

        if address is not "":
            self.address = address