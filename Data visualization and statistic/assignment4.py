#************************************************STEP1******************************************************************
import sys
candidates_name = sys.argv[2]
candidates =str(candidates_name).split(",")
list1 = []
list2 = []
states = []
candisates_list = []
def retieveData(login_file, candidates):
    input_file = open(login_file, "r")
    all_line =[]
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split(",")
        states.append(line[0])
        all_line.append(line)
    for cdd in candidates:
        candisates_list.append(cdd)
    if candisates_list[0] == all_line[0][3]:
        if len(candidates)==4:
            for k in range(1,len(all_line)):
                list1.append(all_line[k][3])
            for k in range(1,len(all_line)):
                list1.append(all_line[k][4])
            for k in range(1,len(all_line)):
                list1.append(all_line[k][5])
            for k in range(1,len(all_line)):
                list1.append(all_line[k][6])
        if len(candidates)==3:
            for k in range(1,len(all_line)):
                list1.append(all_line[k][3])
            for k in range(1,len(all_line)):
                list1.append(all_line[k][4])
            for k in range(1,len(all_line)):
                list1.append(all_line[k][5])
        if len(candidates)==2:
            for k in range(1,len(all_line)):
                list1.append(all_line[k][3])
            for k in range(1,len(all_line)):
                list1.append(all_line[k][4])

    if candisates_list[0] == all_line[0][2]:
        if len(candidates) == 2:
            for k in range(1,len(all_line)):
                list1.append(all_line[k][2])
            for k in range(1,len(all_line)):
                list1.append(all_line[k][3])
        if len(candidates) ==3:
            for k in range(1, len(all_line)):
                list1.append(all_line[k][2])
            for k in range(1, len(all_line)):
                list1.append(all_line[k][3])
            for k in range(1, len(all_line)):
                list1.append(all_line[k][4])
        if len(candidates) ==4:
            for k in range(1, len(all_line)):
                list1.append(all_line[k][2])
            for k in range(1, len(all_line)):
                list1.append(all_line[k][3])
            for k in range(1, len(all_line)):
                list1.append(all_line[k][4])
            for k in range(1, len(all_line)):
                list1.append(all_line[k][5])

    if len(all_line[1]) >=5:
        if candisates_list[0] == all_line[0][4]:
            if len(candidates)==4:
                for k in range(1,len(all_line)):
                    list1.append(all_line[k][4])
                for k in range(1,len(all_line)):
                    list1.append(all_line[k][5])
                for k in range(1,len(all_line)):
                    list1.append(all_line[k][6])
                for k in range(1,len(all_line)):
                    list1.append(all_line[k][7])
            if len(candidates)==3:
                for k in range(1,len(all_line)):
                    list1.append(all_line[k][4])
                for k in range(1,len(all_line)):
                    list1.append(all_line[k][5])
                for k in range(1,len(all_line)):
                    list1.append(all_line[k][6])
            if len(candidates)==2:
                for k in range(1,len(all_line)):
                    list1.append(all_line[k][4])
                for k in range(1,len(all_line)):
                    list1.append(all_line[k][5])

    for itm in list1:
        itms =int(itm)
        list2.append(itms)
    with open("retrievedData.txt", "w")as file_handler:
        for numberr in list2:
            file_handler.write("{} , ".format(numberr))

