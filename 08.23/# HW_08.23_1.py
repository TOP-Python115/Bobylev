
from abc import ABC, abstractmethod

# Passenger & Cargo Carriers
class Carrier(ABC):
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


# Military & Commercial Planes
class Plane(ABC):
    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self, new_objects):
        pass


# СДЕЛАТЬ: напишите реализации нужных классов, так чтобы у вас получился Мост между назначением самолёта и сферой использования.

