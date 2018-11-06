import math
import numpy
import argparse

# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="total number of items to choose from")
parser.add_argument("-k", type=int, default=0, help="total number of items to choose")
parser.add_argument("-l", "--log", type=str, help="returns the integer binomial coefficient")
parser.add_argument("--float", type=str, help="returns the log binomial coefficient")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

# test argument problems early:
if not args.test and __name__ == '__main__':
    if args.n<=0:
        raise Exception("argument -n must greater than 0")
    # no error if file imported as module

def logfactorial(num=args.n,kay=args.k): #has doctest in docstring
    """Returns the log of a factorial.
    Examples: num = 5, 5! =120

    >>> logfactorial(5)
    2.07918124605"""

    #print("Called logFactorial() with values of n=",num,"and k=",kay)

    if kay>num:
        print("Sum of zero terms when k>n; log(1) = 0")
        return 0
    elif kay==0:
        logFactorial=math.log(num) #initialize logFactorial with log of num
        #print("logFactorial so far is",logFactorial)
        for i in range(1,num):
            logNum = math.log(i)
            #print("i is",i,"and log(i) is",logNum)
            logFactorial = logFactorial + logNum 
            #print("Current value of logFactorial is ",logFactorial)
        #print("Returned",logFactorial)
        return logFactorial
    else:
        logFactorial=math.log(num) #initialize logFactorial with log of num
        logKayFactorial=math.log(kay) #initialize logKayFactorial with log of kay
        #print("logFactorial so far is",logFactorial)
        for i in range(1,num):
            logNum = math.log(i)
            #print("i is",i,"and log(i) is",logNum)
            logFactorial = logFactorial + logNum
            #print("Current value of logFactorial is ",logFactorial)
        for i in range(1,kay):
            logKay = math.log(i)
            logKayFactorial = logKayFactorial + logKay
            #print("Current value of logKayFactorial is ",logKayFactorial)
        logFactorial = logFactorial - logKayFactorial
        #print("Returned",logFactorial)
        return logFactorial

def choose(num=args.n,kay=args.k): #has doctest in docstring
    """returns the binomial coefficient.
    Examples:

    >>> choose(5,3)
    10
    
    >>> choose(7,3)
    3.555348061489415
    """
    
    #The number of ways to choose k elements among n is choose(n,k) = n! / (k! (n-k)!) where factorial n: n! = 1*2*...*n 
    #becomes very big very fast. But many terms cancel each other in “n choose k”.
    assert 0<=kay<=num, "K must be at least 0 and no larger than N."
    #print("Called choose() with values of n=",num,"and k=",kay)
    difference = num - kay
    logDiff = logfactorial(difference,0)
    logNumOverKay = logfactorial(num,kay)
    nChooseK = logNumOverKay - logDiff
    #print("Returned nChooseK of",nChooseK)
    return nChooseK

def convertLog(num): #make the --log argument default to this method (call this first), else just call choose()
    """Converts the input from log base 2 to original integer form."""
    coefficient = choose(args.n,args.k)
    coefficient = 2**coefficient
    return coefficient

#This function works
def testing():
    if __name__ == "__main__":
        print("Testing the module...")
        import doctest
        doctest.testmod()
        print("Done with tests.")

#Call the other methods depending on the arguments
if __name__ == '__main__':
    if args.test:
        testing()
    elif args.log:
        convertLog()
    elif args.float:
        choose(args.n,args.k)
    else:
        logfactorial(args.n,args.k)
 
