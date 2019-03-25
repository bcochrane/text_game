import random
from collections import defaultdict

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

        current_room_coords = self.map_start_coords
        self.rooms[current_room_coords] = Room(desc='first room')
        # self.rooms[(7, 4)] = Room(desc='second room')

    def print_map(self, x_min: int, y_min: int, x_max: int, y_max: int):
        map_text_rows = []
        for y in range(y_min, y_max + 1):
            map_text_row = ['', '', '', '', '']
            for x in range(x_min, x_max + 1):
                current_coords = (x, y)
                try:
                    if self.rooms[current_coords]:
                        current_room = self.rooms[current_coords]
                        n = '  ' if 'N' in current_room.exits else '--'
                        e = ' ' if 'E' in current_room.exits else '|'
                        s = '  ' if 'S' in current_room.exits else '--'
                        w = ' ' if 'W' in current_room.exits else '|'
                        room_text = [
                            f'+----{n}----+',
                            f'|          |',
                            f'{w}          {e}',
                            f'|          |',
                            f'+----{s}----+'
                        ]
                except KeyError:
                    room_text = [
                        '            ',
                        '            ',
                        '            ',
                        '            ',
                        '            ',
                    ]
                for i, line in enumerate(room_text):
                    map_text_row[i] += line

            map_text_rows.extend(map_text_row)

        for row in map_text_rows:
            print(row)


class Room:
    def __init__(self, exits: list = [], desc: str = ''):
        self.exits = exits
        self.desc = desc

        if not self.exits:
            self.exits = random.sample(('N', 'E', 'S', 'W'), k=random.randrange(1, 5))


def main():
    map1 = Map()
    map1.generate_map()

    x_min = map1.map_start_coords[0] - 2
    y_min = map1.map_start_coords[1] - 2
    x_max = map1.map_start_coords[0] + 2
    y_max = map1.map_start_coords[1] + 2
    map1.print_map(x_min, y_min, x_max, y_max)


if __name__ == '__main__':
    main()
