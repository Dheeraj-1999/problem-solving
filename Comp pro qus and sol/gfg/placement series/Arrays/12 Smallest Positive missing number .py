# 84
# 36 27 -35 43 -15 36 42 -1 -29 12 -23 40 9 13 -24 -10 -24 22 -14 -39 18 17 -21 32 -20 12 -27 17 -15 -21 -48 -28 8 19 17 43 6 -39 -8 -21 23 -29 -31 34 -13 48 -26 -35 20 -37 -24 41 30 6 23 12 20 46 31 -45 -25 34 -23 -14 -45 -4 -21 -37 7 -26 45 32 -5 -36 17 -16 14 -7 0 37 -42 26 28 38

def findMissing(arr, size): 
    # your code goes here
    barr = sorted(arr)
    print(barr)

    # for i in range(len(arr)):
    #     if(arr[i] >= 0):
    #         index = i
    #         break;


    # for i in range(index, size-1):
    #     if(arr[i] >=0 and arr[i+1] != arr[i]+1 and arr[i+1] != arr[i]):
    #         if(arr[i] > 1 and arr[i-1] <= 0):
    #             return 1
    #         return arr[i]+1
    # return arr[size-1]+1
    d = {}
    for i in range(min(arr), max(arr)+1):
        d[i] = 0
    # print(d)
    for i in arr:
        d[i] += 1
    # print(d)
    for i in range(1, max(arr)):
        if(d.get(d[i])):
            continue
        print(i)
        break
arr = [int(i) for i in input().split(' ')]
findMissing(arr, len(arr))

# 85
# -47 1 4 49 -18 10 26 18 -11 -38 -24 36 44 -11 45 20 -16 28 17 -49 47 -48 -33 42 2 6 -49 30 36 -9 15 39 -6 -31 -10 -21 -19 -33 47 21 31 25 -41 -23 17 6 47 3 36 15 -44 33 -31 -26 -22 21 -18 -21 -47 -31 20 18 -42 -35 -10 -1 46 -27 -32 -5 -4 1 -29 5 29 38 14 -22 -9 0 43 -50 -16 14 -26

# 85
# -47 1 4 49 -18 10 26 18 -11 -38 -24 36 44 -11 45 20 -16 28 17 -49 47 -48 -33 42 2 6 -49 30 36 -9 15 39 -6 -31 -10 -21 -19 -33 47 21 31 25 -41 -23 17 6 47 3 36 15 -44 33 -31 -26 -22 21 -18 -21 -47 -31 20 18 -42 -35 -10 -1 46 -27 -32 -5 -4 1 -29 5 29 38 14 -22 -9 0 43 -50 -16 14 -26