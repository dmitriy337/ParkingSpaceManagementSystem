from parking.types import ParkingLotsTypes
from typing import List
import config

class Vehicle():
    name: str = None
    size: int = None
    required_lot: List[int] = None
    type_of_vehicle: int = None


class Bike(Vehicle):

    def __init__(self) -> None:
        self.name = "Bike"
        self.size = 1
        self.type_of_vehicle = ParkingLotsTypes.BIKE_LOT
        self.required_lot = [ParkingLotsTypes.BIKE_LOT,
                            ParkingLotsTypes.COMPACT_LOT, ParkingLotsTypes.BIG_LOT]


class Car(Vehicle):

    def __init__(self) -> None:
        self.name = "Car"
        self.size = 1
        self.type_of_vehicle = ParkingLotsTypes.COMPACT_LOT
        self.required_lot = [
            ParkingLotsTypes.COMPACT_LOT, ParkingLotsTypes.BIG_LOT]


class Bus(Vehicle):

    def __init__(self) -> None:
        self.name = "Bus"
        self.size = config.bus_required
        self.type_of_vehicle = ParkingLotsTypes.BIG_LOT
        self.required_lot = [ParkingLotsTypes.BIG_LOT]
