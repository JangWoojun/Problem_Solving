from sys import stdin
input = stdin.readline

n = int(input())

while True:
    a = int(input())
    if a == 0:
        break
    if a % n == 0:
        print(f"{a} is a multiple of {n}.", sep="")
    else:
        print(f"{a} is NOT a multiple of {n}.", sep="")