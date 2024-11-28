import random

from Animal import Animal


class Sheep(Animal):
    def __init__(self, xy_limit, step_length, sequence_num):
        init_x = random.uniform(-1 * xy_limit, xy_limit)
        init_y = random.uniform(-1 * xy_limit, xy_limit)
        super().__init__(init_x, init_y, step_length)
        self.direction = 0  # zrobic kierunki swiata jako 0,1,2,3 ????
        self.alive = True
        self.sequence_num = sequence_num

    def set_sequence_num(self, sequence_num):
        self.sequence_num = sequence_num

    def get_sequence_num(self):
        return self.sequence_num

    def set_alive(self, condition):
        self.alive = condition

    def is_alive(self):
        return self.alive

    def set_random_direction(self):
        self.direction = random.randint(0, 3)

    def move(self):
        if self.alive:
            self.set_random_direction()
            if self.direction == 0: # jesli kierunek 0 (north) idzie do gory o dlugosc kroku itd.
                self.set_y_cord(self.get_y_cord() + self.step_length)
            elif self.direction == 2:
                self.set_y_cord(self.get_y_cord() - self.step_length)
            elif self.direction == 1:
                self.set_x_cord(self.get_x_cord() + self.step_length)
            elif self.direction == 3:
                self.set_x_cord(self.get_x_cord() - self.step_length)