retieveData(sys.argv[1], candidates)
#*************************************************STEP2*****************************************************************
def DispBarPlot():
    import numpy as np
    import matplotlib.pyplot as plt
    #total vote finding
    total_list = []
    k = len(states[1:])
    total1 = sum(list2[0:k])
    total_list.append(total1)
    total2 = sum(list2[k:(2 * k)])
    total_list.append(total2)
    if len(candidates)>2:
        total3 = sum(list2[(2 * k):(3 * k)])
        total_list.append(total3)
    if len(candidates)>3:
        total4 = sum(list2[(3 * k):(4 * k)])
        total_list.append(total4)
    #first and second candidates finding
    if max(total_list) == total_list[0]:
        first_votes = (list2[0:k])
    if max(total_list) == total_list[1]:
        first_votes = (list2[k:(2*k)])
    if len(candidates) >2:
        if max(total_list) == total_list[2]:
            first_votes = (list2[(2*k):(3*k)])
    if len(candidates) >3:
        if max(total_list) == total_list[3]:
            first_votes = list2[(3*k):(4*k)]

    total_list.remove(max(total_list))
    tl2 = total_list
    if max(tl2) == tl2[0]:
        second_votes = (list2[k:(2*k)])
    if len(candidates)>2:
        if max(tl2) == tl2[1]:
            second_votes = (list2[(2*k):(3*k)])
    if len(candidates) > 3:
        if max(total_list) == tl2[2]:
            second_votes = (list2[(3*k):(4*k)])

    #GRAPH
    x_axis = len(states[1:])
    state_of_dist = np.arange(x_axis)
    bar_width = 0.30

    plt.bar(state_of_dist, second_votes, bar_width,align ="center",alpha=1.0,color='r',label=candisates_list[1])
    plt.bar(state_of_dist + bar_width, first_votes, bar_width,align="center",alpha=1.0,color='b',label=candisates_list[0])
    plt.xticks(state_of_dist + bar_width, (states[1:]),fontsize=8 ,rotation='vertical')
    plt.legend()
    plt.xlabel('States')
    plt.ylabel('Vote Count')
    plt.tight_layout()
    plt.savefig("ComparativeVotes.pdf")
    plt.show()
    plt.close()

DispBarPlot()
#******************************************STEP3************************************************************************
import matplotlib.pyplot as plt
import numpy as np

def compareVoteonBar(list):
    #Finding percentage percent of candidates
    k = len(states[1:])
    first = sum(list[0:k])
    second = sum(list[k:(2 * k)])
    if len(candidates) > 2:
        third = sum(list[(2 * k):(3 * k)])
    if len(candidates) > 3:
        fourth = sum(list[(3 * k):(4 * k)])

    def first_candidate(list):
        total = sum(list)
        aday_yüzde = (first / total) * 100
        f = round(aday_yüzde, 3)
        return f

    def second_candidate(list):
        total = sum(list)
        aday_yüzde = (second / total) * 100
        s = round(aday_yüzde, 3)
        return s

    if len(candidates) > 2:
        def third_candidate(list):
            total = sum(list)
            aday_yüzde = (third / total) * 100
            t = round(aday_yüzde, 3)
            return t

    if len(candidates) > 3:
        def fourth_candidate(list):
            total = sum(list)
            aday_yüzde = (fourth / total) * 100
            fa = round(aday_yüzde, 3)
            return fa
    #Graph
    if len(candidates) == 4:
        def candidate_stats():
            return first_candidate(list), second_candidate(list), third_candidate(list), fourth_candidate(list)
        fig, ax = plt.subplots()
        ind = np.arange(1, 5)
        plt.show(block=False)

        pa, pb, pc, pd = plt.bar(ind, candidate_stats())
        centers = ind + 0.5*pa.get_width()
        pa.set_facecolor('r')
        pb.set_facecolor('b')
        pc.set_facecolor('y')
        pd.set_facecolor('c')
        o, r, j, s = candidate_stats()
        pa.set_label(candisates_list[0])
        pb.set_label(candisates_list[1])
        pc.set_label(candisates_list[2])
        pd.set_label(candisates_list[3])
        pa.set_height(o)
        pb.set_height(r)
        pc.set_height(j)
        pd.set_height(s)
        ax.set_xticks(centers)
        ax.set_xlabel('Nominees')
        wa=str(first_candidate(list))+'%'
        wb=str(second_candidate(list))+'%'
        wc=str(third_candidate(list))+'%'
        wd=str(fourth_candidate(list))+'%'
        ax.set_xticklabels([wa,wb,wc,wd])
        ax.set_ylabel('Vote percentages')
        plt.legend()
        plt.savefig("CompVotePercs.pdf")
        plt.show()
        plt.close()

    if len(candidates) == 3:
        def candidate_stats():
            return first_candidate(list), second_candidate(list), third_candidate(list)

        fig, ax = plt.subplots()
        ind = np.arange(1, 4)
        plt.show(block=False)

        pa, pb, pc = plt.bar(ind, candidate_stats())
        centers = ind + 0.5*pa.get_width()
        pa.set_facecolor('r')
        pb.set_facecolor('b')
        pc.set_facecolor('y')
        o, r, j = candidate_stats()
        pa.set_label(candisates_list[0])
        pb.set_label(candisates_list[1])
        pc.set_label(candisates_list[2])
        pa.set_height(o)
        pb.set_height(r)
        pc.set_height(j)
        ax.set_xticks(centers)
        ax.set_xlabel('Nominees')
        wa = str(first_candidate(list)) + '%'
        wb = str(second_candidate(list)) + '%'
        wc = str(third_candidate(list)) + '%'
        ax.set_xticklabels([wa, wb, wc])
        ax.set_ylabel('Vote percentages')
        plt.legend()
        plt.savefig("CompVotePercs.pdf")
        plt.show()
        plt.close()

    if len(candidates) == 2:
        def get_stats():
            return first_candidate(list),second_candidate(list)

        fig, ax = plt.subplots()
        ind = np.arange(1, 3)
        plt.show(block=False)

        pa, pb = plt.bar(ind, get_stats())
        centers = ind + 0.5*pa.get_width()
        pa.set_facecolor('r')
        pb.set_facecolor('b')
        o, r = get_stats()
        pa.set_label(candisates_list[0])
        pb.set_label(candisates_list[1])
        pa.set_height(o)
        pb.set_height(r)
        ax.set_xticks(centers)
        ax.set_xlabel('Nominees')
        wa = str(first_candidate(list)) + '%'
        wb = str(second_candidate(list)) + '%'
        ax.set_xticklabels([wa, wb])
        ax.set_ylabel('Vote percentages')
        plt.legend()
        plt.savefig("CompVotePercs.pdf")
        plt.show()
        plt.close()

