# loops in python

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " " + "Pie")

print(fruits)

heights = [123, 534, 533, 21, 1, 12, 324, 14, 1]

sum = 0

for n in heights:
    sum = sum + n

average = sum / len(heights) + 1
print(average)

num = [1, 4, 53, 53, 2]

n = 0

for a in num:
    if (a > n):
        n = a


print(n)

d = 0
for g in range(1, 101):
    d += g

print(d)


h = 0

for k in range(1, 101):
    if (k % 2 == 0):
        h += k
print(h)


# for k in range(1,101,2):
# h+=k
