from models.Components import Components


class MotherBoard(Components):
    def __init__(self, name, price, powerConsumption, productYear, processorType):
        super(MotherBoard, self).__init__(name, price, powerConsumption, productYear)
        self.processorType = processorType
