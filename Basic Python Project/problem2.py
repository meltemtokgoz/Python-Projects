import sys
inputfile=sys.argv[1]
infile = open(inputfile,"r")

resultList = []
def calculateTotalCost(list):
    total = 0
    for i in range(len(list)):
            total = ((list[i][0]) + (10*list[i][1]) + (10*list[i][0]*list[i][2]))
            resultList.append(total)
    return resultList

def displayCost(list1):
    displayList = calculateTotalCost(list1)
    for f in range (len(list1)):
        answer= "{}. House's Total Coast is {}"
        print(answer.format(f+1,displayList[f]))

def selectBestBuy(list2):
    BestBuyList = calculateTotalCost(list2)
    good_choice = min(BestBuyList)
    the_best = "You should select {}. House whose total cost is {}"
    print(the_best.format((BestBuyList.index(good_choice)+1),good_choice))

BulletList= []

for line in infile.readlines():
    BulletList.append(line.split( ))

for i in range(len(BulletList)):
    BulletList[i][0] = float(BulletList[i][0])
    BulletList[i][1] = float(BulletList[i][1])
    BulletList[i][2] = float(BulletList[i][2])

displayCost(BulletList)
selectBestBuy(BulletList)

infile.close()

