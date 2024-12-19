from itertools import product

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

signs = ['+', '*', "||"]
numbers = []
result = []

def parse_numbers_test():
    for line in test_input.split('\n'):
        t = line.split(':')
        right = t[1].strip()
        left = t[0].strip()
        numbers.append([int(num) for num in right.split(' ')])
        result.append(int(left))

def parse_numbers():
     with open("./input/input_7.txt") as file:
        for line in file:
            t = line.split(':')
            right = t[1].strip()
            left = t[0].strip()
            numbers.append([int(num) for num in right.split(' ')])
            result.append(int(left))

def do_math(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '*':
        return a * b
    elif operator == "||":
        return int(str(a) + str(b))
    else:
        return 0

#parse_numbers_test()
parse_numbers()
success = []
for line in zip(result, numbers, range(len(numbers))):
    sign_combinations = list(('+',) + p for p in product(signs, repeat=len(line[1])-1))
    for possibility in sign_combinations:
        ret = 0        
        for idx in range(len(possibility)):
            ret = do_math(possibility[idx], ret, line[1][idx])
        if ret == line[0]:
            success.append({
                "result": line[0],
                "combination": possibility,
                "numbers" : line[1],
                "id": line[2]
            })
sum = 0
seen_ids = set()
unique_data = []

for line in success:
    if line["id"] not in seen_ids:
        #unique_data.append(line)
        seen_ids.add(line["id"])
        sum += line["result"]
print(sum)

        


