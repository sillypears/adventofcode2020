import requests, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cookie import cookie

YEAR=2020
DAY=

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

    return answer

def solve2(inputs):
    answer = ""

    return answer

def main():
    #data = get_test_inputs()
    data = get_inputs(DAY)

    print(solve1(data))
    print(solve2(data))

if __name__ == "__main__":
    sys.exit(main())
