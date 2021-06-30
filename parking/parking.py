from typing import List
from vehicle import Vehicle


class ParkingLot():
    type: int
    _isOccupied: bool
    vehicle: Vehicle

    def __init__(self, type, vehicle=None) -> None:
        self.type = type
        self._isOccupied = False
        self.vehicle = vehicle

    @property
    def isOccupied(self) -> bool:
        if self.vehicle is None:
            self._isOccupied = False
            return self._isOccupied
        else:
            self._isOccupied = True
            return self._isOccupied


class Parking():
    parking: List[List[ParkingLot]]

    def __init__(self, parking: List[List[ParkingLot]]) -> None:
        self.parking = parking
