def bubble_sort(l):
    """
#input params: unsorted list
#output params: sorted list"""
    for y in range(len(l)):
        for x in range(len(l)):
            if x != len(l) - 1:
                if l[x+1] < l[x]:
                    l[x+1],l[x] = l[x],l[x+1]  
                   
