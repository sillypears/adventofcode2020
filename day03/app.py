import requests, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cookie import cookie

import math
from pprint import pprint

YEAR=2020
DAY=3

def get_inputs(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    r = requests.get(url, cookies=dict(session=cookie))
    if r.status_code == 200: return r.text.splitlines()
    print("Couldn't get inputs, update cookie")
    sys.exit(1)

def get_test_inputs():
    with open('test_input.txt', 'r') as f:
        return f.read().splitlines()

def convert_matrix(data, left):
    repeats = len(data)
    line_len = len(data[0])
    add = math.floor(repeats/left)
    # print(f"{repeats} {line_len} {add} {left}")
    matrix = []
    for line in data:
        # print(line)
        row = []
        for x in range(add):
            for d in line:
                row.append(d)
        # print(row)
    
        matrix.append(row)
    # for x in matrix:
        # print(x)
    return matrix

def solve1(inputs, checks):
    answer = 0
    for c in checks:
        left = c[0]
        down = c[1]
        matrix = convert_matrix(inputs, down)
        for x in range(len(matrix)-1):
            if matrix[down][left] == '#':
                # print(f"hit: {left},{down} {matrix[down][left]}")
                matrix[down][left] = "X"
                answer += 1
            else:
                matrix[down][left] = "O"
            
            left += c[0]
            down += c[1]
        # for x in matrix:
        #     print(x)
    return answer

def solve2(inputs, checks):
    answers = []
    for c in checks:
        answer = 0
        left = c[0]
        down = c[1]
        matrix = convert_matrix(inputs, down)
        for x in range(len(matrix)-1):
            try:
                if matrix[down][left] == '#':
                    # print(f"hit: {left},{down} {matrix[down][left]}")
                    matrix[down][left] = "X"
                    answer += 1
                else:
                    matrix[down][left] = "O"
                
                left += c[0]
                down += c[1]
            except:
                pass
        answers.append(answer)
        # for x in matrix:
        #     print(x)
    
    return math.prod(answers)

def main():
    data = get_test_inputs()
    data = get_inputs(DAY)
    # checks = [[3,1]]
    checks = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    print(f"1: {solve1(data, [[3,1]])}")
    print(f"2: {solve2(data, checks)}")

if __name__ == "__main__":
    sys.exit(main())
