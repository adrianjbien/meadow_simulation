import argparse
import configparser
import os
import logging


class ArgumentManager:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="This script runs a meadow simulation")
        self.config_parser = configparser.ConfigParser()
        self.parser.add_argument('-s', '--sheep',
                                 help='Number of sheep as integer', type=self.check_conditions, default=15, required=False,
                                 )
        self.parser.add_argument('-r', '--rounds',
                                 help='Maximum number of rounds as integer', type=self.check_conditions, default=50, required=False,
                                 )
        self.parser.add_argument('-w', '--wait',
                                 help='Pausing program after every round', required=False,
                                 action='store_true'
                                 )

        self.parser.add_argument('-c', '--config',
                             help='Filename with configuration', required=False
                             )
        self.parser.add_argument('-l', '--log',
                                 help='Choose file with configuration', required=False
                                 )

    def check_conditions(self, value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError("Value must be greater than 0")
        return ivalue

    def get_logging_level(self):
        temp = self.parser.parse_args().log
        print(type(temp))
        if temp:
            match temp.upper():
                case "INFO":
                    return logging.INFO
                case "DEBUG":
                    return logging.DEBUG
                case "WARNING":
                    return logging.WARNING
                case "ERROR":
                    return logging.ERROR
                case "CRITICAL":
                    return logging.CRITICAL
                case _:
                    raise argparse.ArgumentTypeError("Invalid logging argument value")
        else:
            return None


    def get_values_from_config(self):
        temp = self.parser.parse_args().config
        if temp is None:  # jesli nie podano argumentu --config
            pos_limit = 10
            sheep_move_dis = 0.5
            wolf_move_dis = 1
        else:
            if os.path.exists(temp):  # jesli podany plik konfiguarcyjny istnieje
                self.config_parser.read(temp)
                pos_limit = self.config_parser.get('Sheep', 'InitPosLimit')
                sheep_move_dis = self.config_parser.get('Sheep', 'MoveDist')
                wolf_move_dis = self.config_parser.get('Wolf', 'MoveDist')
                logging.debug(f"Values from a configuration file were loaded \n pos_limit: {pos_limit},"
                              f" sheep_move_dis: {sheep_move_dis}, wolf_move_dis: {wolf_move_dis}")

            else:
                raise FileNotFoundError("File " + str(temp) + " not found")
        try:
            pos_limit = float(pos_limit)
            sheep_move_dis = float(sheep_move_dis)
            wolf_move_dis = float(wolf_move_dis)

            if pos_limit > 0.0 and sheep_move_dis > 0.0 and wolf_move_dis > 0.0:
                return float(pos_limit), float(sheep_move_dis), float(wolf_move_dis)
            else:
                raise ValueError
        except Exception:
            raise ValueError("Wrong values in configuration file!")


