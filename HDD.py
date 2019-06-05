from models.Components import Components


class HDD(Components):
    def __init__(self, name, price, powerConsumption, productYear, capasity, spindleSpeed):
        super(HDD, self).__init__(name, price, powerConsumption, productYear)
        self.capasity = capasity
        self.spindleSpeed = spindleSpeed
