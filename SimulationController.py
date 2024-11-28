from Sheep import Sheep
from Wolf import Wolf


class SimulationController: # klasa laczaca wszystko i rozpoczynajaca symulacje # do zmiany

    def __init__(self, max_round_num):
        self.max_round_num = max_round_num
        self.round_count = 1

    def get_round_count(self):
        return self.round_count

    def increment_round_count(self):
        self.round_count += 1

    def init_sheep(self, number_of_sheep, xy_limit, step_length):
        return [Sheep(xy_limit, step_length, x + 1) for x in range(number_of_sheep)]

    def wolf_position_info(self, wolf):
        print("Wolf's position:  (" + str(round(wolf.get_x_cord(), 3)) + ", " + str(round(wolf.get_y_cord(), 3)) + ")")

    def round_number_info(self):
        print("Round number: " + str(self.round_count))

    def count_alive_sheep(self, sheep_list):
        count = 0
        for sheep in sheep_list:
            if sheep.alive:
                count += 1
        return count

    def start_simulation(self, wolf, num_of_sheep, xy_limit, sheep_step_length):
        sheep = self.init_sheep(num_of_sheep, xy_limit, sheep_step_length)

        for i in range(self.max_round_num):
            for sh in sheep:
                sh.move()

            wolf.move(sheep)
            self.round_number_info()
            if wolf.target.is_alive():
                print("Wolf is chasing the sheep " + str(wolf.target.get_sequence_num()))
            else:
                print("Wolf ate the sheep " + str(wolf.target.get_sequence_num()))


            print("Sheep " + str(wolf.target.sequence_num) + " position:  (" + str(
                round(wolf.target.get_x_cord(), 3)) + ", " + str(
                round(wolf.target.get_y_cord(), 3)) + ")")
            print("Number of alive sheep: " + str(self.count_alive_sheep(sheep)))
            self.wolf_position_info(wolf)
            self.increment_round_count()

            if self.count_alive_sheep(sheep) == 0:
                print("There is no sheep alive left")
                exit(0)

            print('\n')







