#!/usr/bin/python3
"""backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        a.append([i, None])

    def already_exists(j):
        for x in range(n):
            if j == a[x][1]:
                return True
        return False

    def reject(x, j):
        if (already_exists(j)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - j) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        for j in range(n):
            clear_a(x)
            if reject(x, j):
                a[x][1] = j
                if (x == n - 1):
                    print(a)
                else:
                    nqueens(x + 1)

    nqueens(0)
