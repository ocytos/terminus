import os
import time
import sys
import random

def clear():
    sys.stdout.write('\033[H\033[2J')
    sys.stdout.flush()

def get_heavy_locomotive():
    return [
        r"             _________________               ____________________________________________________________________________ ",
        r"       _____|                |______________|_               [ T  E  R  M  I  N  U  S ]                             _|",
        r"      |cy   |      ||||      |              |                                                                       | ",
        r"    __|_____|______||||______|______________|_________________________________________________________________________| ",
        r"   |                                                                                                                 | ",
        r"   |    _D__      _      _      _      _      _      _      _      _      _      _      _      _      _      _        | ",
        r"   |___/____\____( )____( )____( )____( )____( )____( )____( )____( )____( )____( )____( )____( )____( )____( )_______| ",
        r"     oo-------oo  oo---oo  oo---oo  oo---oo  oo---oo  oo---oo  oo---oo  oo---oo  oo---oo  oo---oo  oo---oo  oo---oo    "
    ]

def animar():
    try:
        ancho, alto = os.get_terminal_size().columns, os.get_terminal_size().lines
    except OSError:
        ancho, alto = 120, 30
    tren = get_heavy_locomotive()
    pos_vertical = alto // 8
    for x in range(ancho + 20, -130, -4):
        clear()
        print("\n" * pos_vertical)
        if x + 15 < ancho:
            humo_prefix = " " * (x + 13)
            print(f"{humo_prefix}ocy")
            print(f"{humo_prefix}  ocy")
        else:
            print("\n")
        for linea in tren:
            if x > 0:
                print(" " * x + linea)
            else:
                offset = abs(x)
                if offset < len(linea):
                    print(linea[offset:])
        sys.stdout.flush()
        time.sleep(0.01)
