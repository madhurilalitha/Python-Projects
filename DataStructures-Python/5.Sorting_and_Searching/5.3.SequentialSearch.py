'''
Sequential Search implementation in python
Logic - The function uses 'pos' object as index and Flag "found" to notify whether the element is found
Using while loop, the logic traverses through out the list visiting each element
If the element is found, it exists the while loop else it visits till the end of the list

It returns the boolean value of "found"
'''
def SequentialSearch(samplelist,item):
    pos = 0 #index
    found = False
    while pos<len(samplelist) and not found: #List traversal
        if samplelist[pos]==item:
            found = True
        else:
            pos = pos+1
    return found

#Testing
testlist = [1,2,32,8,17,19,42,13,0]
print ("Basic Sequential Search")
print (SequentialSearch(testlist,3))
print (SequentialSearch(testlist,32))

'''
5.3.1 Analysis of Sequential Search
Case1: Item is present
Bestcase - 1
Worst Case - n
Average Case - n/2

Case2 : Item not present
Best Case, Worst Case, Average Case - n

Hence, the complexity of sequential search is O(n)
'''

def SortedSequentialSearch(mylist,item):
    index =0
    stop =False
    found = False
    while index<len(mylist) and not found and not stop:
        if mylist[index]==item:
            found = True
        else:
            if mylist[index]>item:
                stop = True
            else:
                index = index+1
    return found

#Testing
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print ("Sequential Search in Sorted List")
print (SortedSequentialSearch(testlist,3)) # negative test case
print (SortedSequentialSearch(testlist,13)) #positive test case

'''
Analysis of Sequential Search in Sorted List
Case1: Item is present
Best Case: 1
Worst Case : n
Average case - n/2

Case 2:Item is not present
Best Case: 1
Worst Case : n
Average Case - n/2
'''
