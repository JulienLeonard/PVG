from itertools import izip_longest
import math
import random
import sys

#
# return the circular nth item from a list
#
def circular(list,n):
    n = n%(len(list))
    # print "circular result",n
    return list[n]

#
# alias for circular
#
def lcircular(list,n):
    return circular(list,n)

#
# general grouping pattern
# [i for i in sliceIterator(range(5),3)]  == [[0,1,2],[1,2,3],[2,3,4]]
#
def sliceIterator(lst, sliceLen):
    for i in range(len(lst) - sliceLen + 1):
        yield lst[i:i + sliceLen]

#
# run along a list 2 by 2
# [i for i in foreach2(range(5))] == [[0,1],[2,3]]
#
def foreach2(lst):
    for i in range(0,len(lst) - 1,2):
        yield lst[i:i + 2]

#
# generalization of foreach2
# [i for i in foreachn(range(7),3)] == [[0,1,2],[3,4,5]]
#
def foreachn(lst,n):
    for i in range(0,len(lst) - (n-1),n):
        yield lst[i:i + n]

#
# run along a list by each pair
# [i for i in pairs(range(4))] == [(0,1),(1,2),(2,3)]
#
def pairs(lst):
    for i in range(len(lst) - 1):
        yield (lst[i],lst[i + 1])

#
# same as pairs but with 3 items
# [i for i in triplets(range(4))] == [(0,1,2),(1,2,3)]
#
def triplets(lst):
    for i in range(len(lst) - 2):
        yield (lst[i],lst[i + 1],lst[i + 2])

#
# same as pairs but with a closing circular pair at the end
# [i for i in pairs(range(4))] == [(0,1),(1,2),(2,3),(3,0)]
#
def circlepairs(list):
    for i in range(len(list) - 1):
        yield (list[i],list[i + 1])
    yield (list[-1],list[0])

#
# get a linear sample from a range
# do not check the bounds of abs (and extend the linearity out of the range)
#
def sample(range,abs):
    return range[0] + (range[1]-range[0])*abs

#
# trim a value to fit the range
#
def rangefit(range,value):
    result = value
    if value < range[0]:
        result = range[0]
    elif value > range[1]:
        result = range[1]
    return result

#
# get n values evenly distributed from rrange
#
def samples(rrange,niter):
    if niter == 0:
        return []
    if niter == 1:
        return [rrange[0]]
    return [sample(rrange,float(i)/float(niter-1)) for i in range(niter)]

#
# shortcut for sampling the unitary range
#
def usamples(niter):
    return samples((0.0,1.0),niter)

#
# get n random values inside the unitary range, sorted, and completely covering the range
#
def urandsamples(niter):
    if niter == 0:
        return []
    if niter == 1:
        return [0.0]
    result = [random.uniform(0.0,1.0) for i in range(niter)]
    result.sort()
    result[0] = 0.0
    result[-1] = 1.0
    return result

#
# shortcut to get a random value
#
def rand(min=0.0,max=1.0):
    return random.uniform(min,max)

#
# get a number of rand values from the range
#
def rands((min,max),niter):
    return [random.uniform(min,max) for i in range(niter)]

#
# alias for rand
#
def rrandom(min,max):
    return rand(min,max)

#
# return a random item from a list
#
def lrand(list):
    if list == []:
        return ""
    return list[int(float(len(list)) * rand())]


#
# alias for pi
#
def pi():
    return math.pi

#
# normalize an angle
#
def normangle(angle):
    while angle > 2.0*pi():
        angle -= 2.0*pi()
    while angle < 0.0:
        angle += 2.0*pi()
    return angle

#
# valuelist must be [(t1,v1),(t2,v2),...,(tn,vn)]
# with t1 <= t1 <= ... <= tn
# TODO: add edge cases
#
def multisamples(valuelist,t):
    if valuelist == []:
        return ""
    
    for (v1,v2) in pairs(valuelist):
        if t < v1[0]:
            return v1[1]
        elif t < v2[0]:
            absc = abscissa((v1[0],v2[0]),t)
            return sample((v1[1],v2[1]),absc)
    return valuelist[-1][-1]

#
# return angle range
#
def rangle():
    return (0.0,2.0*math.pi)

#
# given a range, get the linear abscissa corresponding to the v value
#
def abscissa(range,v):
    v1,v2 = range
    if v > max(v1,v2):
        return 1.0
    elif v < min(v1,v2):
        return 0.0
    elif v1 == v2:
        return 0.0
    else:
        return (v - v1)/(v2 - v1)

#
# get the next item of v from a list in a circular way
#
def circularnext(list,v):
    if len(list)<1:
        return ""
    elif list.count(v) < 1:
        return ""
    elif v == list[-1]:
        return list[0]
    else:
        return list[list.index(v)+1]

#
# reverse of circularnext
#
def circularprev(list,v):
    if len(list)<1:
        return ""
    elif list.count(v) < 1:
        return ""
    elif v == list[0]:
        return list[-1]
    else:
        return list[list.index(v)-1]

