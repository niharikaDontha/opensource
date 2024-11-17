n, m = map(int, input().split())
arr = list(map(int, input().split()))
num1 , num2 = 0, 0
for i in arr:
    if i%m ==0:
        num2+=i
    else:
        num1 +=i
result = num1-num2
print(-abs(result) if result>0 else abs(result))
