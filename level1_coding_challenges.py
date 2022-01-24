# task 1.1

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



# task 1.3

def number65(x, y):
   if x == 65 or y == 65 or (x+y) == 65:
       return True
   else:
       return False
print(number65(6, 58))



#task 1.4

def square(n):
    for i in range(n):
        for j in range(n):
            print("# " ,end="")
        print()
square(20)


# task 1.5

n = 3
b = 0
def triangle(n):
    if n>0:
        for i in range(0, n):
            for j in range(0, i+1):
                print("# ",end="")
        
            print("\r")
    else:
        n = abs(n)
        for i in range(n, 0, -1):
            for j in range(0, i):
                print('#', end=' ')
            print("\r")
triangle(-2)


# task 1.6

def logest_string(str_list):
    longest = max(str_list, key = len)
    length_count = len(longest)
    for word in str_list:
        if len(word) == length_count:
            print(word)
        
logest_string(["people", "apple", "lemons"])


# task 1.7

list1 = [10, 15, 20, 30]
list2 = [5, 7, 9, 14]

def combine_lists(list1,list2):
    newlist = []
    for i in range(len(list1)):
        newlist.append(list1[i])
        newlist.append(list2[i])
    return newlist
print(combine_lists(list1,list2))

