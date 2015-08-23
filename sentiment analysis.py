#! /usr/bin/python

import math
import csv
from sklearn import svm
import random
text = open("happy.txt","r")
for line in text:
    words=line.split()

reader=csv.reader(open("positive words.csv"))
happy_map={row[1]:row[0] for row in reader}               


happy_vector=[]

for word in words:
    try:
        happy_vector.append(int(happy_map[word]))    
    except KeyError:
        print("notfound ",word)




a=[]
happy_feature=[]
print("started")
for i in range(len(happy_map)):
        happy_feature.append(0)
    
for j in range(500):
    
    for i in range(len(happy_map)):
        happy_feature[i]=0

    for k in range(5):
        v = random.randrange(1,len(happy_map))
        happy_feature[v]=1

    a.append(happy_feature)


y5=[]
for j in range(500):
    y5.append(5)


b=[]

print("500 done")
for j in range(300):
    for i in range(len(happy_map)):
        happy_feature[i]=0

    for k in range(3):
        happy_feature[int(random.randrange(1,len(happy_map)))]=1


    a.append(happy_feature)


for j in range(300):
    y5.append(3)


c=[]    

print("300 done")

for j in range(200):
    for i in range(len(happy_map)):
        happy_feature[i]=0


    happy_feature[int(random.randrange(1,len(happy_map)))]=1
    a.append(happy_feature)


for j in range(200):
    y5.append(1)
    

clf = svm.SVC()
clf.fit(a, y5)

text = []
for i in range(len(happy_map)):
        text.append(0)
        
for k in range(0):
        text[int(random.randrange(1,len(text)))]=1

print(clf.predict(text))

