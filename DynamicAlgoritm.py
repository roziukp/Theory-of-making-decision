from random import randint
from  pandas import DataFrame
import numpy as np

#creating matrix 5x5
def matrix(n):
    X=[[randint(-5,20) for i in range(n)] for _ in range(n)]
    return X


#Main function for searching the biggest sum on the rout
def calc(X,n,x,y,arr):

    #possible transition variants
    brr=[X[x-1][y],X[x][y+1],X[x-1][y+1]]
    #max number index from brr
    maxim=brr.index(max(brr))
    #array of indexes
    d=[[x-1,y],[x,y+1],[x-1,y+1]]

    for keys in range(len(d)):
        if keys == maxim:
            print('Index: {} | max: {}'.format(d[keys],max(brr)))
            a,b=d[keys][0],d[keys][1]
            break
    arr[a][b] = X[a][b]

    if d[keys][0]==0:
        for i in range(d[keys][1]+1,len(X)):
            print('Index: [0, {}] | max: {}'.format(i,X[0][i]))
            arr[0][i] = X[0][i]
    elif d[keys][1]==4:
        for i in range(d[keys][0]-1,-1,-1):
            print('Index: [{}, 4] | max: {}'.format(i,X[i][4]))
            arr[i][4] = X[i][4]
        return 0
    else:
        calc(X, d[keys][0], d[keys][0], d[keys][1],arr)

def main():
    n=int(input('Matrix size: '))
    X=matrix(n)
    #X=[[17,14,7,9,3,],[25,19,21,16,5],[39,36,31,24,3],[40,35,28,26,7],[44,37,30,24,15]]
    arr = [['*'] * 5 for i in range(5)]
    arr[4][0]=X[4][0]
    #input array
    for i in X:
        print(i)
    print("__________________________")
    calc(X,n,4,0,arr)
    print("__________________________")
    #Output array(rout BOTTOM-UP)
    for i in arr:
        print(i)


if __name__ == '__main__':
    main()


