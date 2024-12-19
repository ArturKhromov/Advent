array_2d = []
array_2d_new = []

test_c = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

word = "XMAS"
word2 = "MAS"
LENGTH = len(word)
LENGTH2 = 2

def get_right(i, j):
    if j + LENGTH < len(array_2d[i]):
        str = [array_2d[i][j + k] for k in range(LENGTH)]
        return ''.join(str)
    else:
        return ""
    
def get_left(i, j):
    if j - LENGTH < -1:
        return ""
    else:
        str = [array_2d[i][j - k] for k in range(LENGTH)]
        return ''.join(str)
    
    
def get_bottom(i, j):
    if i + LENGTH > len(array_2d):
        return ""
    else:
        str = [array_2d[i + k][j] for k in range(LENGTH)]
        return  ''.join(str)

def get_top(i,j):
    if i - LENGTH < -1:
        return ""
    else:
        str = [array_2d[i - k][j] for k in range(LENGTH)]
        return  ''.join(str)

def get_left_top(i,j):
    if i-LENGTH<-1 or j-LENGTH<-1:
        return ""
    else:
        diagonal = [array_2d[i - k][j - k] for k in range(LENGTH)]
        return ''.join(diagonal)
    
def get_left_top2(i,j):
    if i-LENGTH2<-1 or j-LENGTH2<-1:
        return ""
    elif i+LENGTH2 > len(array_2d) or j+LENGTH2>len(array_2d[i]):
        return ""
    else:
        diagonal = [array_2d[i - k][j - k] for k in range(1, -2, -1)]
        return ''.join(diagonal)

def get_right_top(i, j):
    if j+LENGTH > len(array_2d[i]) or i - LENGTH < -1:
        return ""
    else:
        diagonal = [array_2d[i - k][j + k] for k in range(LENGTH)]
        return ''.join(diagonal)
    
def get_right_top2(i,j):
    if i-LENGTH2<-1 or j+LENGTH2>len(array_2d[i]):
        return ""
    elif i+LENGTH2 > len(array_2d) or j-LENGTH2<-1:
        return ""
    else:
        diagonal = [array_2d[i - k][j + k] for k in range(1, -2, -1)]
        return ''.join(diagonal)
    
def get_left_bottom(i, j):
    if i + LENGTH > len(array_2d) or j - LENGTH < -1 :
        return ""
    else:
        diagonal = [array_2d[i + k][j - k] for k in range(LENGTH)]
        return  ''.join(diagonal)

def get_left_bottom2(i, j):
    if i + LENGTH2 > len(array_2d) or j - LENGTH2 < -1 :
        return ""
    else:
        diagonal = [array_2d[i + k][j - k] for k in range(LENGTH2)]
        return  ''.join(diagonal)
        
def get_right_bottom(i, j):
    if i + LENGTH > len(array_2d) or j+LENGTH > len(array_2d[i]):
        return ""
    else:
        diagonal = [array_2d[i + k][j + k] for k in range(LENGTH)]
        return ''.join(diagonal)
    
def get_right_bottom2(i, j):
    if i + LENGTH2 > len(array_2d) or j+LENGTH2 > len(array_2d[i]):
        return ""
    else:
        diagonal = [array_2d[i + k][j + k] for k in range(LENGTH2)]
        return ''.join(diagonal)

def check_string(str):
    return str == word2

def check_string2(str):
    return str == word2

def check_position(i, j):
    sum = 0
    right = get_right(i, j)
    if check_string(right):
        sum += 1
        for idx, letter in enumerate(word2):
            array_2d_new[i][j + idx] = letter
    left = get_left(i, j)
    if check_string(left):
        sum += 1
        for idx, letter in enumerate(word2):
            array_2d_new[i][j - idx] = letter
    top = get_top(i,j)
    if check_string(top):
        sum += 1
        for idx, letter in enumerate(word2):
            array_2d_new[i-idx][j] = letter
    bottom = get_bottom(i, j)
    if check_string(bottom):
        sum += 1
        for idx, letter in enumerate(word2):
            array_2d_new[i+idx][j] = letter
    left_top = get_left_top(i, j)
    if check_string(left_top):
        sum += 1
        for idx, letter in enumerate(word2):
            array_2d_new[i-idx][j - idx] = letter
    right_top = get_right_top(i, j)
    if check_string(right_top):
        sum += 1
        for idx, letter in enumerate(word2):
            array_2d_new[i-idx][j + idx] = letter
    left_bottom = get_left_bottom(i, j)
    if check_string(left_bottom):
        sum += 1
        for idx, letter in enumerate(word2):
            array_2d_new[i+idx][j - idx] = letter
    right_bottom = get_right_bottom(i, j)
    if check_string(right_bottom):
        sum += 1
        for idx, letter in enumerate(word2):
            array_2d_new[i+idx][j + idx] = letter
    return sum

def check_position2(i, j):
    sum = 0    
    left_top = get_left_top2(i, j)   
    right_top = get_right_top2(i, j)      
    if (left_top == "MAS" or left_top == "SAM") and (right_top == "MAS" or right_top == "SAM"):
        return 1
    else:
        return 0


# rows = test_c.strip().split('\n')
# for row in rows:
#     array_2d.append(list(row))
#     array_2d_new.append(['.' for _ in range(len(row))] )

with open("./input/input_4.txt") as file:
    for line in file:
        array_2d.append(list(line))
        array_2d_new.append(['.' for _ in range(len(line))] )

# for i in range(len(array_2d)):
#     for j in range(len(array_2d[i])):
#         array_2d_new[i][j] = '.'

sum = 0
for i in range(len(array_2d)):
    if i == 0:
        continue
    for j in range(len(array_2d[i])):
        if j==0:
            continue
        if array_2d[i][j] == 'A':
            sum += check_position2(i, j)
print(sum)
# for r in array_2d_new:
#     print(r)


