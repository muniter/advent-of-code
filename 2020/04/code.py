#!/usr/bin/python3

def check_hht(value):
    unit = value[-2:]
    hgt = int(value[:-2])
    if len(value) < 4:
        return False
    if unit == 'cm':
        return 150 <= hgt <= 193
    if unit == 'in':
        return 59 <= hgt <= 76


def check_hcl(value):
    integer = False
    if value[0] == '#':
        if len(value) == 7:
            try:
                integer = int(value[1:], 16)
                return True
            except Exception as e:
                return False


def check_pid(value):
    if len(value) == 9:
        try:
            int(value)
            return True
        except Exception as e:
            return False


def format_input(filename):
    """format the input from the puzzle"""
    with open(filename) as file:
        counter = 0
        data = {}
        raw_data = file.readlines()
        for line in raw_data:
            # Remove new line character \n
            line = line.rstrip()
            # Empty string item means it's a new item.
            if line == '':
                counter += 1
                continue

            fields = line.split(' ')
            fields = map(lambda x: x.split(':'), fields)
            fields = {item[0]: item[1] for item in fields}
            curr_scan = data.get(counter, {})
            curr_scan.update(fields)
            data[counter] = curr_scan

        return data


def check_policy_1(data):
    """Check the policy 1 against the scanned data

    :data: scanned data
    :returns: True/False if it passes or fails.
    """
    REQUIRED_FIELDS = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid']

    for field in REQUIRED_FIELDS:
        if field not in data:
            return False
    return True


def check_policy_2(data):
    """Check the policy 1 against the scanned data

    :data: scanned data
    :returns: True/False if it passes or fails.
    """
    POLICY = {
        'byr': [lambda x: 1920 <= int(x) <= 2002, True],
        'iyr': [lambda x: 2010 <= int(x) <= 2020, True],
        'eyr': [lambda x: 2020 <= int(x) <= 2030, True],
        'hgt': [check_hht, True],
        'hcl': [check_hcl, True],
        'ecl': [lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], True],
        'pid': [check_pid, True]}

    for key, policy in POLICY.items():
        checker_function = policy[0]
        required = policy[1]
        if required and key not in data:
            return False
        if not checker_function(data[key]):
            return False

    return True


def main():
    data = format_input('input.txt')

    counter1 = 0
    counter2 = 0
    for id, scan in data.items():
        if check_policy_1(scan):
            counter1 += 1
        if check_policy_2(scan):
            counter2 += 1

    print("Part 1, number of valid passports is", counter1)
    print("Part 2, number of valid passports is", counter2)


if __name__ == "__main__":
    main()
