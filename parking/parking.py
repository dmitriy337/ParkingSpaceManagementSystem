from typing import List
from vehicle import Vehicle
from .exceptions import VehicleIsNotPossibleToPlace, IsNotVehicle


class ParkingLot():
    type_of_vehicle: int
    _isOccupied: bool = False
    _vehicle: Vehicle

    # Возможно ли размещение транспорта в слоте?

    def possible_to_place(self, type_of_vehicle: int, vehicle: Vehicle) -> bool:
        return type_of_vehicle in vehicle.required_lot

    def __init__(self, type_of_vehicle, vehicle=None) -> None:
        self.type_of_vehicle = type_of_vehicle

        if vehicle:
            if self.possible_to_place(type_of_vehicle, vehicle):
                self._vehicle = vehicle
            else:
                raise VehicleIsNotPossibleToPlace
        else:
            self._vehicle = vehicle

    # Занята ли ячейка?
    @property
    def isOccupied(self) -> bool:
        if self._vehicle is None:
            self._isOccupied = False
            return self._isOccupied
        else:
            self._isOccupied = True
            return self._isOccupied

    @isOccupied.setter
    def isOccupied(self, b: bool) -> bool:
        self._isOccupied = b

    @property
    def vehicle(self) -> Vehicle:
        if self._vehicle != None:
            return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle) -> None:
        if isinstance(vehicle, Vehicle):
            if self.possible_to_place(self.type_of_vehicle, vehicle):
                self._vehicle = vehicle
            else:
                raise VehicleIsNotPossibleToPlace
        else:
            raise IsNotVehicle


class Parking():
    parking: List[List[ParkingLot]]

    def __init__(self, parking: List[List[ParkingLot]]) -> None:
        self.parking = parking
