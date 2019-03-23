import random


class Map:
    def __init__(self, x_size: int = 10, y_size: int = 10):
        self.x_size = x_size
        self.y_size = y_size

    def print_map(self):
        pass


class Room:
    def __init__(self, x_coord: int, y_coord: int, exits: list, description: str = ''):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.exits = exits
        self.description = description

    def print_room(self):
        n = '  ' if 'N' in self.exits else '--'
        e = ' ' if 'E' in self.exits else '|'
        s = '  ' if 'S' in self.exits else '--'
        w = ' ' if 'W' in self.exits else '|'

        room_string = f' ----{n}---- \n|          |\n{w}          {e}\n|          |\n ----{s}---- '
        print(room_string)


def main():
    generate_map()
    # display map
    pass


def generate_map():
    # create a room
    # randomly create exits; disallow creation of exit if adjacent room exists and does't have a matching exit
    # create room adjacent to exits if one does not already exist

    exits = random.sample(('N', 'E', 'S', 'W'), k=random.randrange(1, 5))
    room = Room(0, 0, exits)
    room.print_room()


if __name__ == '__main__':
    main()
