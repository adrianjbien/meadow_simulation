from Animal import Animal


class Wolf(Animal):
    def __init__(self, init_x, init_y, step_length):  # start wilka z pozycji (0,0)
        super().__init__(init_x, init_y, step_length)

    def move(self):
        self.position.x = 2
        self.position.y = 2
        # implementacja kroku i sprawdzanie ktora owca jest najblizej i czy jest w zasiegu
