#write a function "logfactorial" that calculates log(n!) for any integer n>0
#Use math.log() to calculate the log of a single value and use a loop to iterate over i and get the log(i) values
#Add a docstring
#add checks on the input n (should be an integer and non-negative)
####################################THIS PART IS DONE#####################################################


#add tests as examples inside the docstring. For tests to be used, add a section usng the doctest module. 
#Check that you can run the checks with ./binomial.py --tests
#add an optional argument k to calculate log(n!/k!) = log((k+1)*...*n) = log(k+1)+...+log(n) with default k=0
#and return log(1)=0 if k>n, with no error (because it's a sum of zero terms).
#add a check that k is a non negative integer
#add examples to test the function with a non-default k such as n=5 and some k<5, also n=k=5 (boundary), and n=5, k=6
#Write a function to choose to calculate the log of a binomial log(choose(n,k)) for any integeres n>=0 and 0 <= k <= n. Start with the docstring and with a test. Recall that
#choose(n,k) = n!/(k! (n-k)!), so log(choose(n,k)) = log(n!/k!) - log((n-k)!) and you can use the function from step 5 twice. (Functions are supposed
#to make your life easier by eliminating the need to rewrite code for every case)
#add an optional argument to this 'choose' function to return either the binomial coeffiicient itself as an integer or its log as a float.
#Make the function return either the binomial coefficient by default, not its log
#add a docstring for the module itself. Add arguments for the script itself to be able to run it like in the example below:


#when ready to run, include `import binomial` ... other instructions online. You will need to change the file permissions ('chmod u+x' and adding the 'shebang' to the beginning of the file)

import math
import numpy
import argparse

# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="total number of items to choose from")
parser.add_argument("-k", type=int, default=0, help="total number of items to choose")
parser.add_argument("-l", "--log", type=str, help="returns the log binomial coefficient")
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

    print("Called logFactorial() with values of n=",num,"and k=",kay)

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
        print("Returned",logFactorial)
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
        print("Returned",logFactorial)
        return logFactorial

def choose(num=args.n,kay=args.k): #has doctest in docstring
    """returns the binomial coefficient.
    Examples:

    >>> choose(5,3)
    10
    """
    #The number of ways to choose k elements among n is choose(n,k) = n! / (k! (n-k)!) where factorial n: n! = 1*2*...*n 
    #becomes very big very fast. But many terms cancel each other in “n choose k”.
    assert 0<=kay<=num, "K must be at least 0 and no larger than N."
    print("Called choose() with values of n=",num,"and k=",kay)
    difference = num - kay
    logDiff = logfactorial(difference,0)
    logNumOverKay = logfactorial(num,kay)
    nChooseK = logNumOverKay - logDiff
    print("Returned nChooseK of",nChooseK)
    return nChooseK

def testing():
    print("Testing the module...")

    print("Done with tests.")

#Call the other methods depending on the arguments
if __name__ == '__main__':
    if args.test:
        testing()
    elif args.log:
        choose(args.n,args.k)
    else:
        logfactorial(args.n,args.k)
 #still needs to have an optional argument for the log part...