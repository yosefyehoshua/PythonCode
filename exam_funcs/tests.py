

import re

import csv


def totParkSpots(file):
    areaList = [0 for i in range(50)]
    countList = [0 for i in range(100000)]
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] != "DeviceId":
                if countList[int(row[1])] == 0:
                    countList[int(row[1])] += 1
                    areaList[int(row[5])] += 1

    data = [["area", "no. of park_space"]]
    for i in range(len(areaList)):

        if areaList[i] != 0:
            data.append([str(i), str(areaList[i])])
            print("in area: " + str(i) + " there is: " + str(
                areaList[i]) + " parkings spots")

    print(data)
    sums = 0
    for i in range(len(data)):
        if i != 0:
            sums += int(data[i][1])

    with open('constrationPerArea.csv', 'w') as g:

        newCsv = csv.writer(g)
        newCsv.writerows(data)

    return sums



def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365
    # leap year correction
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)
    dayOfWeek %= 7
    return dayOfWeek + 1

areaList = [0 for i in range(50)]
ocupSpots = [0 for i in range(24)]
countList = [0 for i in range(100000)]
with open('outfileFull.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] != "DeviceId":
            matchAr = re.search(
                # group 1 = "date": group 5 = HH: group 6 = MM group 8 = PM/AM
                r'((\d+)/(\d+)/(\d+))\s\b(1[0-2]|0?[1-9]):([0-5][0-9]):([0-5]'
                r'[0-9])\s([AaPp][Mm])\s\+0000', row[2])
            matchDp = re.search(
                # group 1 = "date": group 5 = HH: group 6 = MM group 8 = PM/AM
                r'((\d+)/(\d+)/(\d+))\s\b(1[0-2]|0?[1-9]):([0-5][0-9]):([0-5]'
                r'[0-9])\s([AaPp][Mm])\s\+0000', row[3])
            for i in range(24):
                if i == int(matchAr.group(5)):
                    if matchAr.group(8) == "PM":
                        ocupSpots[i+11] += 1
                    else:
                        ocupSpots[i]+=1
                    if i == int(matchDp.group(5)):
                        if matchAr.group(8) == "PM":
                            ocupSpots[i + 11] -= 1

                        else:
                            ocupSpots[i] -= 1



    print(ocupSpots)


sums = totParkSpots("outfileFull.csv")
print(sums)


