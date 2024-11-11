def bubble_sort(mas):
    n=len(mas)
    unordered=True
    while unordered:
        unordered=False
        for j in range(n-1):
            if mas[j]>mas[j+1]:
                mas[j],mas[j+1]=mas[j+1],mas[j]
                unordered=True
        n-=1
    return mas

def select_sort(mas):
    for i in range(len(mas)-1):
        imin=i
        for j in range(i+1,len(mas)):
            if mas[j]<mas[imin]:
                imin=j
        mas[i],mas[imin]=mas[imin],mas[i]
    return mas

def insertion_sort(mas):
    for i in range(1,len(mas)):
        tmp=mas[i]
        j=i-1
        while j>=0 and mas[j]>tmp:
            mas[j+1]=mas[j]
            j-=1
        mas[j+1]=tmp
    return mas

def quick_sort(mas,low,high):
    if low<high:
        pivot_index=partition(mas,low,high)
        quick_sort(mas,low,pivot_index-1)
        quick_sort(mas,pivot_index+1,high)
def partition(mas,low,high):
    pivot=mas[low]
    i=low+1
    for j in range(low+1,high+1):
        if mas[j]<=pivot:
            mas[i],mas[j]=mas[j],mas[i]
            i+=1
    mas[low],mas[i-1] = mas[i-1],mas[low]
    return i-1
#Ниже - bogosort
import random
def sorted_(a):
    lenl = len(a)
    for i in range(0, lenl - 1):
        if(a[i] > a[i + 1]):
            return False
    return True
def random(a):
    lenl = len(a)
    for i in range(0, lenl):
        rnd = random.randint(0, lenl - 1)
        temp = a[i]
        a[i] = a[rnd]
        a[rnd] = temp  
def bogosort(a):
    while(not(sorted_(a))):
        random_permutation(a)
mas = []
n = int(input("Длина массива:")) 
for i in range(0, n): 
    elt = int(input("arr[" + str(i + 1) + "] = "))   
    mas.append(elt)
bogosort(mas) 
print(mas)
