from Sheep import Sheep
from Wolf import Wolf
from Writer import Writer
import logging


class SimulationController:

    def __init__(self, max_round_num, number_of_sheep, xy_limit, sheep_step_length, wolf_step_length, json, csv):
        self.max_round_num = max_round_num
        self.round_count = 1
        self.sheeps = [Sheep(xy_limit, sheep_step_length, x + 1) for x in range(number_of_sheep)]
        self.wolf = Wolf(wolf_step_length)
        self.writer = Writer(json, csv)


    def get_round_count(self):
        return self.round_count

    def increment_round_count(self):
        self.round_count += 1

    def make_json_log(self):
        return {'round_no': self.round_count,
                'wolf_pos': (self.wolf.get_x_cord(), self.wolf.get_y_cord()),
                'sheep_pos': [(sheep.get_x_cord(), sheep.get_y_cord()) if sheep.is_alive() else None for sheep in self.sheeps]
                }

    # def init_sheep(self, number_of_sheep, xy_limit, step_length):
    #     return [Sheep(xy_limit, step_length, x + 1) for x in range(number_of_sheep)]

    # def wolf_position_info(self, wolf):
    #     print("Wolf's position:  (" + str(round(wolf.get_x_cord(), 3)) + ", " + str(round(wolf.get_y_cord(), 3)) + ")")
    
    def wolf_position_info(self):
         print("Wolf's position:  (" + str(round(self.wolf.get_x_cord(), 3)) + ", " + str(round(self.wolf.get_y_cord(), 3)) + ")")

    def round_number_info(self):
        print("Round number: " + str(self.round_count))

    def count_alive_sheeps(self):
        count = 0
        for sheep in self.sheeps:
            if sheep.alive:
                count += 1
        return count

    def start_simulation(self, with_pause=False):
        
        for i in range(self.max_round_num):
            for sheep in self.sheeps:
                sheep.move()

            self.wolf.move(self.sheeps)
            self.round_number_info()
            if self.wolf.target.is_alive():
                print("Wolf is chasing the sheep " + str(self.wolf.target.get_sequence_num()))
            else:
                print("Wolf ate the sheep " + str(self.wolf.target.get_sequence_num()))


            print("Sheep " + str(self.wolf.target.sequence_num) + " position:  (" + str(
                round(self.wolf.target.get_x_cord(), 3)) + ", " + str(
                round(self.wolf.target.get_y_cord(), 3)) + ")")
            print("Number of alive sheep: " + str(self.count_alive_sheeps()))
            self.wolf_position_info()
            
            if self.count_alive_sheeps() == 0:
                print("There is no sheep alive left")
                exit(0)

            print('\n')

            log = self.make_json_log()
            self.writer.write_to_json(log)
            self.writer.write_to_csv(self.get_round_count(), self.count_alive_sheeps())

            self.increment_round_count()
            if with_pause:
                input("Press Enter to continue...")