#
# return a list with duplicates removed
#
def lunique(input):
    newresult = []
    for item in input:
        if not item in newresult:
            newresult.append(item)
    return newresult

#
# return a list with item removed removed
#
def lremove(input,removed):
    newresult = []
    for item in input:
        if not item == removed:
            newresult.append(item)
    return newresult

#
# return a list with all the items inside removeds removed from input
#
def lsubstract(input,removeds):
    newresult = []
    for item in input:
        if not item in removeds:
            newresult.append(item)
    return newresult

#
# compute min of list (either single list, or list of args)
#
def lmin(linput,*nextlist):
    if len(nextlist) != 0:
        linput = [linput]
        for i in range(len(nextlist)):
            linput.append(nextlist[i])

    if len(linput) < 1:
        return None
    result = linput[0]
    for item in linput[1:]:
        if item < result:
            result = item
    return result

#
# compute max of list
#
def lmax(input):
    if len(input) < 1:
        return None

    result = input[0]
    for item in input[1:]:
        if item > result:
            result = item
    return result

#
# flatten list of lists
#
def lconcat(*lists):
    return [item for list in lists for item in list]

#
# compute sum of list items
#
def ladd(list):
    if len(list) < 1:
        return None
    result = 0.0
    for item in list:
        result += item
    return result

#
# compute all intermediate sums of list
#
def lsum(list):
    if len(list) < 1:
        return None
    csum = list[0]
    result = [csum]
    for i in list[1:]:
        csum += i
        result.append(csum)
    return result

#
# same as lsum
#
def lacc(list):
    return lsum(list)

#
# repeat and concat content of list ntimes
#
def lrepeat(list,ntimes):
    result = []
    for i in range(ntimes):
        result.extend(list)
    return result

#
# return list first item
#
def lfront(list):
    if len(list) < 1:
        return None
    return list[0]

#
# return list last item
#
def lback(list):
    if len(list) < 1:
        return None
    return list[-1]

#
# extract items from list 
#
def litems(list,period,start=0):
    result = []
    for i in range(start,len(list),period):
        result.append(list[i])
    return result

#
# same as lsublist
#
def lsublist(list,period,start=0):
    return litems(list,period,start)

def mean(v1,v2):
    return (v1+v2)/2.0

def lmean(list):
    return sum(list)/len(list)

def lmiddle(list,offset=0):
    if len(list) < 1:
        return None
    else:
        return list[len(list)/2 + offset]

def lreverse(input):
    result = input[:]
    result.reverse()
    return result

def lflatten(list):
    result = []
    for sublist in list:
        result.extend(sublist)
    return result

def lsplit(list,nitems):
    result = []
    for i in range(0,len(list),nitems):
        result.append(list[i:i+nitems])
    return result

def lrange(list):
    return (lmin(list),lmax(list))

def lclose(list):
    return list + [list[0]]

def sign(num):
    if num < 0.0:
        return -1.0
    return 1.0

def iff(test,result1,result2):
    if test:
        return result1
    else:
        return result2

def lgeo(xrange,rfactor,nitems):
    result = [1.0]
    for i in range(nitems):
        result.append(result[-1]*rfactor)
    result = [1.0-i for i in result]
    georange = (result[0],result[-1])
    # print "result",result
    return [sample(xrange,abscissa(georange,i)) for i in result]

def ldoublegeo(xrange,rfactor,nitems):
    result = [1.0]
    for i in range(nitems/2):
        result.append(result[-1]*rfactor)
    newresult = result[:]
    newresult.reverse()
    result = [2.0-i for i in result]
    newresult.extend(result)
    georange = (newresult[0],newresult[-1])
    print "newresult",result
    return [sample(xrange,abscissa(georange,i)) for i in newresult]

def lzip (list1,list2):
    minsize = min(len(list1),len(list2)) 
    return [(list1[i],list2[i]) for i in range(minsize)]

def lzipflat (list1,list2):
    minsize = min(len(list1),len(list2)) 
    result = []
    for i in range(minsize):
        result = result + [list1[i],list2[i]]
    return result

def lunzip(zlist):
    return ([i[0] for i in zlist],[i[1] for i in zlist])

def puts(*arg):
    print arg
    sys.stdout.flush()

def lidentity(list):
    return list

def lshuffle(list):
    result = list[:]
    random.shuffle(result)
    return result

def popfront(list):
    return (list[0],list[1:])

def lappends(list,*arg):
    result = list
    for item in arg:
        result.append(item)
    return result

def lshift(list,n):
    return list[n:] + list[0:n]

def fileexists(filepath):
    try:
        with open(filepath): 
            return True
    except IOError:
        return False

def vtrim(min,max,v):
    if v < min:
        return min
    elif v > max:
        return max
    else:
        return v

def bidirection(i,modulo):
    if ((i % (2*modulo)) < modulo):
        return i % modulo;
    else:
        return modulo - (i % modulo);
	
def alt(boolv,v1,v2):
    if boolv:
        return v1
    else:
        return v2

def ldoublesym(list):
    return list + lreverse(list[1:-1])


