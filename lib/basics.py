from itertools import izip_longest
import math
import random
import sys

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def circular(list,n):
    n = n%(len(list))
    # print "circular result",n
    return list[n]

def lcircular(list,n):
    return circular(list,n)

def sliceIterator(lst, sliceLen):
    for i in range(len(lst) - sliceLen + 1):
        yield lst[i:i + sliceLen]

def foreach2(lst):
    for i in range(0,len(lst) - 1,2):
        yield lst[i:i + 2]

def foreachn(lst,n):
    for i in range(0,len(lst) - (n-1),n):
        yield lst[i:i + n]


def pairs(lst):
    for i in range(len(lst) - 1):
        yield (lst[i],lst[i + 1])

def triplets(lst):
    for i in range(len(lst) - 2):
        yield lst[i:i + 3]

def circlepairs(list):
    for i in range(len(list) - 1):
        yield (list[i],list[i + 1])
    yield (list[-1],list[0])

def sample(range,abs):
    return range[0] + (range[1]-range[0])*abs

def rangefit(range,value):
    result = value
    if value < range[0]:
        result = range[0]
    elif value > range[1]:
        result = range[1]
    return result

def samples(rrange,niter):
    if niter == 1:
        return [rrange[0]]
    return [sample(rrange,float(i)/float(niter-1)) for i in range(niter)]

def usamples(niter):
    return samples((0.0,1.0),niter)

def urandsamples(niter):
    result = [random.uniform(0.0,1.0) for i in range(niter)]
    result.sort()
    result[0] = 0.0
    result[-1] = 1.0
    return result

def rand(min=0.0,max=1.0):
    return random.uniform(min,max)

def rands((min,max),niter):
    return [random.uniform(min,max) for i in range(niter)]


def rrandom(min,max):
    return rand(min,max)

def lrand(list):
    return list[int(float(len(list)) * rand())]

def normangle(angle):
    while angle > 2.0*3.14159:
        angle -= 2.0*3.14159
    while angle < 0.0:
        angle += 2.0*3.14159
    return angle

# valuelist must be [(),(),...,()]
def multisamples(valuelist,t):
    for (v1,v2) in pairs(valuelist):
        if t < v1[0]:
            return v1[1]
        elif t < v2[0]:
            absc = abscissa((v1[0],v2[0]),t)
            return sample((v1[1],v2[1]),absc)
    return valuelist[-1][-1]

def pi():
    return math.pi

def rangle():
    return (0.0,2.0*math.pi)

def abscissa(range,t):
    t1,t2 = range
    if t > t2:
        return t2
    elif t < t1:
        return t1
    elif t1 == t2:
        return t1
    else:
        return (t - t1)/(t2 - t1)

def circularnext(list,v):
    if len(list)<2:
        return ""
    elif list.count(v) < 1:
        return ""
    elif v == list[-1]:
        return list[0]
    else:
        return list[list.index(v)+1]

def circularprev(list,v):
    if len(list)<2:
        return ""
    elif list.count(v) < 1:
        return ""
    elif v == list[0]:
        return list[-1]
    else:
        return list[list.index(v)-1]

def lunique(input):
    newresult = []
    for item in input:
        if not item in newresult:
            newresult.append(item)
    return newresult

def lremove(input,removed):
    newresult = []
    for item in input:
        if not item == removed:
            newresult.append(item)
    return newresult

def lsubstract(input,removeds):
    newresult = []
    for item in input:
        if not item in removeds:
            newresult.append(item)
    return newresult

def lmin(linput,*nextlist):
    if len(nextlist) != 0:
        linput = [linput]
        for i in range(len(nextlist)):
            linput.append(nextlist[i])

    result = linput[0]
    for item in linput[1:]:
        if item < result:
            result = item
    return result
    

def lmax(input):
    result = input[0]
    for item in input[1:]:
        if item > result:
            result = item
    return result

def lconcat(*lists):
    result = lists[0][:]
    for list in lists[1:]:
        result.extend(list)
    return result

def ladd(list):
    result = 0.0
    for item in list:
        result += item
    return result

def lsum(list):
    result = []
    sum = 0.0
    for i in list:
        sum += i
        result.append(sum)
    return result

def lacc(list):
    result = []
    csum = 0.0
    for item in list:
        csum += item
        result.append(csum)
    return result

def lrepeat(list,ntimes):
    result = []
    for i in range(ntimes):
        result.extend(list)
    return result

def lfront(list):
    return list[0]

def lback(list):
    return list[-1]

def litems(list,period,start=0):
    result = []
    for i in range(start,len(list),period):
        result.append(list[i])
    return result

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


# from http://stackoverflow.com/questions/1335392/iteration-over-list-slices
# map(None, *(iter(range(10)),) * 3)
# list_of_slices = zip(*(iter(the_list),) * slice_size)

# big_list = [1,2,3,4,5,6,7,8,9]
# slice_length = 3
# def sliceIterator(lst, sliceLen):
#    for i in range(len(lst) - sliceLen + 1):
#        yield lst[i:i + sliceLen]
