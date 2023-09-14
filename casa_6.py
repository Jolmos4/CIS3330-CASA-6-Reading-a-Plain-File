filename = './big-mac-full-index.csv'

fhand= open('./big-mac-full-index.csv')

count = 0 

for line in fhand:
    if "USA" in line:
        print(line)
        count += 1

fhand.close()
print("Total lines with 'USA':", count)








