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
        coordinates: tuple, door_direction: str):
    if door_direction == 'N':
        return sum_coordinates(coordinates, (0, -1))
    elif door_direction == 'E':
        return sum_coordinates(coordinates, (1, 0))
    elif door_direction == 'S':
        return sum_coordinates(coordinates, (0, 1))
    elif door_direction == 'W':
        return sum_coordinates(coordinates, (-1, 0))
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
        self.room_stack = [self.map_start_coordinates]
        self.current_coordinates = None

        # Map data is stored in a dictionary. The keys are 2-element
        # tuples representing (x, y) coordinates, and the values are
        # Room objects.
        self.rooms = {}

    def generate_map(self):
        # TODO: Add min and max room parameters

        while len(self.room_stack) > 0:
            self.add_room()

    def add_room(self):
        # Pop coordinates off room stack.
        self.current_coordinates = self.room_stack.pop()

        # Create a room with random doors and add it to the map.
        doors = generate_random_doors(min_doors=1, max_doors=3)
        self.rooms[self.current_coordinates] = Room(doors)
        current_room = self.rooms[self.current_coordinates]

        # If the room borders a map edge, remove doors on that side.
        #
        # CAUTION: If the first room is created on a map edge or corner
        # and its only exit(s) face(s) the edge, the room will end up
        # with zero doors after this step, and map generation will stop
        for door_to_remove in self.find_exits_at_map_edge(
                self.current_coordinates):
            current_room.remove_door(door_to_remove)

        directions_possible = ['N', 'E', 'S', 'W']
        random.shuffle(directions_possible)
        for direction in directions_possible:
            current_door = direction
            coordinates = get_adjacent_room_coordinates(self.current_coordinates, direction)
            if self.validate_coordinates(coordinates):
                if self.check_if_room_exists(coordinates):
                    adjacent_room = self.rooms[(coordinates)]
                    opposing_door = get_opposing_door(current_door)

                    # remove door from current room if no matching door in adjacent room
                    if current_door in current_room.doors and opposing_door not in adjacent_room.doors:
                        current_room.remove_door(current_door)

                    # add door to current room if matching door in adjacent room
                    elif current_door not in current_room.doors and opposing_door in adjacent_room.doors:
                        current_room.add_door(current_door)
                else:
                    if current_door in current_room.doors:
                        self.room_stack.append(coordinates)

    def find_exits_at_map_edge(self, coordinates: tuple):
        x, y = coordinates
        exits_at_map_edge = []

        if x == 0:
            exits_at_map_edge.append('W')
        elif x == self.x_size - 1:
            exits_at_map_edge.append('E')

        if y == 0:
            exits_at_map_edge.append('N')
        elif y == self.y_size - 1:
            exits_at_map_edge.append('S')

        return exits_at_map_edge

    def validate_coordinates(self, coordinates: tuple):
        x, y = coordinates
        if x >= 0 and x < self.x_size and y >= 0 and y < self.y_size:
            return True
        else:
            return False

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
                    n = '      ' if 'N' in current_room.doors else '------'
                    e = ' ' if 'E' in current_room.doors else '|'
                    s = '      ' if 'S' in current_room.doors else '------'
                    w = ' ' if 'W' in current_room.doors else '|'
                    room_text = [
                        f'+{n}+',
                        f'{w}      {e}',
                        f'{w}      {e}',
                        f'{w}      {e}',
                        f'+{s}+'
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
    def __init__(self, doors: list, description: str = ''):
        self.doors = doors
        self.description = description

    def add_door(self, door: str):
        if door not in self.doors:
            self.doors.append(door)

    def remove_door(self, door):
        if door in self.doors:
            self.doors.remove(door)


class Entity:
    def __init__(self, name: str, coordinates: tuple):
        self.name = name
        self.coordinates = coordinates


class Player(Entity):
    pass
