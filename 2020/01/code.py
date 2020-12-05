import json


def find_numbers(sum, numbers, depth):

    if depth == 2:
        for x in numbers:
            y = sum - x
            if y in numbers:
                return[x, y]
        return []
    else:
        for num in numbers:
            new_sum = sum - num
            new_numbers = numbers.copy()
            new_numbers.remove(num)
            pair = find_numbers(new_sum, new_numbers, depth - 1)
            if any(pair):
                pair.append(num)
                return pair
            else:
                continue
        return []


def main():
    input_file_path = './input.json'
    with open(input_file_path) as input_file:
        values = json.load(input_file)
        print(find_numbers(2020, values, 2))


if __name__ == "__main__":
    main()
