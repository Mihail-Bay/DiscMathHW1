def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    n = int(lines[0].strip())
    sets = []
    for i in range(1, n + 1):
        current_set = set(map(int, lines[i].strip().split()))
        sets.append(current_set)
    return sets


def find_intersection(sets):
    if not sets:
        return set()

    intersection = set()

    for element in sets[0]:

        found_in_all = True

        for s in sets[1:]:
            if element not in s:
                found_in_all = False
                break

        if found_in_all:
            intersection.add(element)

    return intersection

def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(sorted(result)))


def main():
    sets = read_input('../txtf/input.txt')

    intersection = find_intersection(sets)

    write_output('../txtf/output.txt', intersection)


if __name__ == "__main__":
    main()