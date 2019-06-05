from models.Components import Components


class RAM(Components):
    def __init__(self, name, price, powerConsumption, productYear, memoryAmount, effectiveBandWidth, voltageSupply):
        super(RAM, self).__init__(name, price, powerConsumption, productYear)
        self.memoryAmount = memoryAmount
        self.effectiveBandWidth = effectiveBandWidth
        self.voltageSupply = voltageSupply
