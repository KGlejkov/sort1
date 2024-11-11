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
    
def cocktailsort(a):
    n=len(a)
    swapp=True
    e=n-1
    s=0
    e=n-1
    while swapp==True:
        swapp=False
        for i in range(s,e):
            if a[i] > a[i+1] :
                a[i], a[i+1]= a[i+1], a[i]
                swapp=True
        if swapp==False:
            break
        swapp=False
        e=e-1
        for i in range(e-1, s-1,-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapp=True
        s=s+1
    return a
