# -*- coding: utf-8 -*-
"""
Merge Sort.
Created on Fri Oct 16 17:00:27 2020

@author: 
"""
def mergeSort(myList):
    if len(myList)>1:
        return mergeSubList(mergeSort(myList[:len(myList)//2]),mergeSort(myList[len(myList)//2:]))
    else:
        return myList

def mergeSubList(list1,list2):
    newList =[0]*(len(list1)+len(list2))
    j=0
    k=0
    for i in range(len(newList)):
        if j>=len(list1):
            while i<(len(newList)):
                newList[i]=list2[k]
                #print("residual_L2 ", newList[i])
                k +=1
                i +=1
            break
        if k>=len(list2):
            while i <len(newList):
                newList[i]=list1[j]
                #print("residual_L1 ", newList[i])
                j +=1
                i +=1
            break
        if list1[j][0]>=list2[k][0]:
            newList[i]=list1[j]
            #print("main_True ",newList[i])
            j +=1
        else:
            newList[i]=list2[k]
            #print("main_False ",newList[i])
            k +=1
    return newList

#myList_a = [8]
#myList_b= [7]
#print(mergeSubList(myList_a,myList_b))
# myList = [1,2,200,4,5,6,7,145,34]
# print(mergeSort(myList))
#input("This is your result")
