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
        self.parking_cells = list(
            [ParkingLot(type_of_vehicle=type_of_row) for i in range(row_len)])

        self.type_of_row = type_of_row

    def get_free_cells(self) -> int:
        result = len(list(
            filter(lambda x: not x.is_occupied, self.parking_cells)
        ))
        return result

    def can_park_vehicle(self, vehicle: Vehicle) -> bool:
        if len(list(filter(lambda x: x.is_occupied != True, self.parking_cells))) >= vehicle.size: #Хватает ли мест для парковки?
            if self.type_of_row >= vehicle.type_of_vehicle:
                return True
        else:
            return False

    def set_vehicle_to_cell(self, vehicle: Vehicle, count=1) -> NoReturn:
        for i in range(count):
            if len(list(filter(lambda x: not x.is_occupied, self.parking_cells))) >= vehicle.size:#Проверяем, есть ли куда ставить
                for vehical_size in range(vehicle.size):
                    cell = next(
                        filter(lambda x: not x.is_occupied, self.parking_cells)) # Ищем не занятые месте
                    self.parking_cells[self.parking_cells.index(
                        cell)].vehicle = vehicle

    def remove_vehicle_from_cell(self, vehicle: Vehicle):
        if len(list(filter(lambda x: x.is_occupied, self.parking_cells))) >= vehicle.size: #Проверяем, есть ли что удалять 
            for vehical_size in range(vehicle.size): #Нужно для машин большого размера
                try:
                    cell = next(
                        filter(lambda x: x.is_occupied, self.parking_cells))# Ищем занятые месте
                    self.parking_cells[self.parking_cells.index(
                        cell)].vehicle = None

                except StopIteration:
                    pass

    def __repr__(self) -> str:
        return str(self.parking_cells)

    def __str__(self) -> str:
        return str(self.parking_cells)


class Parking():
    parking: List[ParkingRow]

    def __init__(self, parking: List[ParkingRow]):
        self.parking = parking

    def get_free_cells(self):
        json_to_return = {"For bike places": 0,
                          "Compact places": 0, "Big places": 0}
        for row in self.parking: #Для каждого ряда ищем парковочные места

            if row.type_of_row == ParkingLotsTypes.BIKE_LOT:
                json_to_return["For bike places"] += row.get_free_cells()
            if row.type_of_row == ParkingLotsTypes.COMPACT_LOT:
                json_to_return["Compact places"] += row.get_free_cells()
            if row.type_of_row == ParkingLotsTypes.BIG_LOT:
                json_to_return["Big places"] += row.get_free_cells()
        print(json_to_return)

    #Припарковать машину
    def park_vehicle(self, vehicle: Vehicle):
        for row in self.parking:
            if row.can_park_vehicle(vehicle): #Проверяем можем ли мы припарковать машину
                row.set_vehicle_to_cell(vehicle)
                break
        print("Машина была припаркована")

    #Убрать машину с парковки
    def unpark_vehicle(self, vehicle: Vehicle):
        for row in self.parking:
            if row.type_of_row >= vehicle.type_of_vehicle:
                row.remove_vehicle_from_cell(vehicle)
        print("Машина была убрана с парковки")

    #Красивый вывод парковочных мест
    def print_parking(self):
        for row in self.parking:
            print(row)
