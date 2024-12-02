def main():
    left = []
    right = []

    with open('input.txt', 'r') as file:
        for line in file:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

    left.sort()
    right.sort()

    part_one_holder = 0
    part_two_holder = 0
    
    for i in range(len(left)):
        part_one_holder += abs(left[i]-right[i])
        part_two_holder += left[i] * right.count(left[i]) 
    
    print(part_one_holder, part_two_holder)


if __name__ == "__main__":
    main()
