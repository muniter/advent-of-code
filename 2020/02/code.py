#!/usr/bin/python3

def get_formatted_data(filename):
    """This function takes the input file name, and 
    returns the data as a list with each item having
    all the neccesarry info to process each password

    minimum, maximum, character, password"""
    data = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            # print(line)
            # line = file.readline().rstrip()
            criteria, password = line.split(': ')
            ranges, character = criteria.split(' ')
            minimum, maximum = ranges.split('-')
            data.append((int(minimum), int(maximum), character, password))
        return data

def check_password_policy_1(passwordset):
    """check if the password matches the criteria"""
    minimum, maximum, character, password = passwordset
    times_in_password = password.count(character)

    if minimum <= times_in_password <= maximum:
        return True
    else:
        return False

def check_password_policy_2(passwordset):
    """check if the password matches the criteria"""
    pos1, pos2, character, password = passwordset
    pos1_criteria = False
    pos2_criteria = False

    # Check the first position
    if pos1 <= len(password) and password[pos1 - 1] == character:
        pos1_criteria = True
    # Check the second position
    if pos2 <= len(password) and password[pos2 - 1] == character:
        pos2_criteria = True
    # Use the bitwise exclusive (XOR)
    return pos1_criteria ^ pos2_criteria


def main():
    total = 0
    policy_1 = 0
    policy_2 = 0
    data = get_formatted_data('input.txt')
    for passwordset in data:
        total += 1
        if check_password_policy_1(passwordset):
            policy_1 += 1
        if check_password_policy_2(passwordset):
            policy_2 += 1
    print(f"The number of passwords that follow the criteria of policy 1 is {policy_1}")
    print(f"The number of passwords that follow the criteria of policy 2 is {policy_2}")
    print(f"The total is {total}")


if __name__ == "__main__":
    main()
