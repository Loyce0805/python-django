result = [x * y for x in range(2,10) for y in range(1,10)]

print(result)

print()
result = [num * 3 for num in range(1,5) if num % 2 == 0]
print(result)

result = 0
a = 1
while a <= 1000:
    if a % 3 == 0:
        result += a
    a += 1
    
print(result)

result = 0
for a in range(1, 1001):
    if a % 3 == 0:
        result += a
    a += 1

print(result)

i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)
    
# for i in range(1, 101):
#     print(i)


i = 0
while i < 100:
    i += 1
    print(i)

sum = 0
i = 1
while i < 100:
    sum += i
    i += 1

print(sum)

