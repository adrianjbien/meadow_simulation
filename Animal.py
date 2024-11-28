from Position import Position

class Animal(Position):
    def __init__(self, init_x, init_y, step_length):
        super().__init__(init_x, init_y)
        self.step_length = step_length

    def move(self):
        raise NotImplementedError