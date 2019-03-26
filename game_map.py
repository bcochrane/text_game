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

        current_room_coords = self.map_start_coords
        self.rooms[current_room_coords] = Room(exits=self.get_random_exits(min_exits=1, max_exits=3))

        current_room = self.rooms[current_room_coords]
        for exit in current_room.exits:
            adjacent_room_coords = self.get_adjacent_room_coords(current_room_coords, exit)
            try:
                adjacent_room = self.rooms[adjacent_room_coords]
            except KeyError:
                self.rooms[adjacent_room_coords] = Room(exits=self.get_random_exits(min_exits=2, max_exits=3))
                adjacent_room = self.rooms[adjacent_room_coords]
                opposing_exit = self.get_opposing_exit(exit)
                if not opposing_exit in adjacent_room.exits:
                    adjacent_room.create_exit(opposing_exit)

    def sum_coords(self, coords1: tuple, coords2: tuple):
        return (coords1[0] + coords2[0], coords1[1] + coords2[1])

    def get_random_exits(self, min_exits: int=1, max_exits: int = 4):
        return random.sample(('N', 'E', 'S', 'W'), k=random.randrange(min_exits, max_exits + 1))

    def get_adjacent_room_coords(self, current_room_coords: tuple, exit_direction: str):
        if exit_direction == 'N':
            return self.sum_coords(current_room_coords, (0, -1))
        elif exit_direction == 'E':
            return self.sum_coords(current_room_coords, (1, 0))
        elif exit_direction == 'S':
            return self.sum_coords(current_room_coords, (0, 1))
        elif exit_direction == 'W':
            return self.sum_coords(current_room_coords, (-1, 0))
        else:
            return None

    def get_opposing_exit(self, exit_direction):
        if exit_direction == 'N':
            return 'S'
        elif exit_direction == 'E':
            return 'W'
        elif exit_direction == 'S':
            return 'N'
        elif exit_direction == 'W':
            return 'E'
        else:
            return None

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
                            f'+--{n}--+',
                            f'|      |',
                            f'{w}      {e}',
                            f'|      |',
                            f'+--{s}--+'
                        ]
                except KeyError:
                    room_text = [
                        '        ',
                        '        ',
                        '        ',
                        '        ',
                        '        ',
                    ]
                for i, line in enumerate(room_text):
                    map_text_row[i] += line

            map_text_rows.extend(map_text_row)

        for row in map_text_rows:
            print(row)


class Room:
    def __init__(self, exits: list, desc: str = ''):
        self.exits = exits
        self.desc = desc

    def create_exit(self, exit: str):
        if exit not in self.exits:
            self.exits.append(exit)

    def delete_exit(self, exit):
        if exit in self.exits:
            self.exits.remove(exit)
