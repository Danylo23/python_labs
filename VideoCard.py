from models.Components import Components


class VideoCard(Components):
    def __init__(self, name, price, powerConsumption, productYear, processorType, memory, frequencyOfMemory,
                 frequencyOfCores):
        super(VideoCard, self).__init__(name, price, powerConsumption, productYear)
        self.processorType = processorType
        self.memory = memory
        self.frequencyOfCores = frequencyOfCores
        self.frequencyOfMemory = frequencyOfMemory




class C(a, b):


    class
