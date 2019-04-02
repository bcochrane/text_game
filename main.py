from game_map import Map, Room, Player


def main():
    map1 = Map(x_size=10, y_size=10)
    map1.generate_map()

    # x_min = map1.map_start_coordinates[0] - 2
    # y_min = map1.map_start_coordinates[1] - 2
    # x_max = map1.map_start_coordinates[0] + 2
    # y_max = map1.map_start_coordinates[1] + 2
    x_min = 0
    y_min = 0
    x_max = map1.x_size - 1
    y_max = map1.y_size - 1
    map1.print_map(x_min, y_min, x_max, y_max)

    player = Player(name='Brian', coordinates=map1.map_start_coordinates)

    # game loop
    while True:
        current_room = map1.rooms[player.coordinates]
        print(f'player.coordinates = {player.coordinates}')
        print(f'room.description = "{current_room.description}"')
        print(f'room.doors = "{current_room.doors}"')

        command = input('> ').upper()
        print(f"'{command}'")
        break

if __name__ == '__main__':
    main()
