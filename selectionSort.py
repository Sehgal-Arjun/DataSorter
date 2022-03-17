import matplotlib.pyplot as plt
import random

list = []
xAxis = []
yAxis = []
finished = False
count = 0

#plt.ion()

def selectionSort(i):
    minIndex = i
    holder = i

    for w in range(len(list) - i):
        if list[w+i] < list[minIndex]:
            minIndex = w+i
        else:
            minIndex = minIndex

    temp = list[minIndex]
    list[minIndex] = list[i]
    list[i] = temp

    xAxis.clear()
    yAxis.clear()
    for j in list:
        xAxis.append(str(list[j]))
        yAxis.append(list[j])

def check():
    for i in range(len(list)):
        if i!=len(list) -1:
            if list[i] > list[i+1]:
                return False
    return True

def close():
    plt.figure().clear()
    plt.close('all')
    plt.cla()
    plt.clf()

#Making the initial List:
for i in range(100):
    list.append(i)
random.shuffle(list)
#*/

for a in range(len(list)):
    xAxis.append(str(list[a]))
    yAxis.append(list[a])

fig = plt.figure(figsize = (12, 6))
plt.bar(xAxis,yAxis)
plt.title('Selection Sort')
plt.show()

while check() == False:
    close()
    fig = plt.figure(figsize = (12, 6))
    plt.bar(xAxis,yAxis)
    
    selectionSort(count)

    #yAxis[2] += 5
    plt.title('Selection Sort')
    plt.draw()
    plt.pause(0.0001)
    count+=1

plt.show()
