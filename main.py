from vehicle import *
from parking.parking import ParkingLot, ParkingRow
from parking.types import ParkingLotsTypes




row = ParkingRow(6, ParkingLotsTypes.BIG_LOT)
print(
    row.get_free_cells()
)

row.set_vehicle_to_cell(Bike())
print(
    row.get_free_cells()
)

row.remove_vehicle_from_cell(Bike())
print(
    row.get_free_cells()
)

row.set_vehicle_to_cell(Bus())
print(
    row.get_free_cells()
)

row.remove_vehicle_from_cell(Bus())
print(
    row.get_free_cells()
)
