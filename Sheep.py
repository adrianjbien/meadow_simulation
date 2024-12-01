import random
import logging

from adodbapi.ado_consts import directions

from Animal import Animal


class Sheep(Animal):
    def __init__(self, xy_limit, step_length, sequence_num):
        init_x = random.uniform(-1 * xy_limit, xy_limit)
        init_y = random.uniform(-1 * xy_limit, xy_limit)
        super().__init__(init_x, init_y, step_length)
        self.direction = 0
        self.alive = True
        self.sequence_num = sequence_num
        logging.debug("Initial position of a sheep "
                      + str(self.sequence_num)
                      + " was determined: ("
                      + str(init_x)
                      + ", "
                      + str(init_y)
                      + ")"
                      )
        self.direction_map = {
            0: "North",
            1: "East",
            2: "South",
            3: "West"
        }

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

            logging.debug("Sheep "
                          + str(self.sequence_num)
                          + " randomly chose a direction of movement: "
                          + self.direction_map[self.direction]
                          )

            if self.direction == 0:
                self.set_y_cord(self.get_y_cord() + self.step_length)
            elif self.direction == 2:
                self.set_y_cord(self.get_y_cord() - self.step_length)
            elif self.direction == 1:
                self.set_x_cord(self.get_x_cord() + self.step_length)
            elif self.direction == 3:
                self.set_x_cord(self.get_x_cord() - self.step_length)

            logging.debug("Sheep "
                          + str(self.sequence_num)
                          + " moved, new position: ("
                          + str(self.get_x_cord())
                          + ", "
                          + str(self.get_y_cord())
                          + ")"
                          )
