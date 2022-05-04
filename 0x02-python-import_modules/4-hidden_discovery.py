#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lista = dir(hidden_4)
    for im in lista:
        if im[0:2] != "__":
            print(f"{im}")
