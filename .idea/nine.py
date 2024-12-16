num = int(input())
temp = num
sum = 0
while(temp != 0):
    r = temp % 10
    sum = sum + pow(r,3)
    temp = temp // 10

print(sum)