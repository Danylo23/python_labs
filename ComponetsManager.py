from models.CoolingSystem import CoolingSystem
from models.HDD import HDD
from models.MotherBoard import MotherBoard
from models.PowerSupply import PowerSupply
from models.Processor import Processor
from models.RAM import RAM
from models.VideoCard import VideoCard


class ComponentsManager:

    def __init__(self, components_list):
        self.components_list = components_list

    def sort_components_by_price(self, reverse):
        return sorted(self.components_list, key=lambda components: components.price, reverse=reverse)

    def sort_components_by_productYear(self, reverse):
        return sorted(self.components_list, key=lambda components: components.price, reverse=reverse)

    def sort_components_by_name(self, reverse):
        return sorted(self.components_list, key=lambda components: components.price, reverse=reverse)

coolingsystem = CoolingSystem("Asus", 500, 25, 2016, 2, 4)
hdd = HDD("Toshiba", 1000, 32, 2018, 2, 4)
motherboard = MotherBoard("Asus", 3000, 60, 2019, 4)
powersupply = PowerSupply("GameMax", 500, 55, 2015, 20, 4, 23)
processor = Processor("AMD", 6000, 20, 2016, 54, 12)
ram = RAM("HyperX", 3000, 5, 2018, 24, 76, 54)
videocard = VideoCard("Asus", 12500, 40, 2016, 21, 45, 256, 8)
components = [coolingsystem, hdd, motherboard, powersupply, processor, ram, videocard]
manager = ComponentsManager(components)
print(manager.sort_components_by_price(True))
print(manager.sort_components_by_name(False))
print(manager.sort_components_by_productYear(True))
