from Animal import Animal


class Wolf(Animal):
    def __init__(self, step_length):  # start wilka z pozycji (0,0)
        init_x = 0.0
        init_y = 0.0
        super().__init__(init_x, init_y, step_length)

    def sheep_to_wolf_distance(self, sheep):
        return ((self.get_x_cord - sheep.get_x_cord()) ** 2 + (self.get_y_cord - sheep.get_y_cord()) ** 2) ** 0.5

    def find_closest_sheep(self, sheep):
        closest = sheep[0]
        for sh in sheep:
            if self.sheep_to_wolf_distance(sh) < self.sheep_to_wolf_distance(closest):
                closest = sh
        return closest

    def is_sheep_in_range(self):
        cos = 0

    def move(self):
        self.position.x = 2
        self.position.y = 2
        # implementacja kroku i sprawdzanie ktora owca jest najblizej i czy jest w zasiegu
