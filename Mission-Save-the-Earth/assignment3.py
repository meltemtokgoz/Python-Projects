#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Student Name: MELTEM TOKGOZ
# Student ID: 21527381
# BBM103 Introduction to Programming Laboratory I, Fall 2016
# Assignment 3: Mission: Save the Earth
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import sys

inputfile1 = sys.argv[1]
infile1 = open(inputfile1,"r")
inputfile2 = sys.argv[2]
infile2 = open(inputfile2,"r")
inputfile3 = sys.argv[3]
infile3 = open(inputfile3, "r")

output1 = open("binarian_message.txt", "w")
output2 = open("computations.txt", "w")
output3 = open("message.txt", "w")

#mission-1

dict1={}
for line1 in infile1.readlines():
    line1 = line1.rstrip("\n")
    dictList1 = line1.split(" ")
    dict1[dictList1[0]] = dictList1[1]

textList = []
for line2 in infile2.readlines():
    line2 = line2.rstrip("\n")
    textList.append(line2.split())

def binarian_to_english(textList):
    for i in range(len(textList)):
        if textList[i][0] != '+':
            if textList[i][0][0] != '#':
                for m in range(len(textList[i])):
                    if textList[i][m] in dict1.keys():
                        textList[i][m] = dict1[textList[i][m]]
                satir=" ".join(textList[i])
                print(satir)
                output1.write(satir + "\n")

binarian_to_english(textList)

#mission-2

def ly_to_km(textList):
    for i in range(len(textList)):
        if textList[i][0] == '+':
            for m in range(len(textList[i])):
                f =textList[i][m]
                if f.isdigit() == True:
                    if dict1[textList[i][m - 1]] == 'distance':
                        f = int(f, 2)
                        f = f*(9.4607e+12)
                        f = float(f)
                        g ='%e' %f
                        print("Data about Binarian planet: ")
                        print("Distance from the Earth: {} km".format(g))
                        output2.write("Data about Binarian planet: "
                                      "\nDistance from the Earth: {} km".format(g))
ly_to_km(textList)

def binary_to_decimal(textList):
    for i in range(len(textList)):
        if textList[i][0] == '+':
            for m in range(len(textList[i])):
                a = textList[i][m]
                if a.isdigit() == True:
                    if dict1[textList[i][m-1]] == 'temperature':
                        b = int(a, 2)
                        b= float(b)
                        print("Planet temperature: {} degrees Celsius".format(b))
                        output2.write("\nPlanet temperature: {} degrees Celsius".format(b))
                c = textList[i][m]
                if c.isdigit() == True:
                    if dict1[textList[i][m - 1]] == 'orbital-speed':
                        d = int(c, 2)
                        d=float(d)
                        print("Orbital speed: {} km/s".format(d))
                        output2.write("\nOrbital speed: {} km/s".format(d))
binary_to_decimal(textList)

#mission-3

inputfile1 = sys.argv[1]
infile1 = open(inputfile1,"r")

dict2={}
for line1 in infile1.readlines():
    line1 = line1.rstrip("\n")
    dictList2 = line1.split(" ")
    dict2[dictList2[1]] = dictList2[0]

messageList=[]
for line3 in infile3.readlines():
    line3 = line3.rstrip("\n")
    line3 =line3.lower()
    messageList.append(line3.split())
    for a in range(len(messageList)):
        for b in range(len(messageList[a])):
            if messageList[a][b].endswith("!"):
                messageList[a][b] = messageList[a][b].replace("!", "")
            if messageList[a][b].endswith("."):
                messageList[a][b] = messageList[a][b].replace(".","")
            if messageList[a][b].endswith("?"):
                messageList[a][b] = messageList[a][b].replace("?","")
            if messageList[a][b].endswith(","):
                messageList[a][b] = messageList[a][b].replace(",","")

def english_to_binarian(messageList):
    for a in range(len(messageList)):
        for b in range(len(messageList[a])):
            n = messageList[a][b]
            if n.isdigit() == True:
                k = int(n)
                k = bin(k)[2:]
                messageList[a][b] = "".join(k)
            elif n.isdigit != True:
                if not messageList[a][b] in dict2.keys():
                    messageList[a][b] = messageList[a][b].capitalize()
                if messageList[a][b] in dict2.keys():
                    messageList[a][b] = dict2[messageList[a][b]]
        satir2 = " ".join(messageList[a])
        print(satir2)
        output3.write(satir2 + "\n")
english_to_binarian(messageList)

infile1.close()
infile2.close()
infile3.close()
output1.close()
output2.close()
output3.close()


