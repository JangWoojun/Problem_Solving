n = int(input())

for i in range(1,n+1):
    a = list(input().split())
    print(f"Case #{i}: ",end="")
    for i in reversed(range(len(a))):
        print(a[i],end=" ")
    print()