compareVoteonBar(list2)
#**************************************************STEP4****************************************************************
def obtainHistogram(list):
        zero_list = []
        for f in list:
            if len(f) >= 2:
                if f[-1] == '0':
                    zero_list.append(0)
                if f[-2] == '0':
                    zero_list.append(0)
            if len(f) <= 1:
                if f[-1] == '0':
                    zero_list.append(0)
        one_list=[]
        for f in list:
            if len(f) >= 2:
                if f[-1] == '1':
                    one_list.append(1)
                if f[-2] == '1':
                    one_list.append(1)
            if len(f) <= 1:
                if f[-1] == '1':
                    one_list.append(1)
        two_list =[]
        for f in list:
            if len(f) >= 2:
                if f[-1] == '2':
                    two_list.append(2)
                if f[-2] == '2':
                    two_list.append(2)
            if len(f) <= 1:
                if f[-1] == '2':
                    two_list.append(2)
        three_list = []
        for f in list:
            if len(f) >= 2:
                if f[-1] == '3':
                    three_list.append(3)
                if f[-2] == '3':
                    three_list.append(3)
            if len(f) <= 1:
                if f[-1] == '3':
                    three_list.append(3)
        four_list = []
        for f in list:
            if len(f) >= 2:
                if f[-1] == '4':
                    four_list.append(4)
                if f[-2] == '4':
                    four_list.append(4)
            if len(f) <= 1:
                if f[-1] == '4':
                    four_list.append(4)
        five_list = []
        for f in list:
            if len(f) >= 2:
                if f[-1] == '5':
                    five_list.append(5)
                if f[-2] == '5':
                    five_list.append(5)
            if len(f) <= 1:
                if f[-1] == '5':
                    five_list.append(5)
        six_list = []
        for f in list:
            if len(f) >= 2:
                if f[-1] == '6':
                    six_list.append(6)
                if f[-2] == '6':
                    six_list.append(6)
            if len(f) <= 1:
                if f[-1] == '6':
                    six_list.append(6)
        seven_list = []
        for f in list:
            if len(f) >= 2:
                if f[-1] == '7':
                    seven_list.append(7)
                if f[-2] == '7':
                    seven_list.append(7)
            if len(f) <= 1:
                if f[-1] == '7':
                    seven_list.append(7)
        eight_list = []
        for f in list:
            if len(f) >= 2:
                if f[-1] == '8':
                    eight_list.append(8)
                if f[-2] == '8':
                    eight_list.append(8)
            if len(f) <= 1:
                if f[-1] == '8':
                    eight_list.append(8)
        nine_list = []
        for f in list:
            if len(f) >= 2:
                if f[-1] == '9':
                    nine_list.append(9)
                if f[-2] == '9':
                    nine_list.append(9)
            if len(f) <= 1:
                if f[-1] == '9':
                    nine_list.append(9)
        list1 = []
        for f in list:
            k = float(f)
            list1.append(k)
        for f in list1:
            if f <= 10:
                zero_list.append(0)

        frekans = []
        f0 = len(zero_list) / (2 * len(list))
        frekans.append(f0)
        f1 = len(one_list) / (2 * len(list))
        frekans.append(f1)
        f2 = len(two_list) / (2 * len(list))
        frekans.append(f2)
        f3 = len(three_list) / (2 * len(list))
        frekans.append(f3)
        f4 = len(four_list) / (2 * len(list))
        frekans.append(f4)
        f5 = len(five_list) / (2 * len(list))
        frekans.append(f5)
        f6 = len(six_list) / (2 * len(list))
        frekans.append(f6)
        f7 = len(seven_list) / (2 * len(list))
        frekans.append(f7)
        f8 = len(eight_list) / (2 * len(list))
        frekans.append(f8)
        f9 = len(nine_list) / (2 * len(list))
        frekans.append(f9)
        return (frekans)

