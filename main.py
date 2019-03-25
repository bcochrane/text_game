from game_map import Map


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
