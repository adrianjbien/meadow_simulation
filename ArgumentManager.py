import argparse
import configparser


class ArgumentManager:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="This script runs a meadow simulation")
        self.config_parser = configparser.ConfigParser()
        self.parser.add_argument('-s', '--sheep',
                                 help='Number of sheep as integer', type=int, default=15, required=False,
                                 )
        self.parser.add_argument('-r', '--rounds',
                                 help='Maximum number of rounds as integer', type=int, default=50, required=False,
                                 )
        self.parser.add_argument('-w', '--wait',
                                 help='Pausing program after every round information printed', required=False,
                                 action='store_true'
                                 )

        self.parser.add_argument('-c', '--config',
                             help='Filename with configuration', required=False
                             )
        self.parser.add_argument('-l', '--log',
                                 help='Choose file with configuration', required=False
                                 )


    def get_values_from_config(self):
        if self.parser.parse_args().config is None:
            pos_limit = 10
            sheep_move_dis = 0.5
            wolf_move_dis = 1
        else:
            self.config_parser.read(self.parser.parse_args().config)
            pos_limit = self.config_parser.get('Sheep', 'InitPosLimit')
            sheep_move_dis = self.config_parser.get('Sheep', 'MoveDist')
            wolf_move_dis = self.config_parser.get('Wolf', 'MoveDist')

        return int(pos_limit), float(sheep_move_dis), float(wolf_move_dis)

