import re

def main():
    with open('input.txt', 'r') as file:
        text = file.read().strip()

    reg_part_one = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    valid_one = re.findall(reg_part_one, text)

    valid_two = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text)

    v = [int(l) * int(r) for l, r in valid_one]

    g = True

    ans = 0

    for i in valid_two:
        if i == "do()":
            g = True
        elif i == "don't()":
            g = False
        else:
            if g:
                l, r = map(int, i[4:-1].split(","))
                ans += l * r

    print(sum(v), ans)


if __name__ == "__main__":
    main()
