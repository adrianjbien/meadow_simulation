from Sheep import Sheep
from Wolf import Wolf


class SimulationController: # klasa laczaca wszystko i rozpoczynajaca symulacje
    def __init__(self, simulation):
        self.simulation = simulation # do zmiany



if __name__ == '__main__':
    wolf = Wolf(1.0)
    sheep = [Sheep(1, 0.5)]

    print("x owcy: " + str(sheep[0].get_x_cord()) + ", y owcy: " + str(sheep[0].get_y_cord()))

    for i in range(2):
        sheep[0].move()
        wolf.move(sheep)




