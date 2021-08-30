#! /usr/bin/python

import math
import csv
from sklearn.preprocessing import scale
from sklearn.linear_model import *
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
        'print("notfound ",word)'




a=[]
happy_feature=[]
print("started")
for i in range(len(happy_map)):
        happy_feature.append(0)
    
for j in range(50000):
    
    for i in range(len(happy_map)):
        happy_feature[i]=0

    for k in range(5):
        v = random.randrange(1,len(happy_map))
        happy_feature[v]=1

    a.append(happy_feature)


y5=[]
for j in range(50000):
    y5.append(5)


b=[]

print("500 done")
for j in range(50000):
    for i in range(len(happy_map)):
        happy_feature[i]=0

    for k in range(3):
        happy_feature[int(random.randrange(1,len(happy_map)))]=1


    a.append(happy_feature)


for j in range(50000):
    y5.append(3)


c=[]    

print("300 done")

for j in range(50000):
    for i in range(len(happy_map)):
        happy_feature[i]=0


    happy_feature[int(random.randrange(1,len(happy_map)))]=1
    a.append(happy_feature)


for j in range(50000):
    y5.append(1)
    
'''
a = scale(a)
clf = svm.SVC(kernel = 'linear')
clf.fit(a, y5)

logit = LogisticRegression(C=1.0)

logit.fit(a,y5)
'''

text = []
for i in range(len(happy_map)):
        text.append(0)
        
for k in range(3):
        text[random.randrange(1,len(text))]=1

'''
print(clf.decision_function(text))
print(clf.score(text, [5], None))
print(clf.score(text, [3], None))
print(clf.score(text, [1], None))
print(clf.predict(text))


print ("predicted:", logit.predict(text))
print ("decision: ",logit.decision_function(a))
print ("probability",logit.predict_proba(text))

print ("params: ",logit.get_params(deep=True))
'''
