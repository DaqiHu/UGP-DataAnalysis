li = [2, 3, 5, 11, 7]

count = 0
for i in li:
    if count == 2:
        li.remove(i)
    count += 1

for i in li:
    print(i)