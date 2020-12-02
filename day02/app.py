import requests, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cookie import cookie

YEAR=2020
DAY=2

def get_inputs(day):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    r = requests.get(url, cookies=dict(session=cookie))
    if r.status_code == 200: return r.text.splitlines()
    print("Couldn't get inputs, update cookie")
    sys.exit(1)

def get_test_inputs():
    with open('test_input.txt', 'r') as f:
        return f.read().splitlines()

def solve1(inputs):
    answer = False

    policy, p_letter, password = inputs.split()
    p_letter = p_letter.split(":")[0]
    p_min = int(policy.split("-")[0])
    p_max = int(policy.split("-")[1])
    # print(f"{p_min}, {p_max}, {p_letter}, {password}")
    letters = {}
    for letter in password:
        if letter in letters.keys():
            letters[letter] += 1
        else:
            letters[letter] = 1
    if p_letter not in letters.keys(): letters[p_letter] = 0
    # print(f"{letters}, {p_letter}, {password}")
    if p_min <= letters[p_letter] <= p_max:
        answer = True
    else:
        # print(f"{p_min}, {p_max}, {p_letter}, {password}")
        pass

    return answer

def solve2(inputs):
    answer = False
    policy, p_letter, password = inputs.split()
    p_letter = p_letter.split(":")[0]
    pos1 = int(policy.split("-")[0])-1
    pos2 = int(policy.split("-")[1])-1

    if not answer and password[pos1] is p_letter:
        answer = True
    if not answer and password[pos2] is p_letter:
        answer = True
    if password[pos1] is p_letter and password[pos2] is p_letter:
        answer = False
    # print(f"{pos1}, {pos2}, {p_letter}, {password}")

    return answer

def main():
    data = get_inputs(DAY)
    # data = get_test_inputs()
    trues = 0
    for line in data:
        if solve1(line):
            trues += 1
    print(F"part1: {trues}")
    trues = 0
    for line in data:
        if solve2(line):
            trues += 1
    print(F"part2: {trues}")
if __name__ == "__main__":
    sys.exit(main())
