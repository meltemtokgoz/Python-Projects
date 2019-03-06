import sys
inputfile=sys.argv[1]
infile = open(inputfile,"r")

output = []

for item in infile.readlines():
    ListIntegers = item.split(";")

def avgFirstThreeDigit(ListIntegers):
    for item in ListIntegers:
        total=0
        count = 3
        for number in item[:3]:
            total += int(number)
            average = total / count
        output.append(average)
    return output

newListIntegers = []
for i in ListIntegers:
    newListIntegers.insert(0,i)

print(avgFirstThreeDigit(newListIntegers))

infile.close()