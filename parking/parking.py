from typing import List, Optional, NoReturn
from vehicle import Vehicle, Bus, Car, Bike
from .exceptions import VehicleIsNotPossibleToPlace, IsNotVehicle
from itertools import chain
from .types import ParkingLotsTypes
import config


class ParkingLot:

    # Возможно ли размещение транспорта в слоте?
    def possible_to_place(self, type_of_vehicle: int, vehicle: Vehicle) -> bool:
        return type_of_vehicle in vehicle.required_lot

    def __init__(self, type_of_vehicle: int, vehicle: Optional[Vehicle] = None):
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
    def is_occupied(self) -> bool:
        return bool(self.vehicle)

    @property
    def vehicle(self) -> Optional[Vehicle]:
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle) -> NoReturn:

        if vehicle == None:
            self._vehicle = None
        elif self.possible_to_place(self.type_of_vehicle, vehicle):
            self._vehicle = vehicle
        else:
            raise VehicleIsNotPossibleToPlace

    def __repr__(self) -> str:
        if not self.is_occupied:
            return "Empty"
        return self.vehicle.name

    def __str__(self) -> str:
        if not self.is_occupied:
            return "Empty"
        return self.vehicle.name


class ParkingRow():
    parking_cells: List[ParkingLot] = []
    type_of_row = None

    def __init__(self, row_len, type_of_row):
        self.parking_cells.extend(
            {ParkingLot(type_of_vehicle=type_of_row) for i in range(row_len)}
        )
        self.type_of_row = type_of_row

    def get_free_cells(self) -> int:
        result =  len(list(
            filter(lambda x: not x.is_occupied, self.parking_cells)
        ))
        print(f"Количество свободных мест: {result}")
        return result

    def set_vehicle_to_cell(self, vehicle: Vehicle, count=1):
        for i in range(count):
            if len(list(filter(lambda x: not x.is_occupied, self.parking_cells))) > vehicle.size:
                for vehical_size in range(vehicle.size):
                    cell = next(
                        filter(lambda x: not x.is_occupied, self.parking_cells))
                    self.parking_cells[self.parking_cells.index(
                        cell)].vehicle = vehicle
        print("Машина была припаркована")

    def remove_vehicle_from_cell(self, vehicle: Vehicle):
        cell = next(
            filter(lambda x: x.is_occupied, self.parking_cells))

        self.parking_cells[self.parking_cells.index(cell)].vehicle = None
        print("Машина была убрана с парковки")


""" 
class Parking():
    parking: List[ParkingRow]

    def __init__(self, parking: List[List[ParkingLot]]):
        self.parking = parking

    def get_free_cells(self) -> dict:
        json_to_return = {}
        json_to_return['Bike'] = len(list(filter(lambda x: not x.is_occupied and x.type_of_vehicle == any(
            [1, 2, 3]), chain.from_iterable(self.parking))))
        json_to_return['Car'] = len(list(filter(lambda x: not x.is_occupied and x.type_of_vehicle == any(
            [2, 3]), chain.from_iterable(self.parking))))
        json_to_return['Bus'] = len(list(filter(lambda x: not x.is_occupied and x.type_of_vehicle ==
                                    3, chain.from_iterable(self.parking)))) // config.bus_required  # Автобус может занмать несколько ячеек
        return json_to_return

    def print_free_cells(self) -> None:
        for row in self.parking:
            print(row)

    def get_count_lots_with_vehicle(self) -> dict:
        json_to_return = {}

        json_to_return["Bike"] = len(list(filter(
            lambda x: x.is_occupied and x.vehicle.type_of_vehicle == 1, chain.from_iterable(self.parking))))
        json_to_return["Car"] = len(list(filter(
            lambda x: x.is_occupied and x.vehicle.type_of_vehicle == 2, chain.from_iterable(self.parking))))
        json_to_return["Bus"] = len(list(filter(
            lambda x: x.is_occupied and x.vehicle.type_of_vehicle == 3, chain.from_iterable(self.parking))))

        return json_to_return

    def can_park(self, vehicle: Vehicle):
        return len(list(filter(lambda x: not x.is_occupied and x.type_of_vehicle == any(
                vehicle.required_lot), chain.from_iterable(self.parking)))) > vehicle.size
 """
