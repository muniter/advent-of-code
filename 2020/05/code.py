#!/usr/bin/python3

def format_input(filename):
    """Format the input to process

    :filename: The filename
    :returns: List of items.
    """
    with open(filename) as file:
        data = []
        for line in file:
            data.append(line.rstrip('\n'))
        return data


def decoder(lower, upper, range: tuple, code):
    """decode the number by splitting in halves

    :lower: Character that represents lower
    :upper: Character that represents upper
    :range: Range to start splitting (0, 249)
    :code: string to decode.
    :returns: decoded number.
    """
    left, right = range
    for letter in code:
        distance = (right - left) // 2
        if letter == lower:
            right = right - (distance + 1)
        elif letter == upper:
            left = left + (distance + 1)
        # print(code, left, right)
    return left


def main():
    data = format_input('input.txt')
    result = []
    max_id = 0
    for code in data:
        row = decoder('F', 'B', (0, 127), code[:-3])
        column = decoder('L', 'R', (0, 7), code[-3:])
        id = row * 8 + column
        result.append((row, column, id))
        if id > max_id:
            max_id = id
    print("Puzzle 1 max id is", max_id)

    result.sort(key=lambda x: x[2])
    results_ids = [item[2] for item in result]
    min_id = results_ids[0]
    max_id = results_ids[-1]
    for id in range(min_id, max_id + 1):
        if id not in results_ids:
            print("Puzzle 2 missing id is", id)


if __name__ == "__main__":
    main()
