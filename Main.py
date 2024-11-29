from SimulationController import SimulationController
from Wolf import Wolf

if __name__ == '__main__':
    # parameters
    number_of_sheeps = 15
    xy_limit = 10
    sheep_step_length = 0.5
    wolf_step_length = 1
    max_round_num = 50
    json = 'pos.json'
    csv = 'alive.csv'

    simulation = SimulationController(max_round_num, number_of_sheeps, xy_limit, sheep_step_length, wolf_step_length, json, csv)
    simulation.start_simulation()
    # wolf = Wolf(wolf_step_length)
