import random


class Map:
    def __init__(self, x_size: int = 10, y_size: int = 10):
        self.x_size = x_size
        self.y_size = y_size

        self.map_start_coords = (int(self.x_size / 2), int(self.y_size / 2))
        self.rooms = {}

    def generate_map(self):
        # create a room
        # randomly create exits; disallow creation of exit if adjacent room exists and does't have a matching exit
        # create room adjacent to exits if one does not already exist

        # room.print_room()

        self.rooms[self.map_start_coords] = Room(desc='first room')
        # self.rooms[(5, 5)].print_room()



    def print_map(self):
        pass


class Room:
    def __init__(self, exits: list = [], desc: str = ''):
        self.exits = exits
        self.desc = desc

        if not self.exits:
            self.exits = random.sample(('N', 'E', 'S', 'W'), k=random.randrange(1, 5))

    def print_room(self):
        n = '  ' if 'N' in self.exits else '--'
        e = ' ' if 'E' in self.exits else '|'
        s = '  ' if 'S' in self.exits else '--'
        w = ' ' if 'W' in self.exits else '|'

        room_string = f' ----{n}---- \n|          |\n{w}          {e}\n|          |\n ----{s}---- '
        print(room_string)


def main():
    map1 = Map()
    map1.generate_map()

    # display map
    pass


if __name__ == '__main__':
    main()
