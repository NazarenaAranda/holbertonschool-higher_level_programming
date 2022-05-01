#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lsn = len(sys.argv) - 1
    print(f"{lsn:d} ", end='')
    if lsn == 0:
        print("arguments:.")
    if lsn == 1:
        print("argument:")
    if lsn > 1:
        print("arguments:")
    aux = 0
    for a in sys.argv:
        if a != "./2-args.py":
            aux += 1
            print(f"{aux}: {a}")
