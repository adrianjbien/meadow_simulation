from SimulationController import SimulationController
from Wolf import Wolf

if __name__ == '__main__':
    # parameters
    num_of_sheep = 15
    xy_limit = 10
    sheep_step_length = 0.5
    wolf_step_length = 1
    max_round_num = 50

    simulation = SimulationController(max_round_num)
    wolf = Wolf(wolf_step_length)
    sheep = simulation.init_sheep(num_of_sheep, xy_limit, sheep_step_length)



    for i in range(max_round_num + 1):
        print("round number : " + str(round_num))

        sheep[0].move()
        wolf.move(sheep)