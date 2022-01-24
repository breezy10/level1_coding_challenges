# task1.1
nums = [3, 5]

result = 0
for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)


# task 1.2
def number3(x, y):
   if x == 3 or y == 3 or (x+y) == 3:
       return True
   else:
       return False
print(number3(6, 7))