list3 =[]
for j in list2:
    y = str(j)
    list3.append(y)

graph0_mse= obtainHistogram(list3)
#************************************************STEP5******************************************************************
def plotHistogram(element1,element2,element3):
    import matplotlib.pyplot as plot
    plot.plot(element1,element2, linestyle='--', color='g',label='mean')
    plot.plot(element1,element3, color='r',label='Digit Dist')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.title('Histogram of least sign. digits')
    plot.legend(loc='upper left')
    plot.savefig("Histogram.pdf")
    plot.show()
    plot.close()

x =[0,1,2,3,4,5,6,7,8,9]
ab =[0.10,0.10,0.10,0.10,0.10,0.10,0.10,0.10,0.10,0.10]
plotHistogram(x,ab,graph0_mse)
#**********************************************STEP6********************************************************************
import matplotlib.pyplot as plot
import random
def plotHistogramWithSample():
    #1.sample
    list_a=[]
    for i in range(10):
        a = ("{:.3f}".format(random.uniform(0, 100)))
        list_a.append(a)
    x =[0,1,2,3,4,5,6,7,8,9]
    e= obtainHistogram(list_a)
    ae =[0.10,0.10,0.10,0.10,0.10,0.10,0.10,0.10,0.10,0.10]

    plot.plot(x,ae, linestyle='--', color='g',label='mean')
    plot.plot(x,e,color='r',label='Digit Dist')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.title('Histogram of least sign. digits - Sample:1')
    plot.legend(loc='upper left')
    plot.savefig("HistogramofSample1.pdf")
    plot.show()
    plot.close()
    #2.sample
    list_d=[]
    for x in range(50):
        d = ("{:.3f}".format(random.uniform(0, 100)))
        list_d.append(d)
    x =[0,1,2,3,4,5,6,7,8,9]
    a = obtainHistogram(list_d)

    plot.plot(x,ae, linestyle='--', color='g',label='mean')
    plot.plot(x,a,color='b',label='Digit Dist')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.title('Histogram of least sign. digits - Sample:2')
    plot.legend(loc='upper left')
    plot.savefig("HistogramofSample2.pdf")
    plot.show()
    plot.close()
    #3.sample
    list_g=[]
    for w in range(100):
        g = ("{:.3f}".format(random.uniform(0, 100)))
        list_g.append(g)
    x =[0,1,2,3,4,5,6,7,8,9]
    b =obtainHistogram(list_g)

    plot.plot(x,ae, linestyle='--', color='g',label='mean')
    plot.plot(x,b,color='y',label='Digit Dist')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.title('Histogram of least sign. digits - Sample:3')
    plot.legend(loc='upper left')
    plot.savefig("HistogramofSample3.pdf")
    plot.show()
    plot.close()
    #4.sample
    list_l=[]
    for t in range(1000):
        l = ("{:.3f}".format(random.uniform(0, 100)))
        list_l.append(l)
    x =[0,1,2,3,4,5,6,7,8,9]
    c =obtainHistogram(list_l)

    plot.plot(x,ae, linestyle='--', color='g',label='mean')
    plot.plot(x,c,color='c',label='Digit Dist')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.title('Histogram of least sign. digits - Sample:4')
    plot.legend(loc='upper left')
    plot.savefig("HistogramofSample4.pdf")
    plot.show()
    plot.close()
    #5.sample
    list_p=[]
    for v in range(10000):
        p = ("{:.3f}".format(random.uniform(0, 100)))
        list_p.append(p)
    x =[0,1,2,3,4,5,6,7,8,9]
    d =obtainHistogram(list_p)

    plot.plot(x,ae, linestyle='--', color='g',label='mean')
    plot.plot(x,d,color='m',label='Digit Dist')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.title('Histogram of least sign. digits - Sample:5')
    plot.legend(loc='upper left')
    plot.savefig("HistogramofSample5.pdf")
    plot.show()
    plot.close()

