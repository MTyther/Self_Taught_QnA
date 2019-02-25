list1 = ["Top Gun", "Risky Business", "Minority Report"]
list2 = ["Titanic", "The Revenant", "Inception"]
list3 = ["Training Day", "Man on Fire", "Flight"]
total_list = [list1 + list2 + list3]

import csv
import os

print(total_list)

file_path = os.path.join("C:\\"...)

with open(file_path + "listfile.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(list1)
    w.writerow(list2)
    w.writerow(list3)


with open(file_path + "listfile.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row)) 
