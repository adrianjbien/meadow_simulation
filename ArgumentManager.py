import argparse


class ArgumentManager:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="This script runs a meadow simulation")
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
