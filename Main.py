from SimulationController import SimulationController
from ArgumentManager import ArgumentManager
from Wolf import Wolf
import logging

if __name__ == '__main__':
    pars = ArgumentManager()
    args = pars.parser.parse_args()


    # parameters
    number_of_sheeps = args.sheep
    with_pause = args.wait
    xy_limit, sheep_step_length, wolf_step_length = pars.get_values_from_config()
    max_round_num = args.rounds

    log_level = pars.get_logging_level()

    if log_level:
        logging.basicConfig(level=log_level, filename="chase.log", filemode="w")

    json = 'pos.json'
    csv = 'alive.csv'

    simulation = SimulationController(max_round_num, number_of_sheeps, xy_limit, sheep_step_length, wolf_step_length, json, csv)
    simulation.start_simulation(with_pause)
