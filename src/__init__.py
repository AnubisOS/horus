#!/usr/bin/env -S python 

from modules.tomb import * 

__version__ = "0.4.0"
__author__  = "Hussein Mukhtar"



def main():
    obe = obelisk()
    obe.make_background()
    obe.make_foreground()
    obe.carve()
    obe.destruct()


if __name__ == "__main__":
    main()
