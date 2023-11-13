from abc import ABC, abstractmethod
from enum import Enum

class ServiceCriteria:
    def __init__(self, brand, capacity, quality):
        self.brand = brand
        self.capacity = capacity
        self.quality = quality

class VehicleType(Enum):
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"
    CONVENTIONAL = "Conventional"

class Car(ABC):
    def __init__(self, model, service_criteria):
        self.model = model
        self.service_criteria = service_criteria

    @abstractmethod
    def get_speed_limit(self):
        pass

class CarModel:
    def __init__(self, name, vehicle_type, service_criteria):
        self.name = name
        self.vehicle_type = vehicle_type
        self.service_criteria = service_criteria

class ElectricCar(Car):
    def __init__(self, model, service_criteria):
        super().__init__(model, service_criteria)

    def get_speed_limit(self):
        return 150

class HybridCar(Car):
    def __init__(self, model, service_criteria):
        super().__init__(model, service_criteria)

    def get_speed_limit(self):
        return 180

class ConventionalCar(Car):
    def __init__(self, model, service_criteria):
        super().__init__(model, service_criteria)

    def get_speed_limit(self):
        return 200