import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cookie import cookie
import requests


YEAR = 2020
DAY = 6


def get_inputs(day):

    data = []
    with open('input.txt', 'r') as f:
        group = ""
        for a in f.readlines():
            if a != "\n":
                group += a
            else:
                split = group.strip().split("\n")
                data.append(split)
                group = ""
        data.append(group.replace("\n", " "))
    # print(len(data))

    return data

    # url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    # r = requests.get(url, cookies=dict(session=cookie))
    # if r.status_code == 200: return r.text.splitlines()
    # print("Couldn't get inputs, update cookie")
    # sys.exit(1)


def get_test_inputs():
    data = []
    with open('test_input.txt', 'r') as f:
        group = ""
        for a in f.readlines():
            if a != "\n":
                group += a
            else:
                split = group.strip().split("\n")
                data.append(split)
                group = ""
        data.append(group.replace("\n", " "))
    # print(len(data))
    return data
    # with open('test_input.txt', 'r') as f:
    # return f.read().splitlines()


def solve1(inputs):
    answer = 0
    for group in inputs:
        answers = {}
        for a in group:
            if a != " ":
                if len(a) > 1:
                    for yeses in a:
                        if yeses not in answers.keys():
                            answers[yeses] = 1
                        else:
                            answers[yeses] += 1
                else:
                    if a not in answers.keys():
                        answers[a] = 1
                    else:
                        answers[a] += 1
                # print(answer)
            # print(f"{answer} + {len(answers)} = {answer + len(answers)}")
        # print(f"{len(answers)}, {sorted(answers)}")
        answer += len(answers.keys())
    return answer


def solve2(inputs):
    answer = 0
    for group in inputs:
        answers = {}
        answers['group'] = 0
        # print(group)
        if len(group) == 1:
            answers['group'] = len(group)
            for a in group:
                if a != " ":
                    for yeses in a:
                        if yeses not in answers.keys():
                            answers[yeses] = 1
            # print(answers)
        else:
            answers['group'] = len(group)
            for a in group:
                if len(a) > 1:
                    for yeses in a:
                        if yeses not in answers.keys():
                            answers[yeses] = 1
                        else:
                            answers[yeses] += 1
                else:
                    if a not in answers.keys():
                        answers[a] = 1
                    else:
                        answers[a] += 1
        # print(answers)
        for a in answers:
            if answers[a] == answers['group'] and a != "group":
                answer += 1
            # print(f"{answer} + {len(answers)} = {answer + len(answers)}")
        # print(f"{len(answers)}, {sorted(answers)}")
        # answer += len(answers.keys())
    return answer


def main():
    # data = get_test_inputs()
    data = get_inputs(DAY)

    print(f"1: {solve1(data)}")
    print(f"2: {solve2(data)}")


if __name__ == "__main__":
    sys.exit(main())
