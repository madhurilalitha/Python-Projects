'''

'''
def binarysearch(mylist,item):

    first = 0
    last = len(mylist)-1
    found = False

    while first<=last and not found:
        midpoint = round((first+last)/2)
        if mylist[midpoint]==item:
            found = True
        else:
            if item < mylist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint +1
    return found

#Testing
print ("Basic Binary Search example")
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print (binarysearch(testlist,3)) #Negative testcase
print (binarysearch(testlist,13)) # positive test case
print ("-------------------------")


'''
Implementation of binary search using Recursion - Divide and Conquer Approach'''

def BinarySearchRecursion(mylist,item):
    start = 0
    last = len(mylist)-1

    if len(mylist)==0:
        return False
    else:
        midpoint = round((start+last)/2)
        if mylist[midpoint]==item:
            return True
        else:
            if item<mylist[midpoint]:
                return BinarySearchRecursion(mylist[:midpoint],item)
            else:
                return BinarySearchRecursion(mylist[midpoint+1:],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print ("Binary search using recursion")
print(BinarySearchRecursion(testlist, 3)) #negative test case
print(BinarySearchRecursion(testlist, 13)) # positive test case

'''
Analysis of Binary Search Algorithm
When we split the list enough times, we end up with a list that has just one item. Either that is the item 
we are looking for or it is not. Either way, we are done. The number of comparisons necessary to get to this 
point is i where n2i=1n2i=1. Solving for i gives us i=logni=log⁡n. The maximum number of comparisons is logarithmic 
with respect to the number of items in the list. 
Therefore, the binary search is O(logn)
'''
'''
The recursion implementation of binarysearch used the logic "slicing the array" which takes O(k) time complexity
Therefore alternate efficient implementation can be found below
'''

def RecBinSearch(mylist,item,first,last):
    first = 0
    last = len(mylist)-1
    if (len(mylist)==0):
        return False
    else:
        midpoint = round ((first+last)/2)
        if mylist[midpoint]==item:
            return True
        else:
            if mylist[midpoint]>item:
                last = midpoint-1
                return RecBinSearch(mylist,item,first,last)
            else:
                first = midpoint+1
                return RecBinSearch(mylist,item,first,last)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print ("Binary search using recursion")
print(RecBinSearch(testlist, 3,0,8)) #negative test case
print(RecBinSearch(testlist, 13,0,8)) # positive test case
