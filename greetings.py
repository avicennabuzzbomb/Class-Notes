#!/usr/bin/env python
"""module with very cool functions to say 'hi'"""

import argparse
# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="number of times to say hi")
parser.add_argument("-l", "--long", action="store_true", help="whether to say 'hi' the long way")
parser.add_argument("-g", "--greetings", type=str, help="greeting message, like a name")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()
hi = "Howdy" if args.long else "Hi"

# test argument problems early:
if not args.test and __name__ == '__main__':
    if args.n<0:
        raise Exception("argument -n must be 0 or positive")
    # no error if file imported as module

def print_greetings(extra_greetings, n=args.n):
    """
    print individualized greeting. example:
    >>> print_greetings("have a good day", 0)
    have a good day, you.
    """
    s = ""
    for i in range(0,n):
        s += hi + ", "
    if extra_greetings:
        s += extra_greetings + ", "
    s += args.greetings if args.greetings else "you"
    s += "."
    print(s)

def runTests():
    print("testing the module...")
    if args.n:
        print("ignoring n for testing purposes")
    import doctest
    doctest.testmod()
    print("done with tests.")

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        print_greetings("")