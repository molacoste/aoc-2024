def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()

        ### PART 1
        matrix = [list(l) for l in lines]

        count = 0

        n = len(matrix)

        # horizontal check
        horizontals = [''.join(row) for row in matrix]

        for h in horizontals:
            count += h.count('XMAS')
            count += h[::-1].count('XMAS')

        # vertical check
        verticals = [''.join([row[i] for row in matrix]) for i in range(len(matrix[0]))]

        for v in verticals:
            count += v.count('XMAS')
            count += v[::-1].count('XMAS')

        # diagonal check LR
        diagonal_lrs = []

        for d in range(-n + 1, n):
            diagonal_lrs.append(''.join(matrix[i][i + d] for i in range(n) if 0 <= i + d < n))

        for dlrs in diagonal_lrs:
            count += dlrs.count('XMAS')
            count += dlrs[::-1].count('XMAS')

        # diagonal check RL
        diagonal_rls = []
        
        for d in range(2 * n - 1):
            diagonal_rls.append(''.join(matrix[i][d - i] for i in range(n) if 0 <= d - i < n))

        for drls in diagonal_rls:
            count += drls.count('XMAS')
            count += drls[::-1].count('XMAS')

        ### PART 2
        convul_diags = []
        count_two = 0

        for row in range(n - 2):  
            for col in range(n - 2):
                diag1 = ''.join([matrix[row + i][col + i] for i in range(3)])
                diag2 = ''.join([matrix[row + i][col + 2 - i] for i in range(3)])

                count_diag1 = diag1.count('MAS') + diag1[::-1].count('MAS')
                count_diag2 = diag2.count('MAS') + diag2[::-1].count('MAS')

                if count_diag1 > 0 and count_diag2 > 0:
                    count_two += 1

        print(count, count_two)


if __name__ == "__main__":
    main()
