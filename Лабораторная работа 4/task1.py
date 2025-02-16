# -*- coding: utf-8 -*-

class MusicalInstrument:
    """
    Базовый класс для музыкальных инструментов.
    """
    name: str
    _material: str
    price: float

    def __init__(self, name: str, material: str, price: float) -> None:
        """
        Инициализация музыкального инструмента.
        :param name: Название инструмента
        :param material: Материал изготовления
        :param price: Цена инструмента
        """
        self.name = name
        self._material = material  # Инкапсуляция, материал только для чтения
        self.price = price

    @property
    def material(self) -> str:
        return self._material

    def __str__(self) -> str:
        return f"{self.name} (Материал: {self._material}, Цена: {self.price} руб.)"

    def __repr__(self) -> str:
        return f"MusicalInstrument(name={self.name!r}, material={self._material!r}, price={self.price!r})"

    def play_sound(self) -> str:
        """
        Абстрактный метод, должен быть переопределен в дочерних классах.
        """
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")


class StringInstrument(MusicalInstrument):
    """
    Класс для струнных инструментов.
    """
    number_of_strings: int

    def __init__(self, name: str, material: str, price: float, number_of_strings: int) -> None:
        """
        Инициализация струнного инструмента.
        :param number_of_strings: Количество струн
        """
        super().__init__(name, material, price)
        self.number_of_strings = number_of_strings

    def __str__(self) -> str:
        return (f"{self.name} (Материал: {self.material}, Струн: {self.number_of_strings}, "
                f"Цена: {self.price} руб.)")

    def __repr__(self) -> str:
        return (f"StringInstrument(name={self.name!r}, material={self.material!r}, "
                f"price={self.price!r}, number_of_strings={self.number_of_strings!r})")

    def play_sound(self) -> str:
        return f"{self.name} издает звук за счет вибрации {self.number_of_strings} струн."


class KeyboardInstrument(MusicalInstrument):
    """
    Класс для клавишных инструментов.
    """
    has_pedals: bool

    def __init__(self, name: str, material: str, price: float, has_pedals: bool) -> None:
        """
        Инициализация клавишного инструмента.
        :param has_pedals: Наличие педалей
        """
        super().__init__(name, material, price)
        self.has_pedals = has_pedals

    def __str__(self) -> str:
        pedals_info = "есть" if self.has_pedals else "нет"
        return f"{self.name} (Материал: {self.material}, Педали: {pedals_info}, Цена: {self.price} руб.)"

    def __repr__(self) -> str:
        return (f"KeyboardInstrument(name={self.name!r}, material={self.material!r}, "
                f"price={self.price!r}, has_pedals={self.has_pedals!r})")

    def play_sound(self) -> str:
        return f"{self.name} издает звук при нажатии клавиш."


if __name__ == "__main__":
    guitar = StringInstrument("Гитара", "Дерево", 15000.0, 6)
    piano = KeyboardInstrument("Фортепиано", "Дерево и металл", 120000.0, True)

    print(guitar)
    print(guitar.play_sound())
    print(piano)
    print(piano.play_sound())
