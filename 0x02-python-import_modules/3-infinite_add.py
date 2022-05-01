#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lsn = len(sys.argv) - 1
    sum = 0
    for a in sys.argv:
        if a != "./3-infinite_add.py":
            sum += int(a)
        print(f"{sum}")
