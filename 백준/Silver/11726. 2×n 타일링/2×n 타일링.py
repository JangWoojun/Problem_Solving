from sys import stdin
input = stdin.readline

n = int(input())

arr = [0 for _ in range(1001)]
arr[1] = 1
arr[2] = 2

for i in range(3, 1001):
    arr[i] = (arr[i-1]+arr[i-2])%10007

print(arr[n])