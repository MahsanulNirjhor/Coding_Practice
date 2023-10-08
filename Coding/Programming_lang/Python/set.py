s1 = set()
s2 = {}

print(type(s1))
print(type(s2))

s2 = {1:2, 3:4, 5:6}
print(s2)

s2[2] = 10
print(s2[1])
print(s2[2])

# Check an element in s2
# if 1 in s2:
#     print("Yes")

# check a key in s2
if 2 not in s2:
    print("yes")

for i in range(len(s2) - 1):
    print(i)

s3 = {7: 0, 2: 1}

result = 9 - 2

if result in s3:
    print("Ache ")
