"""
Given an array a[] of size N which contains elements from 0 to N-1,
you need to find all the elements occurring more than once in the given array.

Your Task:
Complete the function duplicates() which takes array a[] and n as input
as parameters and returns a list of elements that occur more than once in the given array
in sorted manner. If no such element is found, return list containing [-1].
"""
def duplicates(arr, n):
    	list={}
    	duplicates=[]
    	noduplicates=[-1]
    	for element in arr:
    	    if element in list:
    	        list[element]+=1
    	    else:
    	        list[element]=1
    	for keys, values in list.items():
    	    if values>1:
    	        duplicates.append(keys)
    	#print(duplicates)
    	duplicates.sort()
    	if len(duplicates)!=0:
    	    return duplicates
    	else:
    	    return noduplicates
n=int(input("Enter a Natural number"))
array=[]
for i in range(0,n):
    element=int(input("Enter the number"))
    array.append(element)
Soln=duplicates(array,n)
print("The numbers occuring more than once in the array are")
for i in Soln:
    print(i,end="")
    

