from models.Components import Components


class PowerSupply(Components):
    def __init__(self, name, price, powerConsumption, productYear, power, videoCardCollectors, modularCableCollectors):
        super(PowerSupply, self).__init__(name, price, powerConsumption, productYear)
        self.power = power
        self.videoCardCollectors = videoCardCollectors
        self.modularCableCollectors = modularCableCollectors
