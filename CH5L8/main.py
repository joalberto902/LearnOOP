class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
        return (self.pos_x >= x_1 and self.pos_x <= x_2) and (self.pos_y >= y_1 and self.pos_y <= y_2)

class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, fire_range: int) -> None:
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x: int, y: int, units: list[Unit]) -> list[Unit]:
        x_1 = x - self.__fire_range
        y_1 = y - self.__fire_range
        x_2 = x + self.__fire_range
        y_2 = y + self.__fire_range
        in_area_units: list[Unit] =  []
        for unit in units:
            if unit.in_area(x_1, y_1, x_2, y_2):
                in_area_units.append(unit)
        return in_area_units.copy()