#Question1:
list1 = []
list2 = []
sum = 0
with open('Data Question 6 Transaction.log', 'r') as f:
    content = f.readlines()
    for x in content:
        row = x.split()
        list1.append(str(row[0]))
        list2.append(int(row[1]))
n = len(list1)
for x in range(1,n):
    if list1[x] == 'D':
        sum = sum + list2[x]
    elif list1[x] == 'W':
        sum = sum - list2[x]
print(sum)
with open('Data Question 6 Transaction.log', 'a') as myfile:
    myfile.write("\n"+str(sum))

