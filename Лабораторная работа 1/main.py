import doctest

# TODO Написать 3 класса с документацией и аннотацией типов


class Computer:
    def __init__(self, cpu_model: str, ram_size: int, gpu_memory_size: int):

        """
        Создание и подготовка к работе объекта "Компьютер"
        :param cpu_model: Модель процессора
        :param ram_size: Объем оперативной памяти
        :param gpu_memory_size: Объем видеопамяти
        Примеры:
        >>> computer = Computer("Ryzen 3600", 16, 8)  # инициализация экземпляра класса
        """
        if not isinstance(cpu_model, str):
            raise TypeError("Модель процессора должна быть типа str")
        self.cpu_model = cpu_model

        if not isinstance(ram_size, int):
            raise TypeError("Объем оперативной памяти должен быть типа int")
        if ram_size <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным числом")
        self.ram_size = ram_size

        if not isinstance(gpu_memory_size, int):
            raise TypeError("Объем видеопамяти должен быть типа int")
        if gpu_memory_size <= 0:
            raise ValueError("Объем видеопамяти должен быть положительным числом")
        self.gpu_memory_size = gpu_memory_size

    def is_computer_for_gaming(self) -> bool:
        """
        Функция которая проверяет является ли компьютер игровым
        :return: Является ли компьютер игровым
        Примеры:
        >>> computer = Computer("Ryzen 3600", 16, 8)
        >>> computer.is_computer_for_gaming()
        """
        ...

    def check_ram_size(self, needed_ram: int) -> None:
        """
        Проверка на достаточность оперативной памяти.
        :param needed_ram: Объем необходимой оперативной памяти
        :return: Достаточно ли оперативной памяти в компьютере
        >>> computer = Computer("Ryzen 3600", 16, 8)
        >>> computer.check_ram_size(32)
        """
        if not isinstance(needed_ram, int):
            raise TypeError("Объем оперативной памяти должен быть типа int")
        if needed_ram < 0:
            raise ValueError("Объем необходимой оперативной памяти должен быть положительным числом")
        ...

    def upgrade_ram(self, adding_ram: int) -> None:
        """
        Добавление оперативной памяти.
        :param adding_ram: Объем добавляемой оперативной памяти
        >>> computer = Computer("Ryzen 3600", 16, 8)
        >>> computer.upgrade_ram(16)
        """
        if adding_ram < 0:
            raise ValueError("Добавляемая оперативная память должна быть положительным числом")
        ...


class ComputerMouse:
    def __init__(self, mouse_model: str, mouse_weight: int):

        """
        Создание и подготовка к работе объекта "Компьютерная мышка"
        :param mouse_model: Модель мыши
        :param mouse_weight: Вес мыши
        Примеры:
        >>> computer_mouse = ComputerMouse("HyperX pulsefire haste", 65)  # инициализация экземпляра класса
        """
        if not isinstance(mouse_model, str):
            raise TypeError("Модель мышки должна быть типа str")
        self.mouse_model = mouse_model

        if not isinstance(mouse_weight, int):
            raise TypeError("Вес мыши должен быть типа int")
        if mouse_weight <= 0:
            raise ValueError("Вес мыши должен быть положительным числом")
        self.mouse_weight = mouse_weight

    def is_mouse_for_gaming(self) -> bool:
        """
        Функция которая проверяет является ли мышь игровой
        :return: Является ли мышь игровой
        Примеры:
        >>> computer_mouse = ComputerMouse("HyperX pulsefire haste", 65)
        >>> computer_mouse.is_mouse_for_gaming()
        """
        ...

    def is_mouse_lightweight(self) -> bool:
        """
        Проверка на легкость мыши.
        :return: Является ли мышь легкой по весу
        >>> computer_mouse = ComputerMouse("HyperX pulsefire haste", 65)
        >>> computer_mouse.is_mouse_lightweight()
        """
        ...


class ComputerSpeakers:
    def __init__(self, speakers_model: str, volume: int):

        """
        Создание и подготовка к работе объекта "Компьютерные колонки"
        :param speakers_model: Модель колонок
        :param volume: Громкость колонок
        Примеры:
        >>> computer_speakers = ComputerSpeakers("Razer Nommo", 30)  # инициализация экземпляра класса
        """
        if not isinstance(speakers_model, str):
            raise TypeError("Модель колонок должна быть типа str")
        self.speakers_model = speakers_model

        if not isinstance(volume, int):
            raise TypeError("Громкость должнв быть типа int")
        if volume <= 0:
            raise ValueError("Громкость должена быть положительным числом")
        if volume > 100:
            raise ValueError("Громкость не может быть больше 100%")
        self.volume = volume

    def is_speakers_compatible(self) -> bool:
        """
        Функция которая проверяет совместимость колонок
        :return: Являются ли колонки совместимыми с системой
        Примеры:
        >>> computer_speakers = ComputerSpeakers("Razer Nommo", 30)
        >>> computer_speakers.is_speakers_compatible()
        """
        ...

    def add_volume(self, needed_volume: int) -> None:
        """
        Добавление громкости
        :param needed_volume: % добавляемой громкости
        >>> computer_speakers = ComputerSpeakers("Razer Nommo", 30)
        >>> computer_speakers.add_volume(50)
        """
        if not isinstance(needed_volume, int):
            raise ("% добавляемой громкости должен быть типа int")
        if needed_volume <= 0:
            raise ("% добавляемой громкости должен быть положительным числом")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
