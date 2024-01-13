#!/usr/bin/python3
import sys
def main ():
    num_args = lens(sys.argv) - 1
    print ("num of argument(s):", num_args)
    if num_args == 0:
        print ("./n")
    else:
        print ("Arguments:")
        for i in range (1, num_args + 1):
            print ("{}: {}".format(i, sys.argv[i]))
            print()
            if __name__ =="__main __":
                main ()
