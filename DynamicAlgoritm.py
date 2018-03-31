from random import randint
from  pandas import DataFrame
import numpy as np

#creating matrix 5x5
def matrix(n):
    X=[[randint(-5,20) for i in range(n)] for _ in range(n)]
    return X

# def newArr(a,b,X):
#     arr = [[0] * 5 for i in range(5)]
#     arr[a][b] = X[a][b]
#     return arr


def calc(X,n,x,y,arr):

    brr=[X[x-1][y],X[x][y+1],X[x-1][y+1]]
    maxim=brr.index(max(brr))

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
    n=5
    X=matrix(n)
#   matr=np.array(X)
    arr = [['*'] * 5 for i in range(5)]
    arr[4][0]=X[4][0]


    for i in X:
        print(i)
    print("__________________________")
    calc(X,n,4,0,arr)
    print("__________________________")
    for i in arr:
        print(i)


if __name__ == '__main__':
    main()


