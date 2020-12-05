
import requests, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cookie import cookie
import math

YEAR=2020
DAY=5

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
    answer = []
    max = 0
    rows = {}

    for seat in inputs:
        if len(seat) >= 7:

            fb = seat[0:7:]
            lr = seat[7::]
            # print(f"row: {fb} column: {lr}")
            rowl = 0
            rowm = 127
            row = 0
            for r in fb:
                if r.lower() == "f":
                    rowm -= int(round((rowm-rowl)/2))
                else:
                    rowl += int(round((rowm-rowl)/2))
            if r.lower() == "f":
                row = rowm-1
            else:
                row += rowl+1
            # print(f"{row}")

            coll = 0
            colm = 7
            col = 0
            for c in lr:
                if c.lower() == "l":
                    colm -= int(round((colm-coll)/2))
                else:
                    coll += int(round((colm-coll)/2))
                # print(f"{coll} -> {colm}")
            if c.lower() == "l":
                col = colm-1
            else:
                col += coll+1
            # print(f"{col}")
            id = row * 8 + col
            if row in rows.keys():
                rows[str(row)].append(str(col))
            else:
                rows[str(row)] = [col]
            # print(f"row: {row}, col: {col}, id: {id}")
            if id > max: max = id
            answer.append(id)

    return max

def solve2(inputs):
    answer = []
    max = 0
    rows = {}

    for seat in inputs:
        if len(seat) >= 7:

            fb = seat[0:7:]
            lr = seat[7::]
            # print(f"row: {fb} column: {lr}")
            rowl = 0
            rowm = 127
            row = 0
            for r in fb:
                if r.lower() == "f":
                    rowm -= int(round((rowm-rowl)/2))
                else:
                    rowl += int(round((rowm-rowl)/2))
            if r.lower() == "f":
                row = rowm-1
            else:
                row += rowl+1
            # print(f"{row}")

            coll = 0
            colm = 7
            col = 0
            for c in lr:
                if c.lower() == "l":
                    colm -= int(round((colm-coll)/2))
                else:
                    coll += int(round((colm-coll)/2))
                # print(f"{coll} -> {colm}")
            if c.lower() == "l":
                col = colm-1
            else:
                col += coll+1
            # print(f"{col}")
            id = row * 8 + col
            if row in rows.keys():
                rows[str(row)].append(str(col))
            else:
                rows[str(row)] = [col]
            # print(f"row: {row}, col: {col}, id: {id}")
            if id > max: max = id
            answer.append(id)
    answer = []
    max = 0
    rows = {}

    for seat in inputs:
        if len(seat) >= 7:

            fb = seat[0:7:]
            lr = seat[7::]
            # print(f"row: {fb} column: {lr}")
            rowl = 0
            rowm = 127
            row = 0
            for r in fb:
                if r.lower() == "f":
                    rowm -= int(round((rowm-rowl)/2))
                else:
                    rowl += int(round((rowm-rowl)/2))
            if r.lower() == "f":
                row = rowm-1
            else:
                row += rowl+1
            # print(f"{row}")

            coll = 0
            colm = 7
            col = 0
            for c in lr:
                if c.lower() == "l":
                    colm -= int(round((colm-coll)/2))
                else:
                    coll += int(round((colm-coll)/2))
                # print(f"{coll} -> {colm}")
            if c.lower() == "l":
                col = colm-1
            else:
                col += coll+1
            # print(f"{col}")
            id = row * 8 + col
            if row in rows.keys():
                rows[str(row)].append(str(col))
            else:
                rows[str(row)] = [col]
            # print(f"row: {row}, col: {col}, id: {id}")
            if id > max: max = id
            answer.append(id)
    # print(len(answer))
    answer.sort()
    last = answer[0]
    for a in answer[1::]:
        if a-last > 1: return a-1
        last = a
    return max

def main():
    # data = get_test_inputs()
    data = get_inputs(DAY)

    print(f"1: {solve1(data)}")
    print(f"2: {solve2(data)}")

if __name__ == "__main__":
    sys.exit(main())
