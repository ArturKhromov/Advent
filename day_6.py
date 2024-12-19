from enum import Enum

test_m = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

map = []
old_obst = '#'
new_obst = 'O'

def get_start():
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '^':
                return [i, j]
            
class Orientation(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4

def probe_coordinate(i, j):
        return map[i][j]
    
def is_obstr(i, j):
    return map[i][j] == old_obst or map[i][j] == new_obst

def is_end(i, j):
    return i < 0 or i >= len(map) or j<0 or j >= len(map[i])
            
class Guard:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.orientation = Orientation.TOP
        self.path_count = 1
        self.path = {(i, j) : self.orientation}
        self.is_in_room = True
        self.is_in_loop = False

    def check_loop(self):
        coordinates = (self.i, self.j)
        if coordinates in self.path and self.path[coordinates] == self.orientation:
            self.is_in_loop = True
            return
        else:
            self.is_in_loop = False

    def get_path_count(self):
        return self.path_count
    
    def get_path(self):
        return self.path

    def is_in_room(self):
        return self.is_in_room

    def get_new_coordinates(self):
        match self.orientation:
            case Orientation.TOP:
                return [self.i - 1, self.j]
            case Orientation.BOTTOM:
                return [self.i + 1, self.j]
            case Orientation.RIGHT:
                return [self.i, self.j + 1]
            case Orientation.LEFT:
                return [self.i, self.j - 1]
    
    def turn_right(self):
        orientations = list(Orientation)
        current_index = orientations.index(self.orientation)
        next_index = (current_index + 1) % len(orientations)
        self.orientation = orientations[next_index]
        self.mark_yourself()

    def mark_path(self):
        map[self.i][self.j] = 'X'

    def get_symbol(self):
        match self.orientation:
            case Orientation.TOP:
                return '^'
            case Orientation.BOTTOM:
                return 'v'
            case Orientation.RIGHT:
                return '>'
            case Orientation.LEFT:
                return '<'

    def mark_yourself(self):        
        map[self.i][self.j] = self.get_symbol()

    def increase_path(self):
        if map[self.i][self.j] != 'X':
            self.path_count += 1

    def remember_path(self):
        self.path[(self.i, self.j)] = self.orientation

    def make_move(self, new_coord):
        self.mark_path()
        self.i = new_coord[0]
        self.j = new_coord[1]
        self.check_loop()
        self.increase_path()
        self.remember_path()
        self.mark_yourself()

    def move_forward(self):
        new_coord = self.get_new_coordinates()

        if is_end(new_coord[0], new_coord[1]):
            self.is_in_room = False
            return

        if is_obstr(new_coord[0], new_coord[1]):
            self.turn_right()
            return
        
        self.make_move(new_coord)

def reset_map_test():
    map.clear()
    for line in test_m.split('\n'):
        map.append(list(line))

def reset_map():
    map.clear()
    with open("./input/input_6.txt") as file:
        for line in file:
            map.append(list(line))



reset_map()
start = get_start()
guard = Guard(start[0], start[1])

while guard.is_in_room:
    guard.move_forward()

old_path = guard.get_path()

reset_map()
guard = Guard(start[0], start[1])
new_obstraction_locations = []
for coordinates in old_path:
    if coordinates[0] == start[0] and coordinates[1] == start[1]:
        continue
    if (coordinates[0], coordinates[1]) in new_obstraction_locations:
        continue
    map[coordinates[0]][coordinates[1]] = new_obst
    while guard.is_in_room and not guard.is_in_loop:
        guard.move_forward()
    if guard.is_in_loop:
        new_obstraction_locations.append((coordinates[0], coordinates[1]))
    reset_map()
    guard = Guard(start[0], start[1])

print(len(new_obstraction_locations))