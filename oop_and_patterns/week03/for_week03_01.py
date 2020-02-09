class System:

    def __init__(self):
        """
        В системе в конструкторе создается двухмерная, карта, на которой
        источники света обозначены как 1, а препятствия как -1.
        """
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены
        self.map[19][11] = 1

    def get_lightening(self, light_mapper):
        """
        Метод get_lightening принимает в качестве аргумента объект, который
        должен посчитывать освещение. У объекта вызывается метод lighten,
        который принимает карту объектов и источников света и возвращает карту
        освещенности.
        :param light_mapper:
        :return:
        """
        self.lightmap = light_mapper.lighten(self.map)


class Light:

    def __init__(self, dim):
        """
        Класс Light создает в методе __init__ поле заданного размера.
        :rtype dim: tuple
        :param dim: tuple where dim[1] - height and dim[0] - width
        """
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        """
        Метод set_lights устанавливает массив источников света с заданными
        координатами и просчитывает освещение.
        :param lights:
        :return:
        """
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        """
        Метод set_obstacles устанавливает препятствия аналогичным образом.
        Положение элементов задается списком кортежей. В каждом элементе кортежа
        хранятся 2 значения: elem[0] -- координата по ширине карты и
        elem[1] -- координата по высоте соответственно.
        :param obstacles: list[tuple] where elem[0] - width and elem[1] - height
        :return:
        """
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        """
        Метод generate_lights рассчитывает освещенность с
        учетом источников и препятствий.
        :return:
        """
        return self.grid.copy()
