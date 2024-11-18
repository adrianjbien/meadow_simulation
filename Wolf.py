import math

from Animal import Animal


class Wolf(Animal):
    def __init__(self, step_length):  # start wilka z pozycji (0,0)
        init_x = 0.0
        init_y = 0.0
        super().__init__(init_x, init_y, step_length)


    def sheep_to_wolf_distance(self, sh):
        return ((self.get_x_cord - sh.get_x_cord()) ** 2 + (self.get_y_cord - sh.get_y_cord()) ** 2) ** 0.5


    def find_closest_sheep(self, sheep):
        closest = sheep[0]
        for sh in sheep:
            if self.sheep_to_wolf_distance(sh) < self.sheep_to_wolf_distance(closest):
                closest = sh
        return closest

    def calculate_angle(self, sheep):
        return math.atan2(self.get_y_cord() - sheep.get_y_cord(), self.get_x_cord() - sheep.get_x_cord())


    def move(self, sheep=None):  # dodanie parametru mimo ze nie ma go w metodzie klasy bazowej,
        closest_sheep = self.find_closest_sheep(sheep)

        if self.sheep_to_wolf_distance(closest_sheep) <= self.step_length:
            closest_sheep.set_alive = False
            self.set_x_cord(closest_sheep.get_x_cord())
            self.set_y_cord(closest_sheep.get_y_cord())
        else:
            angle = self.calculate_angle(closest_sheep)
            self.set_x_cord(closest_sheep.get_x_cord() + (self.step_length * math.cos(angle)))
            self.set_y_cord(closest_sheep.get_y_cord() + (self.step_length * math.sin(angle)))

