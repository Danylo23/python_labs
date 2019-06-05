from models.Components import Components


class Processor(Components):
    def __init__(self, name, price, powerConsumption, productYear, coresNumber, cashe):
        super(Processor, self).__init__(name, price, powerConsumption, productYear)
        self.coresNumber = coresNumber
        self.cashe = cashe
