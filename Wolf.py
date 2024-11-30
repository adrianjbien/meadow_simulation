import math
import logging
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
            if not closest.is_alive():
                closest = sh
            if sh.is_alive() and self.sheep_to_wolf_distance(sh) < self.sheep_to_wolf_distance(closest):
                closest = sh
        self.target = closest

    def calculate_angle(self, sheep):
        return math.atan2(self.get_y_cord() - sheep.get_y_cord(), self.get_x_cord() - sheep.get_x_cord())


    def move(self, sheep=None):  # dodanie parametru mimo ze nie ma go w metodzie klasy bazowej,
        self.find_closest_sheep(sheep)
        distance = self.sheep_to_wolf_distance(self.target)

        logging.debug("The closest sheep " + str(self.target.sequence_num)
                      + " is in distance of " + str(distance))


        if distance <= self.step_length:
            self.target.set_alive(False)
            self.set_x_cord(self.target.get_x_cord())
            self.set_y_cord(self.target.get_y_cord())
            logging.info("A " + str(self.target.sequence_num) + " sheep was eaten")
        else:
            logging.info("The wolf is chasing sheep " + str(self.target.sequence_num))
            angle = self.calculate_angle(self.target)
            new_x = self.get_x_cord() - (self.step_length * math.cos(angle))
            new_y = self.get_y_cord() - (self.step_length * math.sin(angle))
            self.set_x_cord(new_x)
            self.set_y_cord(new_y)
        logging.debug("The wolf moved to position: (" + str(self.get_x_cord()) + ", " + str(self.get_y_cord()) + ")" )
        logging.info("The wolf moved")


