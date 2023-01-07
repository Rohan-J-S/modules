def row_echelon(l , i , j):
    if i >= len(l):
        return l
        
    elif j >= len(l[0]):
        return l
    # print(l[i][j])
    if l[i][j] == 0:
        # print("hi")
        for temp in range(i , len(l)):
            if l[temp][j] != 0:
                l[i] , l[temp] = l[temp] , l[i]
                # print(l)
                break
        else:
            row_echelon(l , i , j+1)

    k = l[i][j]
   
    for temp in range(j , len(l[0])):
        l[i][temp] /= k
    for temp in range(i+1 , len(l)):
        c = l[temp][j]
        
        for temp_2 in range(j , len(l[0])):
            l[temp][temp_2] -= c*l[i][temp_2]
    return row_echelon(l , i+1 , j+1)

def identity(l , i):
    if i < 0:
        return l
    k = len(l[0]) - 2

    for temp in range(k , i , -1):
       
        c = l[i][temp]
        l[i][temp] = 0
        l[i][k+1] -= c*l[temp][k+1]

    return identity(l , i-1)



l = [
[6 , 15 , 2 , 72],
[1 , 1 , 54 , 110] , 
[27, 6 , -1 , 85]

]

final = row_echelon(l , 0 , 0)

for temp in final:
    print(temp)
print()
final_2 = identity(final , 2)

for temp in final_2:
    print(temp)
for x in range(len(final_2)):
    print('x',x , ' = ' , final_2[x][len(l[0])-1] , sep = '')
