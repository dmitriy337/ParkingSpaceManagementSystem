from parking import ParkingLotsTypes
from types import List


class Vehicle():
    size: int
    required_lot: List[int]


class Bike(Vehicle):

    def __init__(self) -> None:
        self.size = 1
        self.required_lot = [ParkingLotsTypes.BIKE_LOT,
                            ParkingLotsTypes.COMPACT_LOT, ParkingLotsTypes.BIG_LOT]


class Car(Vehicle):

    def __init__(self) -> None:
        self.size = 1
        self.required_lot = [
            ParkingLotsTypes.COMPACT_LOT, ParkingLotsTypes.BIG_LOT]


class Bus(Vehicle):

    def __init__(self) -> None:
        self.size = 5
        self.required_lot = [ParkingLotsTypes.BIG_LOT]
