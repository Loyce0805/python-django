A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0
for score in A:
    total += score
average = total / len(A)

print(average)

result = [num for num in range(1,10)]
print(result)

numbers = [1, 2, 3, 4, 5]

result=[]
for i in numbers:
    if i % 2 == 1:
        result.append(i*2)
    else:
        result.append(i)
print(result)

numbers
result = [i*2 for i in numbers if i % 2 == 1]
print(result)
        
        
        