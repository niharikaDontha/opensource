x,y,z=map(int, input().split())
total=x*y
max=2*24*60
if total<=max:
    print("YES")
else:
    print("NO")
