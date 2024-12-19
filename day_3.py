import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
control_1 = "do()"
control_2 = "don't()"
content = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def get_control_and_position(subs, start=0):
    temp = '('+subs[0]+','+subs[1]+')'
    position = content.find(temp, start)
    control_2_pos = content.rfind(control_2, start, position)
    control_1_pos = content.rfind(control_1, start, position)
    if control_1_pos == control_2_pos == -1:
        return(0, control_1)
    positions = [(control_1_pos, control_1), (control_2_pos, control_2)]
    return max(positions, key=lambda x: x[0])
    


with open("./input/input3.txt") as file:
    content = file.read()

matches = re.findall(pattern, content)

sum = 0
start = 0
for m in matches:
    pos, control = get_control_and_position(m, start)
    start = pos
    if control == control_1:
        x, y = map(int, m)
        sum += x*y
print(sum)
