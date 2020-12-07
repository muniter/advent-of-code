#!/usr/bin/python3

def format_input(filename):
    """format the data to be used"""
    with open(filename) as file:
        data = []
        for line in file:
            line = line.rstrip()
            data.append(line)
    return data


def counter(map: list, item, starting_position: tuple, slope: tuple):
    """This function does the counting"""
    loop = 0
    counter = 0
    xstart, ystart = starting_position
    x = xstart
    y = ystart
    xslope, yslope = slope
    yend = len(map)
    while y <= yend:
        loop += 1
        x += xslope
        y += yslope
        value = locator(map, x, y)
        if slope == (5, 1):
            print(x, y, value)
        if value == item:
            counter += 1

    # print(f'last position {x, y} with {loop} loops')
    return counter


def locator(map, x, y):
    """Locates what's in the x, y position given a map

    :map: list of strings, each item is a row,
    each character of the string is a column
    :x: x position.
    :y: y position.
    :returns: The character in x,y

    """
    ymax = len(map) - 1
    xmax = len(map[0])  # Given a rectangular map
    column = x % xmax
    row = y if y < ymax else ymax
    value = map[row][column]
    return value


def main():
    map = format_input('input.txt')
    totals = []
    product = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        hits = counter(map, '#', (0, 0), slope)
        totals.append(hits)
        print(f'For slope {slope} total hits {hits}')

    for i in totals:
        product = product * i

    print(f'The product of the hits of all different slopes is {product}')


if __name__ == "__main__":
    main()
