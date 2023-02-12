class Game:
    """Базовый класс игры"""
    def __init__(self, name: str, max_number_of_players: int):
        """
        Создание и подготовка к работе объекта "Игра"
        :param name: Название игры
        :param max_number_of_players: Максимально допустимое число игроков
        """
        self.name = name
        self.max_number_of_players = max_number_of_players

    def __str__(self) -> str:
        return f"Игра {self.name}. Максимально допустимое число игроков {self.max_number_of_players}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, " \
               f"Максимально допустимое число игроков={self.max_number_of_players})"

    def checking_of_players(self, number_of_players_now: int) -> None:
        """
        Функция проверяющая подходит ли данная игра для стольки человек
        :param number_of_players_now: Сколько из игроков хотят играть
        """
        if number_of_players_now > self.max_number_of_players:
            print("Данная игра не предназначена для такого количества игроков")
        if number_of_players_now >= 1:
            print(f"Игра подходит для {number_of_players_now} игроков")
        else:
            raise ValueError("Количество игроков не может быть меньше 1")


class VideoGame(Game):
    """Класс ВидеоИгры"""
    def __init__(self, name: str, max_number_of_players: int, type_of_multiplayer: str):
        """
        Создание и подготовка к работе объекта "ВидеоИгра"
        :param name: Название видеоигры
        :param max_number_of_players: Максимально допустимое число игроков
        :param max_number_of_players: Тип мультиплеера
        """
        super().__init__(name, max_number_of_players)
        self.type_of_multiplayer = type_of_multiplayer

    def checking_for_interest(self, number_of_players_now: int) -> int:
        """
        Функция проверяющая подходит ли данная игра для заинтересованных игроков
        :param number_of_players_now: Сколько из игроков хотят играть
        :return: Возвращает количество игроков, котоыре заинтересованы в данной игре
        исходя из предпочтений в типе мультиплеера
        """
        if self.type_of_multiplayer == "mmo":
            return round(number_of_players_now * 0.7)
        if self.type_of_multiplayer == "coop":
            return round(number_of_players_now * 0.8)
        if self.type_of_multiplayer == "session":
            return round(number_of_players_now * 0.9)

    def __str__(self) -> str:
        return f"Игра {self.name}. Максимально допустимое число игроков {self.max_number_of_players}." \
               f" Тип мультиплеера={self.type_of_multiplayer!r}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Название={self.name!r}, " \
               f"Максимально допустимое число игроков={self.max_number_of_players}, " \
               f"Тип мультиплеера={self.type_of_multiplayer!r})"


if __name__ == "__main__":
    a = Game("вышибалы", 12)
    b = VideoGame("WoW", 1000, "mmo")
    c = Game.checking_of_players(a, 1)
    r = VideoGame.checking_of_players(b, 888)
    e = VideoGame.checking_for_interest(b, 85)
    print(e)
    pass
