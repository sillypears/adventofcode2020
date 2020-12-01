import requests, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cookie import cookie

YEAR=2020
DAY=1
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
    answer = ""
    for a in inputs:
        input1 = int(a.strip())
        for b in inputs:
            input2 = int(b.strip())
            if int(input1)+int(input2) == 2020:
                return int(input1)*int(input2)
    return answer

def solve2(inputs):
    answer = ""
    for a in inputs:
        input1 = int(a.strip())
        for b in inputs:
            input2 = int(b.strip())
            for c in inputs:
                input3 = int(c.strip())
                if input1+input2+input3 == 2020:
                    return input1*input2*input3
    return answer

def main():
    data = get_inputs(DAY)
    print(solve1(data))
    print(solve2(data))
    #data = get_test_inputs()

if __name__ == "__main__":
    sys.exit(main())