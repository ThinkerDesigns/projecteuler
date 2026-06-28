# WIP - cheated a bit by asking gpt how to import and sort the names
names = []
with open('0022_names.txt', 'r') as file:
    fileContent = file.read().strip()

names = [name.strip('"') for name in fileContent.split(",")]
sum = 0
for x in range(1,len(names)):
    numtmp = 0
    for i in range(len(names[x])):
        tmp = (ord(names[x][i]) - 64)
        numtmp = numtmp + tmp
        print(numtmp,tmp)
    print(numtmp)
    print(numtmp * x)
    sum = sum + (numtmp * x)
print(sum)