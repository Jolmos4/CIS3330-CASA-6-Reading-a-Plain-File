filename = './big-mac-full-index.csv'

file = open(filename)
count = 0 
for line in file:
    if 'USA' in line:
        print(line)
        count += 1
print(count)
