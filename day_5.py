test_rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

test_seq = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules = []
commands = []

def parse_rules(str):
    rules.append(list(map(int, str.split('|'))))

def check_line(numbers):
    forbidden = set()
    for n in numbers:
        if n in forbidden:
            return False
        filtered_first_elements = [row[0] for row in rules if row[1] == n]
        for item in filtered_first_elements:
            forbidden.add(item)
    return True

def organize(numbers):
    forbidden = {}
    i=0
    while i < len(numbers):
        if numbers[i] in forbidden:
            t = forbidden[numbers[i]]
            numbers[i], numbers[t] = numbers[t], numbers[i]
            forbidden = {}
            i = 0
        else:
            filtered_first_elements = [row[0] for row in rules if row[1] == numbers[i]]           
            for item in filtered_first_elements:
                forbidden[item] = i
            i+=1


# for line in test_rules.split('\n'):
#     parse_rules(line)

# for line in test_seq.split('\n'):
#     commands.append(list(map(int, line.split(','))))

with open("./input/input_5.txt") as file:
    for line in file:
        if '|' in line:
            parse_rules(line)
        elif ',' in line:
            commands.append(list(map(int, line.split(','))))   
        else:
            continue

sum = 0
for command in commands:
        if not check_line(command):
            organize(command)
            middle_index = len(command) // 2
            sum += command[middle_index]    
print(sum)


