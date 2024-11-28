from SimulationController import SimulationController
from Wolf import Wolf

if __name__ == '__main__':
    # parameters
    num_of_sheep = 5
    xy_limit = 1
    sheep_step_length = 0.5
    wolf_step_length = 1
    max_round_num = 50

    simulation = SimulationController(max_round_num)
    wolf = Wolf(wolf_step_length)

    simulation.start_simulation(wolf,num_of_sheep, xy_limit, sheep_step_length)