#!/usr/bin/python3

def format_input(filename):
    """Format the input to usable form

    :filename: filename
    :returns: list of list

    """
    with open(filename) as file:
        data = []
        current_group = []
        for line in file:
            line = line.rstrip('\n')
            if line == '':
                data.append(current_group)
                current_group = []
                continue
            else:
                current_group.append(line)
        data.append(current_group)
        return data

def counter_of_answers(group_data):
    """This counts the unique characters in the list of strings

    :group_data: List of strings
    :returns: Unique characters

    """
    unique = set()
    union = ''
    for item in group_data:
        union += item

    for letter in union:
        unique.add(letter)

    # print(len(group_data), len(unique), group_data, unique)
    return len(unique)

def counter_of_answers_yes(group_data):
    """This counts the questions in a group to which everyone
    answered yes

    :group_data: List of strings
    :returns: Unique characters

    """
    counter = 0
    unique = set()
    union = ''
    for item in group_data:
        union += item

    for letter in union:
        unique.add(letter)

    for letter in unique:
        matches = [letter in answer for answer in group_data]
        if all(matches):
            counter += 1

    return counter

def main():
    data = format_input('input.txt')
    print("Number of groups", len(data))
    yes_results = []
    results = []
    total = 0
    for group in data:
        group_result = counter_of_answers(group)
        total += group_result
        results.append(group_result)

        yes_result = counter_of_answers_yes(group)
        yes_results.append(yes_result)

    print("Puzzle 1 the sum of the count is", sum(results))
    print("Puzzle 2 the sum of the count is", sum(yes_results))


if __name__ == "__main__":
    main()
