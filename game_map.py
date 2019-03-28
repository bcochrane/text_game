import random


def sum_coordinates(coordinates1: tuple, coordinates2: tuple):
    x = coordinates1[0] + coordinates2[0]
    y = coordinates1[1] + coordinates2[1]
    return (x, y)


def generate_random_doors(min_doors: int = 1, max_doors: int = 4):
    return random.sample(
        ('N', 'E', 'S', 'W'),
        k=random.randrange(min_doors, max_doors + 1))


def get_adjacent_room_coordinates(
        current_room_coordinates: tuple, door_direction: str):
    if door_direction == 'N':
        return sum_coordinates(current_room_coordinates, (0, -1))
    elif door_direction == 'E':
        return sum_coordinates(current_room_coordinates, (1, 0))
    elif door_direction == 'S':
        return sum_coordinates(current_room_coordinates, (0, 1))
    elif door_direction == 'W':
        return sum_coordinates(current_room_coordinates, (-1, 0))
    else:
        return None


def get_opposing_door(door_direction):
    if door_direction == 'N':
        return 'S'
    elif door_direction == 'E':
        return 'W'
    elif door_direction == 'S':
        return 'N'
    elif door_direction == 'W':
        return 'E'
    else:
        return None


class Map:
    def __init__(self, x_size: int = 10, y_size: int = 10):
        self.x_size = x_size
        self.y_size = y_size

        # find the center of the map
        self.map_start_coordinates = (
            int(self.x_size / 2), int(self.y_size / 2))

        # Map data is stored in a dictionary. The keys are 2-element
        # tuples representing (x, y) coordinates, and the values are
        # Room objects.
        self.rooms = {}

    def generate_map(self):
        # 1. Create a room.
        # 2. Create random doors in the current room.
        # 3. Check for rooms adjacent to the current room.
        # 4. If adjacent rooms don't have matching doors, remove the
        #    corresponding doors from the current room.
        # 5. If the adjacent rooms have doors facing the current room,
        #    and the current room doesn't have matching doors, add
        #    matching doors to the current room.
        # 6. Check for rooms adjacent to current room's doors. If they
        #    don't exist, add coordinates to stack.

        current_room_coordinates = self.map_start_coordinates
        doors = generate_random_doors(min_doors=1, max_doors=3)
        self.rooms[current_room_coordinates] = Room(doors)
        current_room = self.rooms[current_room_coordinates]
        for door in current_room.doors:
            adjacent_room_coordinates = get_adjacent_room_coordinates(
                current_room_coordinates, door)
            if self.check_if_room_exists(adjacent_room_coordinates):
                adjacent_room = self.rooms[adjacent_room_coordinates]
            else:
                self.rooms[adjacent_room_coordinates] = Room(
                    doors=generate_random_doors(min_doors=2, max_doors=3))
                adjacent_room = self.rooms[adjacent_room_coordinates]
                opposing_door = get_opposing_door(door)
                if opposing_door not in adjacent_room.doors:
                    adjacent_room.create_door(opposing_door)

    def check_if_room_exists(self, coordinates: tuple):
        try:
            if self.rooms[coordinates]:
                return True
        except KeyError:
            return False

    def print_map(self, x_min: int, y_min: int, x_max: int, y_max: int):
        map_text_rows = []
        for y in range(y_min, y_max + 1):
            map_text_row = ['', '', '', '', '']
            for x in range(x_min, x_max + 1):
                current_coordinates = (x, y)
                if self.check_if_room_exists(current_coordinates):
                    current_room = self.rooms[current_coordinates]
                    n = '  ' if 'N' in current_room.doors else '--'
                    e = ' ' if 'E' in current_room.doors else '|'
                    s = '  ' if 'S' in current_room.doors else '--'
                    w = ' ' if 'W' in current_room.doors else '|'
                    room_text = [
                        f'+--{n}--+',
                        f'|      |',
                        f'{w}      {e}',
                        f'|      |',
                        f'+--{s}--+'
                    ]
                else:
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
    def __init__(self, doors: list, desc: str = ''):
        self.doors = doors
        self.desc = desc

    def create_door(self, door: str):
        if door not in self.doors:
            self.doors.append(door)

    def delete_door(self, door):
        if door in self.doors:
            self.doors.remove(door)
