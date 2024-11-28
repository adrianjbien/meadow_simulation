import math

from Animal import Animal


class Wolf(Animal):
    def __init__(self, step_length):  # start wilka z pozycji (0,0)
        init_x = 0.0
        init_y = 0.0
        self.target = None
        super().__init__(init_x, init_y, step_length)



    def sheep_to_wolf_distance(self, sh):
        return ((self.get_x_cord() - sh.get_x_cord()) ** 2 + (self.get_y_cord() - sh.get_y_cord()) ** 2) ** 0.5


    def find_closest_sheep(self, sheep):
        closest = sheep[0]
        for sh in sheep:
            if sh.is_alive() and self.sheep_to_wolf_distance(sh) < self.sheep_to_wolf_distance(closest):
                closest = sh
        self.target = closest

    def calculate_angle(self, sheep):
        return math.atan2(self.get_y_cord() - sheep.get_y_cord(), self.get_x_cord() - sheep.get_x_cord())


    def move(self, sheep=None):  # dodanie parametru mimo ze nie ma go w metodzie klasy bazowej,
        self.find_closest_sheep(sheep)

        if self.sheep_to_wolf_distance(self.target) <= self.step_length:
            self.target.set_alive = False
            self.set_x_cord(self.target.get_x_cord())
            self.set_y_cord(self.target.get_y_cord())
        else:
            angle = self.calculate_angle(self.target)
            new_x = self.get_x_cord() - (self.step_length * math.cos(angle))
            new_y = self.get_y_cord() - (self.step_length * math.sin(angle))
            self.set_x_cord(new_x)
            self.set_y_cord(new_y)


