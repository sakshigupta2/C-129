import csv
dataset1 = []
dataset2 = []
with open("dataset_1.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
with open("dataset_2.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
headers = dataset1[0]
planet_data = dataset1[1:]
headers1 = dataset2[0]
planet_data1 = dataset2[1:]
headersfinal = headers + headers1
planet_data2 = []
for index, data_row in enumerate(planet_data):
    planet_data2.append(planet_data[index]+planet_data1[index])
with open("final.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headersfinal)
    csvwriter.writerows(planet_data2)