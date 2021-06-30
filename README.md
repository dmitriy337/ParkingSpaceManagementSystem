# Система для контроля парковки автомобилей

## Для запуска:
```python
python3 main.py
```
## Для взаимодействия:

Создание парковки, первым параметром передём длинну ряда

```python 
park = Parking(
    [
        ParkingRow(6, ParkingLotsTypes.BIKE_LOT),
        ParkingRow(6, ParkingLotsTypes.COMPACT_LOT),
        ParkingRow(6, ParkingLotsTypes.BIG_LOT),
    ]
)
```

Для вывода свободных мест

```python
park.get_free_cells()

#Output {'For bike places': 6, 'Compact places': 6, 'Big places': 6}
```

Для парковки транспорта

```python
#Парковка
park.park_vehicle(Car())
#Убираем с парковки
park.unpark_vehicle(Car())
```

Красивый вывод парковочных мест 

```python
park.print_parking()

#Output
[Bike, Bike, Bike, Empty, Empty, Empty]
[Car, Car, Car, Car, Car, Car]
[Car, Bus, Bus, Bus, Bus, Bus]
```



## Принцип работы:

Для работы с парсовочными местами используется 3 класса:

- Класс парковочного места, в нём же и расположены проверки на возможность парковки
- Класс ряда с парковочными местами
- Класс парковки с парковочными рядами

Для парковки мы смотрим в класс ряда и проверяем, хватает ли нам кол-ва парковочных мест, если да - паркуем

Для убирания транспорта с парковки проверяем, хватает ли кол-ва занятых ячеек

