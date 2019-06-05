from models.Components import Components


class CoolingSystem(Components):
    def __init__(self, name, price, powerConsumption, productYear, fanSize, weight):
        super(CoolingSystem, self).__init__(name, price, powerConsumption, productYear)
        self.fanSize = fanSize
        self.weight = weight
