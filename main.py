from vehicle import *
from parking.parking import ParkingLot, ParkingRow, Parking
from parking.types import ParkingLotsTypes



park = Parking(
    [
        ParkingRow(6, ParkingLotsTypes.BIKE_LOT),
        ParkingRow(6, ParkingLotsTypes.COMPACT_LOT),
        ParkingRow(6, ParkingLotsTypes.BIG_LOT),
    ]
)

park.get_free_cells()
park.park_vehicle(Car())
park.get_free_cells()
park.unpark_vehicle(Car())
park.get_free_cells()
print('\n')


for i in range(8):
    park.park_vehicle(Car())

print('\n')

park.print_parking()
for i in range(8):
    park.unpark_vehicle(Car())


park.print_parking()