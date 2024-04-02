#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        outcome = fct(*args)
        return outcome
    except ZeroDivisionError:
        pass
    except (IndexError, ValueError, TypeError):
        print("Exception: {}".format(sys.ecx_info()[1]), file=sys.stderr)
    return None
