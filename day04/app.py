import requests, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cookie import cookie
import re

YEAR=2020
DAY=4

def get_inputs(day):
    data = []
    with open('input.txt', 'r') as f:
        passport = ""
        for a in f.readlines():
            if a != "\n":
                passport += a
            else:
                data.append(passport.replace("\n", " "))
                passport = ""
        data.append(passport.replace("\n", " "))
    return data

    # Web inputs were all kinds of weird, read in from file instead

    # url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    # r = requests.get(url, cookies=dict(session=cookie))
    # if r.status_code == 200: return r.text.splitlines()
    # print("Couldn't get inputs, update cookie")
    # sys.exit(1)

def get_test_inputs():
    data = []
    with open('test_input.txt', 'r') as f:
        passport = ""
        for a in f.readlines():
            if a != "\n":
                passport += a
            else:
                data.append(passport.replace("\n", " "))
                passport = ""
        data.append(passport.replace("\n", " "))
        return data

def parse_inputs1(data, skip_field):
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    valid_fields.sort()
    passport = data.split()
    valid_fields.remove(skip_field)
    keys = []
    for value in passport:
        keys.append(value.split(":")[0])
    keys.sort()

    if len(passport) == 8: return True
    if keys == valid_fields: return True
    return False

def parse_inputs2(data, skip_field):
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    valid_fields.sort()
    passport = data.split()
    valid_fields.remove(skip_field)
    keys = []
    for value in passport:
        keys.append(value.split(":")[0])
    keys.sort()
    temp_passport = {}
    for value in passport:
        k, v = value.split(":")
        temp_passport[k] = v
    try:
        if check_byr(temp_passport['byr']) and check_ecl(temp_passport['ecl']) and check_eyr(temp_passport['eyr']) and check_hcl(temp_passport['hcl']) and check_hgt(temp_passport['hgt']) and check_iyr(temp_passport['iyr']) and check_pid(temp_passport['pid']):
            return True
    except:
        return False

def check_byr(value):
    try:
        value = int(value)
    except:
        return False
    if 1920 <= value <= 2002: return True
    return False

def check_iyr(value):
    try:
        value = int(value)
    except:
        return False
    
    if 2010 <= value <= 2020: return True
    return False

def check_eyr(value):
    try:
        value = int(value)
    except:
        return False
    
    if 2020 <= value <= 2030: return True
    return False

def check_hgt(value):
    try:
        hgt = int(re.findall(r'[0-9]\d+', value)[0])
    except:
        return False
    try:
        measure = re.findall(r'[A-Za-z]\w+', value)[0]
    except:
        return False
    if measure == "cm":
        if 150 <= hgt <= 193: return True
    if measure == "in":
        if 59 <= hgt <= 76: return True
    return False

def check_hcl(value):
    try:
        hcl = value.split("#")[1]
    except:
        return False

    if len(hcl) == 6:
        if re.match(r'[A-Za-f0-9]{6,}', hcl):
            return True
    return False

def check_ecl(value):
    ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if value in ecls: return True
    return False

def check_pid(value):
    try:
        cid = int(value)
    except:
        return False
    if len(value) == 9: return True

    return False

def check_cid(value):

    return True

def solve1(inputs):
    answer = 0
    for passport in inputs:
        if parse_inputs1(passport, "cid"):
            answer += 1
    return answer

def solve2(inputs):
    answer = 0
    for passport in inputs:
        if parse_inputs2(passport, "cid"):
            answer += 1
    return answer

def main():
    # data = get_test_inputs()
    data = get_inputs(DAY)

    print(f"1: {solve1(data)}")
    print(f"2: {solve2(data)}")

if __name__ == "__main__":
    sys.exit(main())
