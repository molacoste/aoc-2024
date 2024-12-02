def main():
    safe_reports = 0
    safe_reports_with_dampener = 0

    with open('input.txt', 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))

            if (
                (all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)) or 
                all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))) and
                all(1 <= abs(numbers[i + 1] - numbers[i]) <= 3 for i in range(len(numbers) - 1))
            ):
                safe_reports += 1
            
            safe_with_dampener = False  

            for i in range(len(numbers)):
                removed = numbers[:i] + numbers[i+1:]

                if (
                    (all(removed[j] < removed[j + 1] for j in range(len(removed) - 1)) or 
                    all(removed[j] > removed[j + 1] for j in range(len(removed) - 1))) and
                    all(1 <= abs(removed[j + 1] - removed[j]) <= 3 for j in range(len(removed) - 1))
                ):
                    safe_with_dampener = True
                    
            if safe_with_dampener:
                safe_reports_with_dampener += 1

    print(safe_reports, safe_reports_with_dampener)


if __name__ == "__main__":
    main()
