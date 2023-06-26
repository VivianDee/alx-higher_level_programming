#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count < x and isinstance(i, int):
                print("{:d}".format(i), end="")
                count += 1
    except ValueError:
        pass
    finally:
        print()
        return (count)
