def bubblesort(mas):
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

def selectsort(mas):
    for i in range(len(mas)-1):
        imin=i
        for j in range(i+1,len(mas)):
            if mas[j]<mas[imin]:
                imin=j
        mas[i],mas[imin]=mas[imin],mas[i]
    return mas

def insertionsort(mas):
    for i in range(1,len(mas)):
        tmp=mas[i]
        j=i-1
        while j>=0 and mas[j]>tmp:
            mas[j+1]=mas[j]
            j-=1
        mas[j+1]=tmp
    return mas

def quicksort(mas,low,high):
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
    
def cocktail(mas): 
    up = range(len(mas) - 1)       
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if mas[i] > mas[i+1]:  
                    mas[i],mas[i+1] = mas[i+1],mas[i]
                    swapped = True
            if not swapped:
                return mas