plotHistogramWithSample()
#************************************STEP7*****************************************************************
result_list=[]
def calculateMSE(list_x, list_y):
    z1 = (list_x[0] - list_y[0]) ** 2
    result_list.append(z1)
    z2 = (list_x[1] - list_y[1]) ** 2
    result_list.append(z2)
    z3 = (list_x[2] - list_y[2]) ** 2
    result_list.append(z3)
    z4 = (list_x[3] - list_y[3]) ** 2
    result_list.append(z4)
    z5 = (list_x[4] - list_y[4]) ** 2
    result_list.append(z5)
    z6 = (list_x[5] - list_y[5]) ** 2
    result_list.append(z6)
    z7 = (list_x[6] - list_y[6]) ** 2
    result_list.append(z7)
    z8 = (list_x[7] - list_y[7]) ** 2
    result_list.append(z8)
    z9 = (list_x[8] - list_y[8]) ** 2
    result_list.append(z9)
    z10 = (list_x[9] - list_y[9]) ** 2
    result_list.append(z10)
    return sum(result_list)

#MSE account for the two closest values
list_l=[]
for t in range(1000):
    l = ("{:.3f}".format(random.uniform(0, 100)))
    list_l.append(l)
c =obtainHistogram(list_l)

list_p=[]
for v in range(10000):
    p = ("{:.3f}".format(random.uniform(0, 100)))
    list_p.append(p)
d = obtainHistogram(list_p)

(calculateMSE(c,d))
#************************************STEP8******************************************************************************
def calculateMSEusaElection(x1):
    y1 =[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,]
    return(calculateMSE(x1,y1))

print("MSE value of 2012 USA election is {}".format(calculateMSEusaElection(graph0_mse)))
#**********************************STEP 9 and 10********************************************************************************
huge_list =[]
for x in range(10000):
    randoms_list = []
    for it in range(len(list2)):
        k = ("{:.3f}".format(random.uniform(0, 100)))
        randoms_list.append(k)
    huge_list.append(randoms_list)

huge_items_obtain =[]
for huge_items in huge_list:
    huge_items_obtain.append(obtainHistogram(huge_items))

listt1=[]
for dx in huge_items_obtain:
    listt1.append(calculateMSEusaElection(dx))

how_many = []
for value in listt1:
    if calculateMSEusaElection(graph0_mse) > value:
        how_many.append('*')
k = (len(how_many) / 10000)

output2=open("myAnswer.txt","w")
output2.write("\nThe number of MSE of random samples which are larger than or equal to USA election MSE is {}".format(
    len(how_many)))
output2.write("\nThe number of MSE of random samples which are smaller than USA election MSE is {}".format(
    10000 - len(how_many)))
output2.write("\n2012 USA election rejection level p is {}".format(k))

print("The number of MSE of random samples which are larger than or equal to USA election MSE is {}".format(
    len(how_many)))
print("The number of MSE of random samples which are smaller than USA election MSE is {}".format(
    10000 - len(how_many)))
print("2012 USA election rejection level p is {}".format(k))

if k<0.05:
    print("Finding: We reject the null hypothesis at the p={} level".format(k), file=output2)
else:
    print("Finding: There is no statistical evidence to reject null hypothesis", file=output2)

output2.close()