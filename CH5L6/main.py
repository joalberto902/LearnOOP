class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.__name = name
        self.__health = health

    def get_name(self) -> str:
        return self.__name

    def get_health(self) -> int:
        return self.__health

    def take_damage(self, damage: int) -> None:
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name: str, health: int, num_arrows: int) -> None:
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target: Hero) -> None:
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


# don't touch above this line


class Wizard(Hero):
    def __init__(self, name: str, health: int, mana: int) -> None:
        super().__init__(name, health)
        self.__mana: int = mana

    def cast(self, target: Hero) -> None:
        cost_of_spell_cast = 25
        if self.__mana < cost_of_spell_cast:
            raise Exception("not enough mana") 
        
        self.__mana -= cost_of_spell_cast
        target.take_damage(25)
