
class ParkingLotsTypes():
    BIKE_LOT = 1
    COMPACT_LOT = 2
    BIG_LOT = 3
    

class ParkingLot():
    type: int
    isOccupied: bool

    def __init__(self, type) -> None:
        self.type = type
        self.isOccupied = False
    
    def MarkAsOccupied(self):
        self.isOccupied = True
        
    def MarkAsUnoccupied(self):
        self.isOccupied = False


class Parking():
    pass

