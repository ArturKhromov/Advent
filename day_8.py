from itertools import combinations

test_input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

data = []
sets = {}

def parse_input(test=True):
    if test:
        for line in test_input.split('\n'):
            if line:
                data.append([c for c in line])
    else:
        with open("./input/input_8.txt") as file:
            for line in file:
                if line:
                    data.append([c for c in line.strip()])

def build_sets():
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '.' or data[i][j] == '\n':
                continue
            if data[i][j] not in sets:
                sets[data[i][j]] = {
                    "coordinates": [(i, j)]
                }
            else:
                sets[data[i][j]]["coordinates"].append((i, j))

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x2 - x1, y2 - y1)

def is_valid_and_within_bounds(a1, p1, p2):
    if a1[0] >= 0 and a1[1] >= 0:
        if a1[0] < len(data) and a1[1] < len(data[0]):
            if min(p1[0], p2[0]) <= a1[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= a1[1] <= max(p1[1], p2[1]):
                return False
            else:
                return True
    return False


def get_coordinates_for_ant(p1, p2):
    ret = set()
    dist1 = calculate_distance(p1, p2)
    dist2 = calculate_distance(p2, p1)
    a1 = (p2[0] + dist1[0], p2[1] + dist1[1])
    while is_valid_and_within_bounds(a1, p1, p2):
        ret.add(a1)
        a1 = (a1[0] + dist1[0], a1[1] + dist1[1])   
    a4 = (p2[0] - dist2[0], p2[1] - dist2[1])
    while is_valid_and_within_bounds(a4, p1, p2):
        ret.add(a4)
        a4 = (a4[0] - dist2[0], a4[1] - dist2[1])
    a2 = (p1[0] - dist1[0], p1[1] - dist1[1])
    while is_valid_and_within_bounds(a2, p1, p2):
        ret.add(a2)
        a2 = (a2[0] - dist1[0], a2[1] - dist1[1])
    a3 = (p1[0] + dist2[0], p1[1] + dist2[1])
    while is_valid_and_within_bounds(a3, p1, p2):
        ret.add(a3)
        a3 = (a3[0] + dist2[0], a3[1] + dist2[1])
    return ret

parse_input(False)
build_sets()

sum = 0
for letter in sets:
    coordinates = sets[letter]["coordinates"]
    sets[letter]["antidots"] = set()
    unique_combinations = list(combinations(coordinates, 2))
    for comb in unique_combinations:
        ants = get_coordinates_for_ant(comb[0], comb[1])
        for ant in ants:
            sets[letter]["antidots"].add(ant)
            if data[ant[0]][ant[1]] == '.':
                data[ant[0]][ant[1]] = '#'

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != '.':
            sum += 1
print(sum)

